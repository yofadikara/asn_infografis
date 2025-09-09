from dataconfig.data import get_all_data, get_table_name, tambah_persentase, klasifikasi_kelompok_jabatan, ringkasan_kelompok_jabatan
from dataconfig.db_config import connect_db, load_env
from automation.export_excel import export_per_provinsi
from automation.export_ppt import isi_infografis, generate_instansi_values, isi_balok_pendidikan, generate_all_tables
from pptx import Presentation
import pandas as pd
from dataconfig.mapping import mapping_placeholder_per_kategori, label_column_per_kategori, selid_kategori_shared
from io import BytesIO
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload
from template.query_templates import get_provinsi_list
import os
from automation.filter import get_instansi_filter, resolve_filter

#Tarik Data
params = load_env()
conn = connect_db(params)
args = get_instansi_filter()
#untuk mengambil prefix wilker
filter_value = resolve_filter(args, conn)
#kondisi mode instansi atau wilker
if args.instansi:
    mode = 'instansi'
    target_list = get_provinsi_list(conn, filter_value)
elif args.wilker:
    mode = 'wilker'
    target_list = filter_value
else:
    raise ValueError("Mode harus 'instansi' atau 'wilker'")
data_dict = get_all_data(conn, get_table_name(), target_list, mode=mode)
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
                '''print(f"Memproses isi_infografis untuk kategori: {kategori}")'''
                isi_infografis(prs, data_export, mapping_placeholder, mapping_instansi, label_column= label_column)
            else:
                print(f"Data Kosong untuk Provinsi: {prov}, Kategori: {kategori}")
        
    #Save PPT
    output_path = f"output/ppt/{prov}.pptx"
    prs.save(output_path)
    print(f"PowerPoint Disimpan: {output_path}")
    
    #Upload Drive
    '''SCOPES = ['https://www.googleapis.com/auth/drive.file']
    TOKEN_FILE = 'token.json'
    CREDENTIALS_FILE = 'credentials.json'
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
        creds = flow.run_local_server(port=0)
        with open(TOKEN_FILE, 'w') as token:
            token.write(creds.to_json())
    drive_service = build('drive', 'v3', credentials=creds)
    #save to bytes sementara
    ppt_stream = BytesIO()
    prs.save(ppt_stream)
    ppt_stream.seek(0)
    #Upload
    file_metadata = {
        'name': f'{prov}.pptx',
        'parents': ['1OhAKH94lYQwZVAarrz1nlWW86X3aBKJv']
    }
    media = MediaIoBaseUpload(ppt_stream, mimetype='application/vnd.openxmlformats-officedocument.presentationml.presentation',
                              resumable=True)
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"File {prov}.pptx diunggah ke Google Drive dengan ID: {file.get('id')}")
'''
    '''#Export ke Excel
    if data_dict and any(data_dict.values()):
        export_per_provinsi(data_dict)
    else:
        print("Tidak ada data yang tersedia untuk diekspor.")'''