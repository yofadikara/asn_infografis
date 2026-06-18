from datetime import datetime, timedelta
import warnings
warnings.filterwarnings(
    "ignore",
    message=".*pandas only supports SQLAlchemy connectable.*"
)
import pandas as pd
from dataconfig.db_config import connect_db, load_env

#Nama Table PNS Backup    
def get_table_name(bulan = None, tahun = None, schema = "dwstat"):
    if bulan and tahun:
        bulan_lalu = datetime(tahun, bulan, 1) - timedelta(days=1)
    else:
        now = datetime.now()
        bulan_lalu = datetime(now.year, now.month, 1) - timedelta(days=1)
    nama_table = f"{schema}.pnsbackup{bulan_lalu.year}{bulan_lalu.month:02}"
    return nama_table

#Populate Tanggal Data
def get_tanggal_data():
    from dataconfig.mapping import bulan_map_id
    today = datetime.now()
    bulan = bulan_map_id[today.month]
    return f"1 {bulan} {today.year}"

#Pengambilan All Data
def get_all_data(conn, table_name, target_list, mode):
    data = {}
    kategori_default = ["Jenis_ASN","Jenis_Kelamin", "Pendidikan",
                     "Kelompok_Generasi", "Jenis_Jabatan"]
    kategori_nasional = ["Jenis_ASN","Jenis_Instansi","Jenis_Kelamin",
                         "Kelompok_Generasi","Pendidikan","Jenis_Jabatan"]
    for target in target_list:
        if mode == 'nasional':
            nama = 'Nasional'
            cepat_kode = None
            kategori_list = kategori_nasional
        elif mode == 'instansi':
            nama = target['nama']
            cepat_kode = target['cepat_kode']
            kategori_list = kategori_default
        elif mode == 'all':
            nama = target['nama']
            cepat_kode = target['cepat_kode']
            instansi_id = target['id']
            kategori_list = kategori_default
        elif mode == 'provinsi':
            wilayah = target['wilayah']
            cepat_kode = target['prefix']
            nama = f"Provinsi {wilayah.title()}"
            kategori_list = kategori_default
        elif mode == 'kanreg':
            kanreg = target['nama']
            cepat_kode = target['id']
            nama = f"Wilker {kanreg}"
            kategori_list = kategori_default
        else:
            raise ValueError("Mode harus 'instansi', 'provinsi', atau 'kanreg'")
        if mode == "all":
            data[nama] = {"instansi_id":instansi_id, "kategori":{}}  
        else: 
            data[nama] = {}
        for kategori in kategori_list:
            if mode == "all":
                data[nama]["kategori"][kategori] = get_data(conn, cepat_kode, kategori, table_name, mode)
            else : 
                data[nama][kategori] = get_data(conn, cepat_kode, kategori, table_name, mode)
        '''print("Isi data_dict keys:", list(data.keys()))'''
    return data

#Ambil Data Berdasarkan Cepat Kode dan Kategori
def get_data(conn, cepat_kode, kategori, table_name, mode):
    from template.query_templates import queries, queries_provinsi, queries_kanreg, queries_nasional
    if mode == 'nasional':
        query = queries_nasional[kategori].format(table_name=table_name)
    elif mode == 'instansi':
        query = queries[kategori].format(cepat_kode=cepat_kode, table_name=table_name)
    elif mode == 'all':
        query = queries[kategori].format(cepat_kode=cepat_kode, table_name=table_name)
    elif mode == 'provinsi':
        query = queries_provinsi[kategori].format(cepat_kode=cepat_kode, table_name=table_name)
    elif mode == 'kanreg':
        query = queries_kanreg[kategori].format(cepat_kode=cepat_kode, table_name=table_name)
    else:
        raise ValueError("Mode harus 'instansi' atau 'wilker'")
    return pd.read_sql_query(query, conn)

#Penambahan Persentase
def tambah_persentase(df, kolom_jumlah = 'count'):
    total = df[kolom_jumlah].sum()
    min_visual = 1.0
    base_visual = 0.0
    if total == 0:
        df['persentase_raw'] = 0
    else:
        df['persentase_raw'] = (df[kolom_jumlah] / total * 100).round(5)
    df['persentase_vis'] = df['persentase_raw'].apply(lambda x: min_visual if x < min_visual and x > base_visual else int(round(x))
                                                      if pd.notnull(x) else 0)
    excess = df['persentase_vis'].sum() - 100
    if excess > 0:
        df_sorted = df.sort_values(by='persentase_vis', ascending=False)
        for i in df_sorted.index:
            available = df.at[i, 'persentase_vis'] - excess
            potong = min(excess, available)
            df.at[i, 'persentase_vis'] -= potong
            excess -= potong
            if excess <= 0:
                break
    elif excess < 0 :
        df_sorted = df.sort_values(by='persentase_vis', ascending=True)
        for i in df_sorted.index:
            available = 100 - df.at[i, 'persentase_vis']
            tambah = min(-excess, available)
            df.at[i, 'persentase_vis'] += tambah
            excess += tambah
            if excess >= 0:
                break
    df['persentase_vis_num'] = df['persentase_vis'].astype(int)
    df['persentase_vis'] = df['persentase_vis_num'].astype(str)+'%'
    return df

#Pembuatan Kelompok Jabatan
'''def klasifikasi_kelompok_jabatan(df, kolom_sumber='jenisjabatan'):
    mapping = {
        'Struktural': ['PNS JPT Utama','PNS JPT Madya','PNS JPT Pratama','PPPK JPT Utama',
                       'PPPK JPT Madya','PPPK JPT Pratama', 'Administrator',
                       'Pengawas','Eselon V'],
        'Fungsional': ['PNS JF Dosen','PNS JF Guru','PNS JF Medis','PNS JF Kesehatan','PNS JF Teknis',
                       'PPPK JF Dosen','PPPK JF Guru','PPPK JF Medis','PPPK JF Medis',
                       'PPPK JF Teknis'],
        'Pelaksana': ['Pelaksana','PPPK Pelaksana']
    }
    def klasifikasi(jenis):
        for kelompok, jenis_list in mapping.items():
            if jenis in jenis_list:
                return kelompok
    df['kelompok_jabatan'] = df[kolom_sumber].apply(klasifikasi)
    return df'''

#Ringkasan Kelompok Jabatan
def ringkasan_kelompok_jabatan(df):
    total_per_kelompok = (
        df.groupby("kelompok_jabatan")['count'].sum().reset_index()
    )
    total_per_kelompok.columns = ['kelompok_jabatan', 'count']
    total_per_kelompok = tambah_persentase(total_per_kelompok, kolom_jumlah='count')
    return total_per_kelompok
                