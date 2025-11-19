from pptx.dml.color import RGBColor

#mappingan
label_column_per_kategori = {
    "Jenis_ASN": "jenis_asn",
    "Jenis_Kelamin": "jenis_kelamin",
    "Masa_Kerja": "kelompok_masa_kerja",
    "Kelompok_Usia": "kelompok_usia",
    "Ringkasan_Jenis_Jabatan": "kelompok_jabatan",
    "Jenis_Jabatan": "jenisjabatannew",
    "Jenis_Instansi": "jenis_instansi",
    "Kelompok_Generasi": "kelompok_generasi"
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
    "Jenis_Instansi": {
        "count":{
            "D": "{count_daerah}",
            "P": "{count_pusat}"
        },
        "persentase_vis":{
            "D": "{persentase_vis_daerah}",
            "P": "{persentase_vis_pusat}"
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
    "Ringkasan_Jenis_Jabatan": 0,
    "Kelompok_Generasi": 0
}

#Mapping diagram instansi
mapping_diagram_cm = {
    "SD-SMA": {"x": 13.27, "y": 7, "width": 1.2, "color": RGBColor(220, 20, 87)},
    "DI-DIII": {"x": 15.52, "y": 7, "width": 1.2, "color": RGBColor(220, 20, 87)},
    "DIV/S1": {"x": 17.73, "y": 7, "width": 1.2, "color": RGBColor(220, 20, 87)},
    "S2": {"x": 19.97, "y": 7, "width": 1.2, "color": RGBColor(220, 20, 87)},
    "S3": {"x": 22.29, "y": 7, "width": 1.2, "color": RGBColor(220, 20, 87)}
}

#Mapping diagram Nasional
mapping_diagram_nasional = {
    "SD-SMA": {"x": 0.52, "y": 12.53, "width": 1.2, "color": RGBColor(220, 20, 87)},
    "DI-DIII": {"x": 2.17, "y": 12.53, "width": 1.2, "color": RGBColor(220, 20, 87)},
    "DIV/S1": {"x": 3.91, "y": 12.53, "width": 1.2, "color": RGBColor(220, 20, 87)},
    "S2": {"x": 5.55, "y": 12.53, "width": 1.2, "color": RGBColor(220, 20, 87)},
    "S3": {"x": 7.34, "y": 12.53, "width": 1.2, "color": RGBColor(220, 20, 87)}
}

#Mapping Textbox
mapping_textbox_cm = {
    "SD-SMA": {"x": 13.27, "y_offset": 1.3, "width": 1.2},
    "DI-DIII": {"x": 15.52, "y_offset": 1.3, "width": 1.2},
    "DIV/S1": {"x": 17.73, "y_offset": 1.3, "width": 1.2},
    "S2": {"x": 19.97, "y_offset": 1.3, "width": 1.2},
    "S3": {"x": 22.29, "y_offset": 1.3, "width": 1.2}
}

#Mapping Textbox Nasional
mapping_textbox_nasional = {
    "SD-SMA": {"x": 0.52, "y_offset": 1.3, "width": 1.2},
    "DI-DIII": {"x": 2.17, "y_offset": 1.3, "width": 1.2},
    "DIV/S1": {"x": 3.91, "y_offset": 1.3, "width": 1.2},
    "S2": {"x": 5.55, "y_offset": 1.3, "width": 1.2},
    "S3": {"x": 7.34, "y_offset": 1.3, "width": 1.2}
}

#Mapping Bulan
bulan_map_id = {
    1: "Januari", 2: "Februari", 3: "Maret", 4: "April",
    5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus",
    9: "September", 10: "Oktober", 11: "November", 12: "Desember"
}

#posisi table dinamis instansi
TABLE_POSITIONS = {
    "Masa_Kerja": {
        "slide_index": 0,
        "pos_x_cm": 1.15,
        "pos_y_cm": 8.87,
        "col_widths_cm": [2.0, 2.25],
        "label_column": "kelompok_masa_kerja",
        "value_column": "count",
        "margin": {
            "left": 0.02,
            "right": 0.02,
            "top": 0,
            "bottom": 0
        },
        "fill_color": "BAF8FF"
    },
    "Kelompok_Usia": {
        "slide_index": 0,
        "pos_x_cm": 8.36,
        "pos_y_cm": 8.87,
        "col_widths_cm": [1.6, 2.0],
        "label_column": "kelompok_usia",
        "value_column": "count",
        "margin": {
            "left": 0.02,
            "right": 0.02,
            "top": 0,
            "bottom": 0
        },
        "fill_color": "BAF8FF"
    },
    "Jenis_Jabatan": {
        "Struktural": {
            "slide_index": 0,
            "pos_x_cm": 13.97,
            "pos_y_cm": 10,
            "col_widths_cm": [2.26, 0.8],
            "label_column": "jenisjabatan",
            "value_column": "count",
            "margin": {
                "left": 0,
                "right": 0.1,
                "top": 0,
                "bottom": 0
            },
            "fill_color": "FDEADA",
            "label_order": ["PNS JPT Utama", "PNS JPT Madya", "PNS JPT Pratama", 
                            "PPPK JPT Utama", "PPPK JPT Madya", "PPPK JPT Pratama",
                            "Administrator", "Pengawas", "Eselon V"]
        },
        "Fungsional": {
            "slide_index": 0,
            "pos_x_cm": 17.74,
            "pos_y_cm": 10,
            "col_widths_cm": [2.16, 0.9],
            "label_column": "jenisjabatan",
            "value_column": "count",
            "margin": {
                "left": 0,
                "right": 0.1,
                "top": 0,
                "bottom": 0
            },
            "fill_color": "F9BFD2",
            "label_order": ["PNS JF Dosen", "PNS JF Guru", "PNS JF Medis", "PNS JF Teknis",
                            "PPPK JF Dosen","PPPK JF Guru", "PPPK JF Medis", "PPPK JF Teknis"]
        }
    }
}

#mapping table dinamis nasional
#posisi table dinamis instansi
TABLE_POSITIONS_NAS = {
    "Masa_Kerja": {
        "slide_index": 0,
        "pos_x_cm": 8.98,
        "pos_y_cm": 7.98,
        "col_widths_cm": [1.5, 2.75],
        "label_column": "kelompok_masa_kerja",
        "value_column": "count",
        "margin": {
            "left": 0.02,
            "right": 0.02,
            "top": 0,
            "bottom": 0.3
        },
        "fill_color": "E8EDFD"
    },
    "Jenis_Jabatan": {
        "Struktural": {
            "slide_index": 0,
            "pos_x_cm": 13.72,
            "pos_y_cm": 8.98,
            "col_widths_cm": [2.26, 1.2],
            "label_column": "jenisjabatan",
            "value_column": "count",
            "margin": {
                "left": 0,
                "right": 0.1,
                "top": 0,
                "bottom": 0.2
            },
            "fill_color": "FDEADA",
            "label_order": ["PNS JPT Utama", "PPPK JPT Utama", "PNS JPT Madya", "PPPK JPT Madya",
                            "PNS JPT Pratama", "PPPK JPT Pratama",
                            "Administrator", "Pengawas", "Eselon V"]
        },
        "Fungsional": {
            "slide_index": 0,
            "pos_x_cm": 17.43,
            "pos_y_cm": 8.98,
            "col_widths_cm": [2.46, 1.8],
            "label_column": "jenisjabatan",
            "value_column": "count",
            "margin": {
                "left": 0,
                "right": 0.1,
                "top": 0,
                "bottom": 0.2
            },
            "fill_color": "F9BFD2",
            "label_order": ["PNS JF Dosen", "PNS JF Guru", "PNS JF Medis", "PNS JF Teknis",
                            "PPPK JF Dosen","PPPK JF Guru", "PPPK JF Medis", "PPPK JF Teknis"]
        }
    }
}

#mapping vis table
VIS_TABLE_POSITIONS = {
    "Masa_Kerja": {
        "slide_index": 0,
        "pos_x_cm": 5.53,
        "pos_y_cm": 8.87,
        "col_widths_cm": [0.81],
        "value_column": "persentase_vis",
        "margin": {
            "left": 0.02,
            "right": 0.02,
            "top": 0,
            "bottom": 0
        }
    },
        "Kelompok_Usia": {
        "slide_index": 0,
        "pos_x_cm": 12.15,
        "pos_y_cm": 8.87,
        "col_widths_cm": [0.81],
        "value_column": "persentase_vis",
        "margin": {
            "left": 0.02,
            "right": 0.02,
            "top": 0,
            "bottom": 0
        }
    }
}

#warna piechart
color_map = {
    "Gen Z (1997-2012)": "#FFAB40",
    "Gen Y (1981-1996)": "#78909C",
    "Gen X (1965-1980)": "#ED7D31",
    "Baby Boomers (1946-1964)": "#3F51B5"
}
