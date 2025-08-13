from pptx.util import Pt, Inches
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE 
from pptx.enum.text import PP_ALIGN
import pandas as pd
from dataconfig.data import tambah_persentase, get_tanggal_data
from dataconfig.mapping import mapping_diagram_cm, mapping_textbox_cm, TABLE_MAPPING

#fungsi untuk mengganti teks pada shape dengan mempertahankan gaya
def replace_text_reserving_style(shape, placeholder, replacement):
    if not shape.has_text_frame:
        return
    for paragraph in shape.text_frame.paragraphs:
        full_text = ''.join([run.text for run in paragraph.runs])
        if placeholder not in full_text:
                continue
        replaced_text = full_text.replace(placeholder, replacement)
        for run in paragraph.runs:
                run.text = ''
                if paragraph.runs:
                     paragraph.runs[0].text = replaced_text

def generate_instansi_values(prov):
     return{
          "{instansi_1}": prov,
          "{tanggal_data}": get_tanggal_data()
     }

#fungsi untuk mengisi slide dengan data jenis ASN
def isi_infografis(prs, df_kategori, mapping_placeholder, mapping_instansi, label_column='label'):
    slide = prs.slides[0]
    for shape in slide.shapes:
        if not shape.has_text_frame:
            continue
        for placeholder, replacement in mapping_instansi.items():
             replace_text_reserving_style(shape, placeholder, replacement)
        text = shape.text
        for idx, row in df_kategori.iterrows():
            label = row.get(label_column)
            for kolom_data, map_label in mapping_placeholder.items():
                if label in map_label:
                    placeholder = map_label[label]
                    nilai = row.get(kolom_data)
                    nilai_str = f"{nilai:,}".replace(",",".") if isinstance(nilai, (int)) else str(nilai)
                    replace_text_reserving_style(shape, placeholder, nilai_str)
                    #if placeholder in text:
                        #shape.text = text.replace(placeholder, nilai_str)

#konversi cm ke inches
def cm(val):
    return Inches(val / 2.54)

#Fungsi Balok Pendidikan
def isi_balok_pendidikan(df,slide):
    max_val = df['persentase_vis_num'].max()
    max_height = cm(2)

    for _, row in df.iterrows():
         label = row['tingkatpendidikan']
         count = row['count']
         persen_vis = row['persentase_vis_num']
         if label in mapping_diagram_cm:
            pos = mapping_diagram_cm[label]
            base_y = cm(pos['y'])
            tinggi = (persen_vis / max_val) * max_height
            if tinggi > base_y:
                 tinggi = base_y - cm(0.1)  # mengurangi sedikit agar tidak melebihi batas
            y_top = base_y - tinggi
        # Balok Diagram
            shape = slide.shapes.add_shape(
                MSO_SHAPE.RECTANGLE,
                cm(pos['x']), y_top,
                cm(pos['width']), tinggi
            )
            shape.fill.solid()
            shape.fill.fore_color.rgb = pos['color']
            shape.line.fill.background()  # hilangkan border
        # Textbox Nilai di Atas Balok
            base_y = cm(pos['y'])
            text_pos = mapping_textbox_cm[label]
            textbox = slide.shapes.add_textbox(
                cm(text_pos['x']),
                base_y - tinggi - cm(text_pos['y_offset']),
                cm(text_pos['width']),
                cm(1.0)
            )
            tf = textbox.text_frame
            tf.text = f"{persen_vis:.0f}%\n{count:,}".replace(",",".")
            tf.paragraphs[0].alignment = PP_ALIGN.CENTER
            tf.paragraphs[1].alignment = PP_ALIGN.CENTER
            #baris persentase
            run0 = tf.paragraphs[0].runs[0]
            font0 = run0.font
            font0.size = Pt(12)
            font0.bold = True
            font0.color.rgb = RGBColor(31,78,121)
            #baris count
            run1 = tf.paragraphs[1].runs[0]
            font1 = run1.font
            font1.size = Pt(11)
            font1.color.rgb = RGBColor(37,156,215)

def isi_table_count(slide, df, mapping_placeholder, label_column, table_name_count, font_size_count=10):
    #Merubah jadi List Mapping
    table_name = table_name_count if isinstance(table_name_count, list) else [table_name_count]
    expected_labels = set(mapping_placeholder.get("count", {}).keys())
    existing_labels = set(df[label_column].unique())
    missing_labels = expected_labels - existing_labels
    if missing_labels:
        df_missing = pd.DataFrame({
            label_column: list(missing_labels),
            'count': [0] * len(missing_labels)
        })
        df = pd.concat([df, df_missing], ignore_index=True)  
            # Isi count ke table_count
    for table_name in table_name:
        table_count = next((s.table for s in slide.shapes if s.has_table and s.name == table_name), None)
        if not table_count:
            raise ValueError(f"Tabel '{table_name}' tidak ditemukan di slide.")
        for row in table_count.rows:
            for col_idx, cell in enumerate(row.cells):
                text = cell.text_frame.text
                for label in expected_labels:
                    count_ph = mapping_placeholder.get("count", {}).get(label)
                    if count_ph and count_ph in text:
                        count_val = df[df[label_column] == label].iloc[0]['count']
                        text = text.replace(count_ph, f"{count_val:,}".replace(",","."))
                cell.text_frame.text = text
                if col_idx == 0:
                    for paragraph in cell.text_frame.paragraphs:
                        for run in paragraph.runs:
                            font = run.font
                            font.size = font_size_count
                if col_idx == 1:
                    for paragraph in cell.text_frame.paragraphs:
                        for run in paragraph.runs:
                            font = run.font
                            font.size = font_size_count
                        paragraph.alignment = PP_ALIGN.RIGHT

def isi_table_persen(slide, df, mapping_placeholder, label_column, table_name_persen, font_size_persen=10):
    if "persentase_vis" not in mapping_placeholder:
        return
    #Cari Table Persen
    table_persen = next((s.table for s in slide.shapes if s.has_table and s.name == table_name_persen), None)
    if not table_persen:
        return
    expected_labels = set(mapping_placeholder.get("persentase_vis", {}).keys())
    existing_labels = set(df[label_column].unique())
    missing_labels = expected_labels - existing_labels
    # Tambahkan label yang hilang
    if missing_labels:
        df_missing = pd.DataFrame({
            label_column: list(missing_labels),
            'persentase_vis': [0] * len(missing_labels)
        })
        df_missing["persentase_vis"] = df_missing["persentase_vis"].astype(int)
        df = pd.concat([df, df_missing], ignore_index=True)
    df = tambah_persentase(df)
    # Isi persentase ke table_persen
    for row in table_persen.rows:
        for cell in row.cells:
            text = cell.text_frame.text
            for label in expected_labels:
                persen_ph = mapping_placeholder.get("persentase_vis", {}).get(label)
                if persen_ph and persen_ph in text:
                    persen_val = df[df[label_column] == label].iloc[0]['persentase_vis']
                    text = text.replace(persen_ph, persen_val)
            cell.text_frame.text = text
            for paragraph in cell.text_frame.paragraphs:
                for run in paragraph.runs:
                    font = run.font
                    font.size = font_size_persen
                    font.color.rgb = RGBColor(31, 78, 121)
                    font.bold = True
                paragraph.alignment = PP_ALIGN.RIGHT


def isi_dua_table_kategori(slide, df, mapping_placeholder, kategori, label_column):
    if kategori not in TABLE_MAPPING:
        raise ValueError(f"Kategori '{kategori}' belum ada di TABLE_MAPPING")
    table_name_count = TABLE_MAPPING[kategori]['count']
    table_name_persen = None
    if 'persentase_vis' in TABLE_MAPPING[kategori]:
        table_name_persen = TABLE_MAPPING[kategori]['persentase_vis']
    font_size = Pt(TABLE_MAPPING[kategori].get('font_size', 10))
    isi_table_count(
        slide,
        df,
        mapping_placeholder,
        label_column=label_column,
        table_name_count=table_name_count,
        font_size_count=font_size
    )
    if table_name_persen and 'persentase_vis' in mapping_placeholder:
        isi_table_persen(
            slide,
            df,
            mapping_placeholder,
            label_column=label_column,
            table_name_persen=table_name_persen,
            font_size_persen=font_size
        )

