import pandas as pd
from dataconfig.data import get_table_name

#Cepat Kode Provinsi
def get_provinsi_list(conn):
    query = """SELECT cepat_kode, nama 
            FROM ref.instansi WHERE
            nama ILIKE '%sumatera selatan%'"""
    return pd.read_sql_query(query, conn).to_dict(orient='records')

#Query Infografis
table_name = get_table_name()
queries = {
    "Jenis_ASN":
    f"""SELECT p.jenis_asn, count(*) 
    from {table_name} p
    where p.cepat_kode_instansikerja = '{{cepat_kode}}'
    --and p.jenis_insker = 'D' 
    and (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92'))
    and p.status_instansikerja = 'A'
    group by p.jenis_asn
    """,
    "Jenis_Kelamin":
    f"""select p.jenis_kelamin , count(*) 
    from {table_name} p
    where p.cepat_kode_instansikerja = '{{cepat_kode}}'
    --and p.jenis_insker = 'D' 
    and (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92'))
    and p.status_instansikerja = 'A'
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
	    when p.tkpendidikan in ('Diploma I','Diploma II') or p.tkpendidikan ilike '%Diploma III%' then 'DI-DIII'
	    when p.tkpendidikan ilike '%diploma%IV%' or p.tkpendidikan ilike '%S-1%' or p.tkpendidikan = 'Profesi' then 'DIV/S1'
	    when p.tkpendidikan ilike '%s%2%' or p.tkpendidikan = 'Spesialis' then 'S2'
	    when p.tkpendidikan ilike '%s%3%' or p.tkpendidikan = 'Subspesialis' then 'S3'
	    else 'SD-SMA'
        end as tingkatpendidikan, 
    count(*) from {table_name} p
    join ref.instansi i on p.instansi_kerja_id = i.id
    where p.cepat_kode_instansikerja = '{{cepat_kode}}'
    group by tingkatpendidikan 
    )a
    )b
order by b.urutan""",
    "Masa_Kerja":
    f"""select kelompok_masa_kerja, count from (
    SELECT kelompok_masa_kerja,
    count(*),
    CASE kelompok_masa_kerja
	WHEN ' 0 -  5' THEN 1
	WHEN ' 6 - 10' THEN 2
	WHEN '11 - 15' THEN 3
	WHEN '16 - 20' THEN 4
	WHEN '21 - 25' THEN 5
	WHEN '26 - 30' THEN 6
	WHEN '> 30' THEN 7
    END AS urutan
    FROM {table_name} p 
    WHERE  
    p.cepat_kode_instansikerja = '{{cepat_kode}}'
    --and p.jenis_insker = 'D' 
    and (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92'))
    and p.status_instansikerja = 'A'
    GROUP BY p.kelompok_masa_kerja)a
    order by a.urutan""",
    "Kelompok_Usia":
    f"""select p.kelompok_usia  , count(*) from {table_name} p
    where p.cepat_kode_instansikerja = '{{cepat_kode}}'
    --and p.jenis_insker = 'D' 
    and (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92'))
    and p.status_instansikerja = 'A'
    group by p.kelompok_usia""",
    "Jenis_Jabatan":
    f"""SELECT
  CASE
    a.jenisjabatannew
    WHEN 'JPT Utama' THEN
      'PNS JPT Utama'
    WHEN 'JPT Madya' THEN
      'PNS JPT Madya'
    WHEN 'JPT Pratama' THEN
      'PNS JPT Pratama'
    WHEN 'JF Dosen' THEN
      'PNS JF Dosen'
    WHEN 'JF Guru' THEN
      'PNS JF Guru'
    WHEN 'JF Medis' THEN
      'PNS JF Medis'
    WHEN 'JF Teknis' THEN
      'PNS JF Teknis'
    WHEN 'PPPK Dosen' THEN
      'PPPK JF Dosen'
    WHEN 'PPPK Guru' THEN
      'PPPK JF Guru'
    WHEN 'PPPK Kesehatan' THEN
      'PPPK JF Medis'
    WHEN 'PPPK Teknis' THEN
      'PPPK JF Teknis'
    ELSE
      a.jenisjabatannew
  END AS jenisjabatan,
  count
FROM
(
    SELECT
    CASE
	WHEN p.jenis_asn = 'PNS' THEN p.jenis_kelompok_jabatan
    WHEN p.jenis_kelompok_jabatan in ('PPPK Tendik','PPPK Penyuluh Pertanian') THEN 'PPPK Teknis'
	WHEN (p.jenis_jabatan_id='2' AND jf.id IS NOT NULL) OR p.jenis_kelompok_jabatan LIKE '%JPT%' THEN p.jenis_kelompok_jabatan
	ELSE 'PPPK Pelaksana'
    end jenisjabatannew, count(*)
    from {table_name} p
    left join ref.jabatan_fungsional jf on p.jabatan_fungsional_id = jf.id
    where p.cepat_kode_instansikerja = '{{cepat_kode}}'
    --and p.jenis_insker = 'D' 
    and (p.kedudukan_hukum_id <= '51' or p.kedudukan_hukum_id in ('71','73','92'))
    and p.status_instansikerja = 'A'
    group by jenisjabatannew
    )a"""
}
