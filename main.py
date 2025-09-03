from dataconfig.data import get_all_data, get_table_name, tambah_persentase, klasifikasi_kelompok_jabatan, ringkasan_kelompok_jabatan
from dataconfig.db_config import connect_db, load_env
from automation.export_excel import export_per_provinsi
from automation.export_ppt import isi_infografis, generate_instansi_values, isi_balok_pendidikan, generate_all_tables
from pptx import Presentation
import pandas as pd
from dataconfig.mapping import mapping_placeholder_per_kategori, label_column_per_kategori, selid_kategori_shared


#Tarik Data
params = load_env()
conn = connect_db(params)
data_dict = get_all_data(conn, get_table_name())
for prov, kategori_data in data_dict.items():
    prs = Presentation('template/template_infografis.pptx')
    print(f"Data untuk Provinsi: {prov}")
    kategori_items = list(kategori_data.items()) #untuk mengindari runtime error saat iterasi
    for kategori, df in kategori_items:
        if 'count' in df.columns:
            #penambahan kolom TOTAL pada jenis ASN
            if 'jenis_asn' in df.columns and 'TOTAL' not in df['jenis_asn'].values:
                df_total = pd.DataFrame({
                    'jenis_asn': ['TOTAL'],
                    'count': [df['count'].sum()]
                })
                df = pd.concat([df, df_total], ignore_index=True)
                df_clean = df[df['jenis_asn'] != 'TOTAL'].copy()
                df_clean = tambah_persentase(df_clean) #tambah persentase
                df_final = pd.concat([
                    df_clean,
                    df[df['jenis_asn'] == 'TOTAL']
                ], ignore_index=True)
                data_dict[prov][kategori] = df_final
            #penambahan ringkasan kelompok jabatan        
            elif 'jenisjabatan' in df.columns and 'count' in df.columns:
                df = klasifikasi_kelompok_jabatan(df)
                #data_dict[prov][kategori] = tambah_persentase(df) 
                df_ringkasan = ringkasan_kelompok_jabatan(df)
                data_dict[prov][f"Ringkasan_{kategori}"] = df_ringkasan
            else:
                data_dict[prov][kategori] = tambah_persentase(df)
    #table dinamis
    generate_all_tables(prs, data_dict[prov])
    #add ulang kategori            
    kategori_items = list(kategori_data.items())
    for kategori, df in kategori_items:
        '''if kategori in TABLE_MAPPING:
            slide_index = selid_kategori_shared.get(kategori)
            slide = prs.slides[slide_index]
            mapping_placeholder = mapping_placeholder_per_kategori[kategori]
            label_column = label_column_per_kategori.get(kategori, "label")
            data_export = data_dict[prov][kategori]
            isi_dua_table_kategori(slide, data_export, mapping_placeholder, kategori, label_column=label_column)'''
        if kategori == "Pendidikan":
            slide_index = selid_kategori_shared.get(kategori)
            slide = prs.slides[slide_index]
            df_export = data_dict[prov][kategori]
            isi_balok_pendidikan(df_export, slide)
        #Isi Data PPT
        if kategori in mapping_placeholder_per_kategori:
            mapping_placeholder = mapping_placeholder_per_kategori[kategori]
            label_column = label_column_per_kategori.get(kategori, "label")
            #untuk nama instansi dinamis di slide                    
            mapping_instansi = generate_instansi_values(prov)
            data_export = data_dict[prov][kategori]
            if data_export is not None:
                print(f"Memproses isi_infografis untuk kategori: {kategori}")
                isi_infografis(prs, data_export, mapping_placeholder, mapping_instansi, label_column= label_column)
            else:
                print(f"Data Kosong untuk Provinsi: {prov}, Kategori: {kategori}")
        

    #Save PPT
    output_path = f"output/ppt/{prov}.pptx"
    prs.save(output_path)
    print(f"PowerPoint Disimpan: {output_path}")
    
    #Export ke Excel
    '''if data_dict and any(data_dict.values()):
        export_per_provinsi(data_dict)
    else:
        print("Tidak ada data yang tersedia untuk diekspor.")'''