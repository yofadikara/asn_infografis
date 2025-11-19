import pandas as pd
from pathlib import Path
import os

def export_per_provinsi(data_dict, output_dir= 'output/excel'):
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    for provinsi, kategori_dict in data_dict.items():
        file_path = os.path.join(output_dir, f"{provinsi}.xlsx")
        with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
            for kategori, df in kategori_dict.items():
                sheet_name = kategori[:31]  # Excel sheet name max 31 chars
                df.to_excel(writer, sheet_name=sheet_name, index=False)
        print(f"Excel Disimpan: {file_path}")

def export_nasional(data_dict, output_dir= 'output/excel'):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    file_path = os.path.join(output_dir, "Nasional.xlsx")
    with pd.ExcelWriter(file_path, engine='xlsxwriter') as writer:
        for kategori, subkategori_dict in data_dict.items():
                for subkategori ,df in subkategori_dict.items():
                    sheet_name = f"{kategori}_{subkategori}"[:31]  # Excel sheet name max 31 chars
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
        print(f"Excel Disimpan: {file_path}")

