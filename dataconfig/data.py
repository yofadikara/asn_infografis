from datetime import datetime, timedelta
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
    print("Nama tabel yang digunakan:", nama_table)
    return nama_table

'''namatable = get_table_name()
print("Nama tabel yang digunakan:", namatable)'''

#Ambil Data PNS Backup
'''def get_asn_data(conn, nama_table):
    query = f"SELECT * FROM {nama_table} LIMIT 5"
    return pd.read_sql_query(query, conn)'''

#Contoh Eksekusi
'''if __name__ == "__main__":
    params = load_env()
    conn = connect_db(params)
    if conn:
        nama_table = get_table_name()
        print("Nama tabel yang digunakan:", nama_table)
        asn_data = get_asn_data(conn, nama_table)
        print(asn_data.head())
        
        conn.close()
    else:
        print("Tidak dapat mengambil data karena koneksi gagal.")'''

#Populate Tanggal Data
def get_tanggal_data():
    from dataconfig.mapping import bulan_map_id
    today = datetime.now()
    bulan = bulan_map_id[today.month]
    return f"1 {bulan} {today.year}"

#Ambil Data Berdasarkan Cepat Kode dan Kategori
def get_data(conn, cepat_kode, kategori, table_name):
    from template.query_templates import queries
    query = queries[kategori].format(cepat_kode=cepat_kode, table_name=table_name)
    return pd.read_sql_query(query, conn)

#Penambahan Persentase
def tambah_persentase(df, kolom_jumlah = 'count'):
    total = df[kolom_jumlah].sum()
    min_visual = 1.0
    base_visual = 0.0
    if total == 0:
        df['persentase_raw'] = 0
    else:
        df['persentase_raw'] = (df[kolom_jumlah] / total * 100).round(2)
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

#Pengambilan All Data
def get_all_data(conn, table_name):
    data = {}
    kategori_list = ["Jenis_ASN","Jenis_Kelamin", "Pendidikan",
                     "Masa_Kerja", "Kelompok_Usia", "Jenis_Jabatan"]
    from template.query_templates import get_provinsi_list
    provinsi_list = get_provinsi_list(conn)
    for prov in provinsi_list:
        nama = prov['nama']
        cepat_kode = prov['cepat_kode']
        data[nama] = {}
        for kategori in kategori_list:
            data[nama][kategori] = get_data(conn, cepat_kode, kategori, table_name)
    return data

#Pembuatan Kelompok Jabatan
def klasifikasi_kelompok_jabatan(df, kolom_sumber='jenisjabatan'):
    mapping = {
        'Struktural': ['PSN JPT Utama','PNS JPT Madya','PNS JPT Pratama','PPPK JPT Utama',
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
    return df

#Ringkasan Kelompok Jabatan
def ringkasan_kelompok_jabatan(df):
    total_per_kelompok = (
        df.groupby("kelompok_jabatan")['count'].sum().reset_index()
    )
    total_per_kelompok.columns = ['kelompok_jabatan', 'count']
    total_per_kelompok = tambah_persentase(total_per_kelompok, kolom_jumlah='count')
    return total_per_kelompok