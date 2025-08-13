from pptx.dml.color import RGBColor

#mappingan
label_column_per_kategori = {
    "Jenis_ASN": "jenis_asn",
    "Jenis_Kelamin": "jenis_kelamin",
    "Masa_Kerja": "kelompok_masa_kerja",
    "Kelompok_Usia": "kelompok_usia",
    "Ringkasan_Jenis_Jabatan": "kelompok_jabatan",
    "Jenis_Jabatan": "jenisjabatannew"
}

#mapping ke key ppt
mapping_placeholder_per_kategori = {
    "Jenis_ASN":{
    "count": {
        "PNS": "{count_pns}",
        "PPPK": "{count_pppk}",
        "TOTAL": "{total_jenis_asn}"
    },
    "persentase_vis": {
        "PNS": "{persentase_vis_pns}",
        "PPPK": "{persentase_vis_pppk}",
    }
    },
    "Jenis_Kelamin": {
    "count": {
        "PRIA": "{count_pria}",
        "WANITA": "{count_wanita}"
    },
    "persentase_vis": {
        "PRIA": "{persentase_vis_pria}",
        "WANITA": "{persentase_vis_wanita}"
    }
    },
    "Masa_Kerja": {
        "count": {
            " 0 -  5": "{count_0_5}",
            " 6 - 10": "{count_6_10}",
            "11 - 15": "{count_11_15}",
            "16 - 20": "{count_16_20}",
            "21 - 25": "{count_21_25}",
            "26 - 30": "{count_26_30}",
            "> 30": "{count_30}"
        },
        "persentase_vis": {
            " 0 -  5": "{persentase_vis_0_5}",
            " 6 - 10": "{persentase_vis_6_10}",
            "11 - 15": "{persentase_vis_11_15}",
            "16 - 20": "{persentase_vis_16_20}",
            "21 - 25": "{persentase_vis_21_25}",
            "26 - 30": "{persentase_vis_26_30}",
            "> 30": "{persentase_vis_30}"
        }
    },
    "Kelompok_Usia": {
        "count": {
            "18 - 20": "{count_18_20}",
            "21 - 30": "{count_21_30}",
            "31 - 40": "{count_31_40}",
            "41 - 50": "{count_41_50}",
            "51 - 60": "{count_51_60}",
            "diatas 60": "{count_60}"
        },
        "persentase_vis": {
            "18 - 20": "{persentase_vis_18}",
            "21 - 30": "{persentase_vis_21}",
            "31 - 40": "{persentase_vis_31}",
            "41 - 50": "{persentase_vis_41}",
            "51 - 60": "{persentase_vis_51}",
            "diatas 60": "{persentase_vis_60}"
        }
    },
    "Ringkasan_Jenis_Jabatan": {
        "count": {
            "Struktural": "{count_struktural}",
            "Fungsional": "{count_fungsional}",
            "Pelaksana": "{count_pelaksana}"
        },
        "persentase_vis": {
            "Struktural": "{persentase_vis_struktural}",
            "Fungsional": "{persentase_vis_fungsional}",
            "Pelaksana": "{persentase_vis_pelaksana}"
        }
    },
    "Jenis_Jabatan": {
        "count": {
            "JPT Utama": "{count_utama}",
            'JPT Madya': "{count_madya}",
            'JPT Pratama': "{count_pratama}",
            'Administrator': "{count_administrator}",
            'Pengawas': "{count_pengawas}",
            'Eselon V': "{count_eselon}",
            "JF Guru": "{count_jf_guru}",
            "JF Medis": "{count_jf_medis}",
            "JF Teknis": "{count_jf_teknis}",
            "PPPK Guru": "{count_pppk_guru}",
            "PPPK Kesehatan": "{count_pppk_medis}",
            "PPPK Teknis": "{count_pppk_teknis}"
        }
    }
}

#slide
selid_kategori_shared = {
    "Jenis_ASN": 0,
    "Jenis_Kelamin": 0,
    "Pendidikan": 0,
    "Masa_Kerja": 0,
    "Kelompok_Usia": 0,
    "Jenis_Jabatan": 0,
    "Ringkasan_Jenis_Jabatan": 0
}

#Mapping diagram
mapping_diagram_cm = {
    "SD-SMA": {"x": 13.27, "y": 7, "width": 1.2, "color": RGBColor(220, 20, 87)},
    "DI-DIII": {"x": 15.52, "y": 7, "width": 1.2, "color": RGBColor(220, 20, 87)},
    "DIV/S1": {"x": 17.73, "y": 7, "width": 1.2, "color": RGBColor(220, 20, 87)},
    "S2": {"x": 19.97, "y": 7, "width": 1.2, "color": RGBColor(220, 20, 87)},
    "S3": {"x": 22.29, "y": 7, "width": 1.2, "color": RGBColor(220, 20, 87)}
}

#Mapping Textbox
mapping_textbox_cm = {
    "SD-SMA": {"x": 13.27, "y_offset": 1.3, "width": 1.2},
    "DI-DIII": {"x": 15.52, "y_offset": 1.3, "width": 1.2},
    "DIV/S1": {"x": 17.73, "y_offset": 1.3, "width": 1.2},
    "S2": {"x": 19.97, "y_offset": 1.3, "width": 1.2},
    "S3": {"x": 22.29, "y_offset": 1.3, "width": 1.2}
}

TABLE_MAPPING = {
    "Masa_Kerja": {
        "count": "table_1",
        "persentase_vis": "table_2"
    },
    "Kelompok_Usia": {
        "count": "table_3",
        "persentase_vis": "table_4"
    },
    "Jenis_Jabatan": {
        "count": ["table_5","table_6"],
        "font_size" : 6
    }
}

#Mapping Bulan
bulan_map_id = {
    1: "Januari", 2: "Februari", 3: "Maret", 4: "April",
    5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus",
    9: "September", 10: "Oktober", 11: "November", 12: "Desember"
}
