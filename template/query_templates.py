import warnings
warnings.filterwarnings(
    "ignore",
    message=".*pandas only supports SQLAlchemy connectable.*"
)
import pandas as pd
from dataconfig.data import get_table_name

#All Instansi
def get_all_instansi(conn):
    query = """SELECT id, cepat_kode, nama
                FROM ref.instansi WHERE status = 'A'"""
    df = pd.read_sql_query(query,conn)
    return df.to_dict(orient='records')

#Cepat Kode Provinsi
def get_instansi_list(conn, instansi_filter):
    if not instansi_filter:
        return[]
    query = """SELECT cepat_kode, nama 
            FROM ref.instansi WHERE
            nama ILIKE %s
            --jenis_instansi_id = 'PROV'"""
    params = [f"%{instansi_filter}%"]
    df = pd.read_sql_query(query, conn, params=params)
    return df.to_dict(orient='records')

#Query Infografis
table_name = get_table_name()
queries = {
    "Jenis_ASN":
    f"""SELECT p.jenis_asn, count(*) 
    from {table_name} p
    where p.cepat_kode_instansi_kerja = '{{cepat_kode}}'
    --and p.jenis_instansi_kerja = 'D' 
    --and (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92'))
    and p.status_instansi_kerja = 'A'
    group by p.jenis_asn
    """,
    "Jenis_Kelamin":
    f"""select p.jenis_kelamin , count(*) 
    from {table_name} p
    where p.cepat_kode_instansi_kerja = '{{cepat_kode}}'
    --and p.jenis_instansi_kerja = 'D' 
    --and (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92'))
    and p.status_instansi_kerja = 'A'
    group by p.jenis_kelamin""",
    "Pendidikan":
    f"""select tingkatpendidikan,
    b.count from (
    select tingkatpendidikan,
        case tingkatpendidikan
        when 'SD-SMA' then 1
        when 'DI-DIII' then 2
        when 'DIV/S1' then 3
        when 'S2' then 4
        when 'S3' then 5
        end as urutan,
    a.count
    from (
    select 
        case 
	    when p.tingkat_pendidikan in ('Diploma I','Diploma II') or p.tingkat_pendidikan ilike '%Diploma III%' then 'DI-DIII'
	    when p.tingkat_pendidikan ilike '%diploma%IV%' or p.tingkat_pendidikan ilike '%S-1%' or p.tingkat_pendidikan = 'Profesi' then 'DIV/S1'
	    when p.tingkat_pendidikan ilike '%s%2%' or p.tingkat_pendidikan = 'Spesialis' then 'S2'
	    when p.tingkat_pendidikan ilike '%s%3%' or p.tingkat_pendidikan = 'Subspesialis' then 'S3'
	    when p.tingkat_pendidikan IN ('Sekolah Dasar','SLTP','SLTP Kejuruan','SLTA','SLTA Kejuruan','SLTA Keguruan') THEN 'SD-SMA'
        else p.tingkat_pendidikan
        end as tingkatpendidikan, 
    count(*) from {table_name} p
    join ref.instansi i on p.instansi_kerja_id = i.id
    where p.cepat_kode_instansi_kerja = '{{cepat_kode}}'
    --and (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92'))
    and p.status_instansi_kerja = 'A'
    group by tingkatpendidikan 
    )a
    )b
    order by b.urutan""",
    "Kelompok_Generasi":
    f"""select p.kelompok_generasi  , count(*) from {table_name} p
    where p.cepat_kode_instansi_kerja = '{{cepat_kode}}'
    --and p.jenis_instansi_kerja = 'D' 
    --and (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92'))
    and p.status_instansi_kerja = 'A'
    group by p.kelompok_generasi""",
    "Jenis_Jabatan":
    f"""SELECT 
    CASE
	    WHEN p.jenis_kelompok_jabatan IN ('JPT Madya','JPT Pratama','JPT Utama','Administrator','Pengawas','Eselon V') THEN 'Struktural'
	    WHEN p.jenis_kelompok_jabatan = 'JF Dosen' THEN 'JF Dosen'
	    WHEN p.jenis_kelompok_jabatan = 'JF Guru' THEN 'JF Guru'
	    WHEN p.jenis_kelompok_jabatan = 'JF Kesehatan' THEN 'JF Kesehatan'
	    WHEN p.jenis_kelompok_jabatan = 'JF Teknis' THEN 'JF Teknis'
	    WHEN p.jenis_kelompok_jabatan ILIKE '%pelaksana%' THEN 'Pelaksana'
    END AS kelompok_jabatan,
    CASE
      WHEN p.jenis_kelompok_jabatan = 'JPT Utama' AND p.jenis_asn = 'PNS' THEN 'PNS JPT Utama'
	    WHEN p.jenis_kelompok_jabatan = 'JPT Utama' AND p.jenis_asn = 'PPPK' THEN 'PPPK JPT Utama'
	    WHEN p.jenis_kelompok_jabatan = 'JPT Madya' AND p.jenis_asn = 'PNS' THEN 'PNS JPT Madya'
	    WHEN p.jenis_kelompok_jabatan = 'JPT Madya' AND p.jenis_asn = 'PPPK' THEN 'PPPK JPT Madya'
	    WHEN p.jenis_kelompok_jabatan = 'JPT Pratama' AND p.jenis_asn = 'PNS' THEN 'PNS JPT Pratama'
	    WHEN p.jenis_kelompok_jabatan = 'JPT Pratama' AND p.jenis_asn = 'PPPK' THEN 'PNS JPT Pratama'
	    WHEN p.jenis_kelompok_jabatan = 'JF Dosen' AND p.jenis_asn = 'PNS' THEN 'PNS'
	    WHEN p.jenis_kelompok_jabatan = 'JF Guru' AND p.jenis_asn = 'PNS' THEN 'PNS'
	    WHEN p.jenis_kelompok_jabatan = 'JF Kesehatan' AND p.jenis_asn = 'PNS' THEN 'PNS'
	    WHEN p.jenis_kelompok_jabatan = 'JF Teknis' AND p.jenis_asn = 'PNS' THEN 'PNS'
	    WHEN p.jenis_kelompok_jabatan = 'JF Dosen' AND p.jenis_asn = 'PPPK' THEN 'PPPK'
	    WHEN p.jenis_kelompok_jabatan = 'JF Guru' AND p.jenis_asn = 'PPPK' THEN 'PPPK'
	    WHEN p.jenis_kelompok_jabatan = 'JF Kesehatan' AND p.jenis_asn = 'PPPK' THEN 'PPPK'
	    WHEN p.jenis_kelompok_jabatan = 'JF Teknis' AND p.jenis_asn = 'PPPK' THEN 'PPPK'
	    WHEN p.jenis_kelompok_jabatan = 'JF Dosen' AND p.jenis_asn = 'PPPK Paruh Waktu' THEN 'PPPK Paruh Waktu'
	    WHEN p.jenis_kelompok_jabatan = 'JF Guru' AND p.jenis_asn = 'PPPK Paruh Waktu' THEN 'PPPK Paruh Waktu'
	    WHEN p.jenis_kelompok_jabatan = 'JF Kesehatan' AND p.jenis_asn = 'PPPK Paruh Waktu' THEN 'PPPK Paruh Waktu'
	    WHEN p.jenis_kelompok_jabatan = 'JF Teknis' AND p.jenis_asn = 'PPPK Paruh Waktu' THEN 'PPPK Paruh Waktu'
	    WHEN p.jenis_kelompok_jabatan ILIKE '%pelaksana%' AND p.jenis_asn = 'PNS' THEN 'PNS'
	    WHEN p.jenis_kelompok_jabatan ILIKE '%pelaksana%' AND p.jenis_asn = 'PPPK' THEN 'PPPK'
	    WHEN p.jenis_kelompok_jabatan ILIKE '%pelaksana%' AND p.jenis_asn = 'PPPK Paruh Waktu' THEN 'PPPK Paruh Waktu'
	    ELSE p.jenis_kelompok_jabatan
    END AS jabatan,
    COUNT(*)
    FROM {table_name} p
    where p.cepat_kode_instansi_kerja = '{{cepat_kode}}'
    --and p.jenis_instansi_kerja = 'D' 
    --and (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92'))
    and p.status_instansi_kerja = 'A'
    group by jabatan,kelompok_jabatan
    """
}

#Provinsi
def get_provinsi_prefix(conn, wilayah_name):
    query = """SELECT nama as prefix 
            FROM ref.lokasi WHERE
            nama ILIKE %s AND jenis = 'P'"""
    df = pd.read_sql_query(query, conn, params=[f"%{wilayah_name}%"])
    prefix_list = df['prefix'].tolist()
    #penambahan kolom wilayah
    return [{'prefix': p, 'wilayah': wilayah_name} for p in prefix_list]

def get_all_provinsi(conn):
    query = "SELECT id AS provinsi_id, nama FROM REF.lokasi WHERE jenis = 'P' AND kode_kemendagri IS NOT NULL"
    df = pd.read_sql_query(query,conn)
    return df.to_dict(orient='records')

#Query Infografis provinsi
table_name = get_table_name()
queries_provinsi = {
    "Jenis_ASN":
    f"""SELECT p.jenis_asn, count(*) 
    from {table_name} p
    where p.lokasi_kerja_clean ilike '{{cepat_kode}}%'
    --and p.jenis_instansi_kerja = 'D' 
    --and (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92'))
    and p.status_instansi_kerja = 'A'
    group by p.jenis_asn
    """,
    "Jenis_Kelamin":
    f"""select p.jenis_kelamin , count(*) 
    from {table_name} p
    where p.lokasi_kerja_clean ilike '{{cepat_kode}}%'
    --and p.jenis_instansi_kerja = 'D' 
    --and (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92'))
    and p.status_instansi_kerja = 'A'
    group by p.jenis_kelamin""",
    "Pendidikan":
    f"""select tingkatpendidikan,
    b.count from (
    select tingkatpendidikan,
        case tingkatpendidikan
        when 'SD-SMA' then 1
        when 'DI-DIII' then 2
        when 'DIV/S1' then 3
        when 'S2' then 4
        when 'S3' then 5
        end as urutan,
    a.count
    from (
    select 
        case 
	    when p.tingkat_pendidikan in ('Diploma I','Diploma II') or p.tingkat_pendidikan ilike '%Diploma III%' then 'DI-DIII'
	    when p.tingkat_pendidikan ilike '%diploma%IV%' or p.tingkat_pendidikan ilike '%S-1%' or p.tingkat_pendidikan = 'Profesi' then 'DIV/S1'
	    when p.tingkat_pendidikan ilike '%s%2%' or p.tingkat_pendidikan = 'Spesialis' then 'S2'
	    when p.tingkat_pendidikan ilike '%s%3%' or p.tingkat_pendidikan = 'Subspesialis' then 'S3'
	    when p.tingkat_pendidikan IN ('Sekolah Dasar','SLTP','SLTP Kejuruan','SLTA','SLTA Kejuruan','SLTA Keguruan') THEN 'SD-SMA'
        else p.tingkat_pendidikan
        end as tingkatpendidikan, 
    count(*) from {table_name} p
    join ref.instansi i on p.instansi_kerja_id = i.id
    where p.lokasi_kerja_clean ilike '{{cepat_kode}}%'
    --and (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92'))
    and p.status_instansi_kerja = 'A'
    group by tingkatpendidikan 
    )a
    )b
    order by b.urutan""",
    "Kelompok_Generasi":
    f"""select p.kelompok_generasi  , count(*) from {table_name} p
    where p.lokasi_kerja_clean ilike '{{cepat_kode}}%'
    --and p.jenis_instansi_kerja = 'D' 
    --and (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92'))
    and p.status_instansi_kerja = 'A'
    group by p.kelompok_generasi""",
    "Jenis_Jabatan":
    f"""SELECT 
    CASE
	    WHEN p.jenis_kelompok_jabatan IN ('JPT Madya','JPT Pratama','JPT Utama','Administrator','Pengawas','Eselon V') THEN 'Struktural'
	    WHEN p.jenis_kelompok_jabatan = 'JF Dosen' THEN 'JF Dosen'
	    WHEN p.jenis_kelompok_jabatan = 'JF Guru' THEN 'JF Guru'
	    WHEN p.jenis_kelompok_jabatan = 'JF Kesehatan' THEN 'JF Kesehatan'
	    WHEN p.jenis_kelompok_jabatan = 'JF Teknis' THEN 'JF Teknis'
	    WHEN p.jenis_kelompok_jabatan ILIKE '%pelaksana%' THEN 'Pelaksana'
    END AS kelompok_jabatan,
    CASE
      WHEN p.jenis_kelompok_jabatan = 'JPT Utama' AND p.jenis_asn = 'PNS' THEN 'PNS JPT Utama'
	    WHEN p.jenis_kelompok_jabatan = 'JPT Utama' AND p.jenis_asn = 'PPPK' THEN 'PPPK JPT Utama'
	    WHEN p.jenis_kelompok_jabatan = 'JPT Madya' AND p.jenis_asn = 'PNS' THEN 'PNS JPT Madya'
	    WHEN p.jenis_kelompok_jabatan = 'JPT Madya' AND p.jenis_asn = 'PPPK' THEN 'PPPK JPT Madya'
	    WHEN p.jenis_kelompok_jabatan = 'JPT Pratama' AND p.jenis_asn = 'PNS' THEN 'PNS JPT Pratama'
	    WHEN p.jenis_kelompok_jabatan = 'JPT Pratama' AND p.jenis_asn = 'PPPK' THEN 'PNS JPT Pratama'
	    WHEN p.jenis_kelompok_jabatan = 'JF Dosen' AND p.jenis_asn = 'PNS' THEN 'PNS'
	    WHEN p.jenis_kelompok_jabatan = 'JF Guru' AND p.jenis_asn = 'PNS' THEN 'PNS'
	    WHEN p.jenis_kelompok_jabatan = 'JF Kesehatan' AND p.jenis_asn = 'PNS' THEN 'PNS'
	    WHEN p.jenis_kelompok_jabatan = 'JF Teknis' AND p.jenis_asn = 'PNS' THEN 'PNS'
	    WHEN p.jenis_kelompok_jabatan = 'JF Dosen' AND p.jenis_asn = 'PPPK' THEN 'PPPK'
	    WHEN p.jenis_kelompok_jabatan = 'JF Guru' AND p.jenis_asn = 'PPPK' THEN 'PPPK'
	    WHEN p.jenis_kelompok_jabatan = 'JF Kesehatan' AND p.jenis_asn = 'PPPK' THEN 'PPPK'
	    WHEN p.jenis_kelompok_jabatan = 'JF Teknis' AND p.jenis_asn = 'PPPK' THEN 'PPPK'
	    WHEN p.jenis_kelompok_jabatan = 'JF Dosen' AND p.jenis_asn = 'PPPK Paruh Waktu' THEN 'PPPK Paruh Waktu'
	    WHEN p.jenis_kelompok_jabatan = 'JF Guru' AND p.jenis_asn = 'PPPK Paruh Waktu' THEN 'PPPK Paruh Waktu'
	    WHEN p.jenis_kelompok_jabatan = 'JF Kesehatan' AND p.jenis_asn = 'PPPK Paruh Waktu' THEN 'PPPK Paruh Waktu'
	    WHEN p.jenis_kelompok_jabatan = 'JF Teknis' AND p.jenis_asn = 'PPPK Paruh Waktu' THEN 'PPPK Paruh Waktu'
	    WHEN p.jenis_kelompok_jabatan ILIKE '%pelaksana%' AND p.jenis_asn = 'PNS' THEN 'PNS'
	    WHEN p.jenis_kelompok_jabatan ILIKE '%pelaksana%' AND p.jenis_asn = 'PPPK' THEN 'PPPK'
	    WHEN p.jenis_kelompok_jabatan ILIKE '%pelaksana%' AND p.jenis_asn = 'PPPK Paruh Waktu' THEN 'PPPK Paruh Waktu'
	    ELSE p.jenis_kelompok_jabatan
    END AS jabatan,
    COUNT(*)
    FROM
    {table_name} p
    where p.lokasi_kerja_clean ilike '{{cepat_kode}}%'
    --and p.jenis_instansi_kerja = 'D' 
    --and (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92'))
    and p.status_instansi_kerja = 'A'
    group by jabatan,kelompok_jabatan
    """
}

#Kanreg
def get_kanreg_prefix(conn, kanreg_id):
    query = f"""SELECT id, nama 
            FROM ref.kanreg WHERE
            id = '{kanreg_id}'"""
    df = pd.read_sql_query(query, conn)
    return df.to_dict(orient='records')

queries_kanreg = {
    "Jenis_ASN":
    f"""SELECT p.jenis_asn, count(*) 
    from {table_name} p
	  WHERE p.status_instansi_kerja = 'A' AND p.id_kanreg_instansi_kerja = '{{cepat_kode}}' AND p.jenis_instansi_kerja = 'D'
    group by p.jenis_asn
    """,
    "Jenis_Kelamin":
    f"""select p.jenis_kelamin , count(*) 
    from {table_name} p
	  WHERE p.status_instansi_kerja = 'A' AND p.id_kanreg_instansi_kerja = '{{cepat_kode}}' AND p.jenis_instansi_kerja = 'D'
    group by p.jenis_kelamin""",
    "Pendidikan":
    f"""select tingkatpendidikan,
    b.count from (
    select tingkatpendidikan,
        case tingkatpendidikan
        when 'SD-SMA' then 1
        when 'DI-DIII' then 2
        when 'DIV/S1' then 3
        when 'S2' then 4
        when 'S3' then 5
        end as urutan,
    a.count
    from (
    select 
        case 
	    when p.tingkat_pendidikan in ('Diploma I','Diploma II') or p.tingkat_pendidikan ilike '%Diploma III%' then 'DI-DIII'
	    when p.tingkat_pendidikan ilike '%diploma%IV%' or p.tingkat_pendidikan ilike '%S-1%' or p.tingkat_pendidikan = 'Profesi' then 'DIV/S1'
	    when p.tingkat_pendidikan ilike '%s%2%' or p.tingkat_pendidikan = 'Spesialis' then 'S2'
	    when p.tingkat_pendidikan ilike '%s%3%' or p.tingkat_pendidikan = 'Subspesialis' then 'S3'
	    when p.tingkat_pendidikan IN ('Sekolah Dasar','SLTP','SLTP Kejuruan','SLTA','SLTA Kejuruan','SLTA Keguruan') THEN 'SD-SMA'
        else p.tingkat_pendidikan
        end as tingkatpendidikan, 
    count(*) from {table_name} p
	  WHERE p.status_instansi_kerja = 'A' AND p.id_kanreg_instansi_kerja = '{{cepat_kode}}' AND p.jenis_instansi_kerja = 'D'
    group by tingkatpendidikan 
    )a
    )b
    order by b.urutan""",
    "Kelompok_Generasi":
    f"""select p.kelompok_generasi  , count(*) from {table_name} p
	  WHERE p.status_instansi_kerja = 'A' AND p.id_kanreg_instansi_kerja = '{{cepat_kode}}' AND p.jenis_instansi_kerja = 'D'
    group by p.kelompok_generasi""",
    "Jenis_Jabatan":
    f"""SELECT 
    CASE
	    WHEN p.jenis_kelompok_jabatan IN ('JPT Madya','JPT Pratama','JPT Utama','Administrator','Pengawas','Eselon V') THEN 'Struktural'
	    WHEN p.jenis_kelompok_jabatan = 'JF Dosen' THEN 'JF Dosen'
	    WHEN p.jenis_kelompok_jabatan = 'JF Guru' THEN 'JF Guru'
	    WHEN p.jenis_kelompok_jabatan = 'JF Kesehatan' THEN 'JF Kesehatan'
	    WHEN p.jenis_kelompok_jabatan = 'JF Teknis' THEN 'JF Teknis'
	    WHEN p.jenis_kelompok_jabatan ILIKE '%pelaksana%' THEN 'Pelaksana'
    END AS kelompok_jabatan,
    CASE
      WHEN p.jenis_kelompok_jabatan = 'JPT Utama' AND p.jenis_asn = 'PNS' THEN 'PNS JPT Utama'
	    WHEN p.jenis_kelompok_jabatan = 'JPT Utama' AND p.jenis_asn = 'PPPK' THEN 'PPPK JPT Utama'
	    WHEN p.jenis_kelompok_jabatan = 'JPT Madya' AND p.jenis_asn = 'PNS' THEN 'PNS JPT Madya'
	    WHEN p.jenis_kelompok_jabatan = 'JPT Madya' AND p.jenis_asn = 'PPPK' THEN 'PPPK JPT Madya'
	    WHEN p.jenis_kelompok_jabatan = 'JPT Pratama' AND p.jenis_asn = 'PNS' THEN 'PNS JPT Pratama'
	    WHEN p.jenis_kelompok_jabatan = 'JPT Pratama' AND p.jenis_asn = 'PPPK' THEN 'PNS JPT Pratama'
	    WHEN p.jenis_kelompok_jabatan = 'JF Dosen' AND p.jenis_asn = 'PNS' THEN 'PNS'
	    WHEN p.jenis_kelompok_jabatan = 'JF Guru' AND p.jenis_asn = 'PNS' THEN 'PNS'
	    WHEN p.jenis_kelompok_jabatan = 'JF Kesehatan' AND p.jenis_asn = 'PNS' THEN 'PNS'
	    WHEN p.jenis_kelompok_jabatan = 'JF Teknis' AND p.jenis_asn = 'PNS' THEN 'PNS'
	    WHEN p.jenis_kelompok_jabatan = 'JF Dosen' AND p.jenis_asn = 'PPPK' THEN 'PPPK'
	    WHEN p.jenis_kelompok_jabatan = 'JF Guru' AND p.jenis_asn = 'PPPK' THEN 'PPPK'
	    WHEN p.jenis_kelompok_jabatan = 'JF Kesehatan' AND p.jenis_asn = 'PPPK' THEN 'PPPK'
	    WHEN p.jenis_kelompok_jabatan = 'JF Teknis' AND p.jenis_asn = 'PPPK' THEN 'PPPK'
	    WHEN p.jenis_kelompok_jabatan = 'JF Dosen' AND p.jenis_asn = 'PPPK Paruh Waktu' THEN 'PPPK Paruh Waktu'
	    WHEN p.jenis_kelompok_jabatan = 'JF Guru' AND p.jenis_asn = 'PPPK Paruh Waktu' THEN 'PPPK Paruh Waktu'
	    WHEN p.jenis_kelompok_jabatan = 'JF Kesehatan' AND p.jenis_asn = 'PPPK Paruh Waktu' THEN 'PPPK Paruh Waktu'
	    WHEN p.jenis_kelompok_jabatan = 'JF Teknis' AND p.jenis_asn = 'PPPK Paruh Waktu' THEN 'PPPK Paruh Waktu'
	    WHEN p.jenis_kelompok_jabatan ILIKE '%pelaksana%' AND p.jenis_asn = 'PNS' THEN 'PNS'
	    WHEN p.jenis_kelompok_jabatan ILIKE '%pelaksana%' AND p.jenis_asn = 'PPPK' THEN 'PPPK'
	    WHEN p.jenis_kelompok_jabatan ILIKE '%pelaksana%' AND p.jenis_asn = 'PPPK Paruh Waktu' THEN 'PPPK Paruh Waktu'
	    ELSE p.jenis_kelompok_jabatan
    END AS jabatan,
    COUNT(*)
    from {table_name} p
	  WHERE p.status_instansi_kerja = 'A' AND p.id_kanreg_instansi_kerja = '{{cepat_kode}}' AND p.jenis_instansi_kerja = 'D'
    group by jabatan,kelompok_jabatan
    """
}

#NASIONAL
queries_nasional = {
    "Jenis_ASN":
    f"""select p.jenis_asn, count(*) from {table_name} p 
    where (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92','101')) 
    and p.status_instansi_kerja = 'A'
    GROUP BY p.jenis_asn""",
    "Jenis_Instansi":
    f"""select p.jenis_instansi_kerja as jenis_instansi, count(*) from {table_name} p
    where (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92','101'))
    and p.status_instansi_kerja = 'A'
    GROUP BY p.jenis_instansi_kerja""",
    "Jenis_Kelamin":
    f"""select p.jenis_kelamin, count(*) from {table_name} p
    where (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92','101'))
    and p.status_instansi_kerja = 'A'
    GROUP BY p.jenis_kelamin""",
    "Kelompok_Generasi":
    f"""select p.kelompok_generasi, count(*) from {table_name} p
    where (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92','101'))
    and p.status_instansi_kerja = 'A'
    GROUP BY p.kelompok_generasi""",
    "Pendidikan":
    f"""select tingkatpendidikan,
    b.count from (
    select tingkatpendidikan,
        case tingkatpendidikan
        when 'SD-SMA' then 1
        when 'DI-DIII' then 2
        when 'DIV/S1' then 3
        when 'S2' then 4
        when 'S3' then 5
        end as urutan,
    a.count
    from (
    select 
        case 
	    when p.tingkat_pendidikan in ('Diploma I','Diploma II') or p.tingkat_pendidikan ilike '%Diploma III%' then 'DI-DIII'
	    when p.tingkat_pendidikan ilike '%diploma%IV%' or p.tingkat_pendidikan ilike '%S-1%' or p.tingkat_pendidikan = 'Profesi' then 'DIV/S1'
	    when p.tingkat_pendidikan ilike '%s%2%' or p.tingkat_pendidikan = 'Spesialis' then 'S2'
	    when p.tingkat_pendidikan ilike '%s%3%' or p.tingkat_pendidikan = 'Subspesialis' then 'S3'
	    when p.tingkat_pendidikan IN ('Sekolah Dasar','SLTP','SLTP Kejuruan','SLTA','SLTA Kejuruan','SLTA Keguruan') THEN 'SD-SMA'
        else p.tingkat_pendidikan
        end as tingkatpendidikan, 
    count(*) from {table_name} p
    join ref.instansi i on p.instansi_kerja_id = i.id
    where (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92','101'))
    and p.status_instansi_kerja = 'A'
    group by tingkatpendidikan 
    )a
    )b
    order by b.urutan""",
    "Jenis_Jabatan":
    f"""SELECT 
    CASE
	    WHEN p.jenis_kelompok_jabatan IN ('JPT Madya','JPT Pratama','JPT Utama','Administrator','Pengawas','Eselon V') THEN 'Struktural'
	    WHEN p.jenis_kelompok_jabatan = 'JF Dosen' THEN 'JF Dosen'
	    WHEN p.jenis_kelompok_jabatan = 'JF Guru' THEN 'JF Guru'
	    WHEN p.jenis_kelompok_jabatan = 'JF Kesehatan' THEN 'JF Kesehatan'
	    WHEN p.jenis_kelompok_jabatan = 'JF Teknis' THEN 'JF Teknis'
	    WHEN p.jenis_kelompok_jabatan ILIKE '%pelaksana%' THEN 'Pelaksana'
    END AS kelompok_jabatan,
    CASE
      WHEN p.jenis_kelompok_jabatan = 'JPT Utama' AND p.jenis_asn = 'PNS' THEN 'PNS JPT Utama'
	    WHEN p.jenis_kelompok_jabatan = 'JPT Utama' AND p.jenis_asn = 'PPPK' THEN 'PPPK JPT Utama'
	    WHEN p.jenis_kelompok_jabatan = 'JPT Madya' AND p.jenis_asn = 'PNS' THEN 'PNS JPT Madya'
	    WHEN p.jenis_kelompok_jabatan = 'JPT Madya' AND p.jenis_asn = 'PPPK' THEN 'PPPK JPT Madya'
	    WHEN p.jenis_kelompok_jabatan = 'JPT Pratama' AND p.jenis_asn = 'PNS' THEN 'PNS JPT Pratama'
	    WHEN p.jenis_kelompok_jabatan = 'JPT Pratama' AND p.jenis_asn = 'PPPK' THEN 'PNS JPT Pratama'
	    WHEN p.jenis_kelompok_jabatan = 'JF Dosen' AND p.jenis_asn = 'PNS' THEN 'PNS'
	    WHEN p.jenis_kelompok_jabatan = 'JF Guru' AND p.jenis_asn = 'PNS' THEN 'PNS'
	    WHEN p.jenis_kelompok_jabatan = 'JF Kesehatan' AND p.jenis_asn = 'PNS' THEN 'PNS'
	    WHEN p.jenis_kelompok_jabatan = 'JF Teknis' AND p.jenis_asn = 'PNS' THEN 'PNS'
	    WHEN p.jenis_kelompok_jabatan = 'JF Dosen' AND p.jenis_asn = 'PPPK' THEN 'PPPK'
	    WHEN p.jenis_kelompok_jabatan = 'JF Guru' AND p.jenis_asn = 'PPPK' THEN 'PPPK'
	    WHEN p.jenis_kelompok_jabatan = 'JF Kesehatan' AND p.jenis_asn = 'PPPK' THEN 'PPPK'
	    WHEN p.jenis_kelompok_jabatan = 'JF Teknis' AND p.jenis_asn = 'PPPK' THEN 'PPPK'
	    WHEN p.jenis_kelompok_jabatan = 'JF Dosen' AND p.jenis_asn = 'PPPK Paruh Waktu' THEN 'PPPK Paruh Waktu'
	    WHEN p.jenis_kelompok_jabatan = 'JF Guru' AND p.jenis_asn = 'PPPK Paruh Waktu' THEN 'PPPK Paruh Waktu'
	    WHEN p.jenis_kelompok_jabatan = 'JF Kesehatan' AND p.jenis_asn = 'PPPK Paruh Waktu' THEN 'PPPK Paruh Waktu'
	    WHEN p.jenis_kelompok_jabatan = 'JF Teknis' AND p.jenis_asn = 'PPPK Paruh Waktu' THEN 'PPPK Paruh Waktu'
	    WHEN p.jenis_kelompok_jabatan ILIKE '%pelaksana%' AND p.jenis_asn = 'PNS' THEN 'PNS'
	    WHEN p.jenis_kelompok_jabatan ILIKE '%pelaksana%' AND p.jenis_asn = 'PPPK' THEN 'PPPK'
	    WHEN p.jenis_kelompok_jabatan ILIKE '%pelaksana%' AND p.jenis_asn = 'PPPK Paruh Waktu' THEN 'PPPK Paruh Waktu'
	    ELSE p.jenis_kelompok_jabatan
    END AS jabatan,
    COUNT(*)
    from {table_name} p
    left join ref.jabatan_fungsional jf on p.jabatan_fungsional_id = jf.id
    where
    (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92','101'))
    and p.status_instansi_kerja = 'A'
    group by kelompok_jabatan, jabatan
    """
}