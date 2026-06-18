from pptx.dml.color import RGBColor

#mappingan
label_column_per_kategori = {
    "Jenis_ASN": "jenis_asn",
    "Jenis_Kelamin": "jenis_kelamin",
    "Ringkasan_Jenis_Jabatan": "kelompok_jabatan",
    "Jenis_Jabatan": "jabatan",
    "Jenis_Instansi": "jenis_instansi",
    "Kelompok_Generasi": "kelompok_generasi"
}

#mapping ke key ppt
mapping_placeholder_per_kategori = {
    "Jenis_ASN":{
    "count": {
        "PNS": "{count_pns}",
        "PPPK": "{count_pppk}",
        "PPPK Paruh Waktu": "{count_pw}",
        "TOTAL": "{total_jenis_asn}"
    },
    "persentase_vis": {
        "PNS": "{persentase_vis_pns}",
        "PPPK": "{persentase_vis_pppk}",
        "PPPK Paruh Waktu": "{persentase_vis_pw}"
    }
    },
    "Jenis_Kelamin": {
    "count": {
        "Pria": "{count_pria}",
        "Wanita": "{count_wanita}"
    },
    "persentase_vis": {
        "Pria": "{persentase_vis_pria}",
        "Wanita": "{persentase_vis_wanita}"
    }
    },
    "Jenis_Jabatan":{
        "count":{
            "Struktural":{
                "PNS JPT Utama":"{count_jptu}",
                "PPPK JPT Utama":"{count_pjptu}",
                "PNS JPT Madya":"{count_jptm}",
                "PPPK JPT Madya":"{count_pjptm}",
                "PNS JPT Pratama":"{count_jptp}",
                "Administrator":"{count_administrator}",
                "Pengawas":"{count_pengawas}",
                "Eselon V":"{count_eselon}",
            },
            "JF Dosen":{
                "PNS":"{count_pns_dosen}",
                "PPPK":"{count_p3k_dosen}",
                "PPPK Paruh Waktu":"{count_pw_dosen}"
            },
            "JF Guru":{
                "PNS":"{count_pns_guru}",
                "PPPK":"{count_p3k_guru}",
                "PPPK Paruh Waktu":"{count_pw_guru}"
            },
            "JF Kesehatan":{
                "PNS":"{count_pns_nakes}",
                "PPPK":"{count_p3k_nakes}",
                "PPPK Paruh Waktu":"{count_pw_nakes}"
            },
            "JF Teknis":{
                "PNS":"{count_pns_teknis}",
                "PPPK":"{count_p3k_teknis}"
            },
            "Pelaksana":{
                "PNS":"{count_pns_pelaksana}",
                "PPPK":"{count_p3k_pelaksana}",
                "PPPK Paruh Waktu":"{count_pw_pelaksana}"
            }
        }
    },
    "Ringkasan_Jenis_Jabatan": {
        "count": {
            "Struktural": "{count_struktural}",
            "JF Dosen": "{count_dosen}",
            "JF Guru": "{count_guru}",
            "JF Kesehatan": "{count_kesehatan}",
            "JF Teknis": "{count_teknis}",
            "Pelaksana": "{count_pelaksana}"
        },
        "persentase_vis": {
            "Struktural": "{persentase_vis_struktural}",
            "JF Dosen": "{persentase_vis_dosen}",
            "JF Guru": "{persentase_vis_guru}",
            "JF Kesehatan": "{persentase_vis_kesehatan}",
            "JF Teknis": "{persentase_vis_teknis}",
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
    },
    "Kelompok_Generasi":{
        "persentase_vis":{
            "Baby Boomers (1946-1964)" : "{persentase_bb}",
            "Gen X (1965-1980)": "{persentase_x}",
            "Gen Y (1981-1996)": "{persentase_y}",
            "Gen Z (1997-2012)": "{persentase_z}"
        },
        "count":{
            "Baby Boomers (1946-1964)" : "{count_bb}",
            "Gen X (1965-1980)": "{count_x}",
            "Gen Y (1981-1996)": "{count_y}",
            "Gen Z (1997-2012)": "{count_z}"            
        }
    }
}

#slide
selid_kategori_shared = {
    "Jenis_ASN": 0,
    "Jenis_Instansi": 0,
    "Jenis_Kelamin": 0,
    "Pendidikan": 0,
    "Jenis_Jabatan": 0,
    "Ringkasan_Jenis_Jabatan": 0,
    "Kelompok_Generasi": 0
}

#Mapping diagram instansi
mapping_diagram_cm = {
    "SD-SMA": {"x": 1.47, "y": 26, "width": 2.68, "color": RGBColor(231, 69, 123)},
    "DI-DIII": {"x": 4.46, "y": 26, "width": 2.68, "color": RGBColor(231, 69, 123)},
    "DIV/S1": {"x": 7.44, "y": 26, "width": 2.68, "color": RGBColor(231, 69, 123)},
    "S2": {"x": 10.45, "y": 26, "width": 2.68, "color": RGBColor(231, 69, 123)},
    "S3": {"x": 13.41, "y": 26, "width": 2.68, "color": RGBColor(231, 69, 123)}
}

#Mapping diagram Nasional
mapping_diagram_nasional = {
    "SD-SMA": {"x": 1.47, "y": 26, "width": 2.68, "color": RGBColor(231, 69, 123)},
    "DI-DIII": {"x": 4.46, "y": 26, "width": 2.68, "color": RGBColor(231, 69, 123)},
    "DIV/S1": {"x": 7.44, "y": 26, "width": 2.68, "color": RGBColor(231, 69, 123)},
    "S2": {"x": 10.45, "y": 26, "width": 2.68, "color": RGBColor(231, 69, 123)},
    "S3": {"x": 13.41, "y": 26, "width": 2.68, "color": RGBColor(231, 69, 123)}
}

#Mapping Textbox instansi
mapping_textbox_cm = {
    "SD-SMA": {"x": 1.62, "y_offset": 2, "width": 2.36},
    "DI-DIII": {"x": 4.61, "y_offset": 2, "width": 2.36},
    "DIV/S1": {"x": 7.59, "y_offset": 2, "width": 2.36},
    "S2": {"x": 10.6, "y_offset": 2, "width": 2.36},
    "S3": {"x": 13.56, "y_offset": 2, "width": 2.36}
}

#Mapping Textbox Nasional
mapping_textbox_nasional = {
    "SD-SMA": {"x": 1.62, "y_offset": 1.6, "width": 2.36},
    "DI-DIII": {"x": 4.61, "y_offset": 1.6, "width": 2.36},
    "DIV/S1": {"x": 7.59, "y_offset": 1.6, "width": 2.36},
    "S2": {"x": 10.6, "y_offset": 1.6, "width": 2.36},
    "S3": {"x": 13.56, "y_offset": 1.6, "width": 2.36}
}

#Mapping Color Textbox
mapping_color_textbox = {
    "SD-SMA": RGBColor(89,89,89),
    "DI-DIII": RGBColor(89,89,89),
    "DIV/S1": RGBColor(89,89,89),
    "S2": RGBColor(89,89,89),
    "S3": RGBColor(89,89,89)
}

'''
#Mapping Color Lama
#Mapping diagram instansi
mapping_diagram_cm = {
    "SD-SMA": {"x": 1.47, "y": 26, "width": 2.68, "color": RGBColor(92, 157, 178)},
    "DI-DIII": {"x": 4.46, "y": 26, "width": 2.68, "color": RGBColor(65, 184, 213)},
    "DIV/S1": {"x": 7.44, "y": 26, "width": 2.68, "color": RGBColor(45, 139, 186)},
    "S2": {"x": 10.45, "y": 26, "width": 2.68, "color": RGBColor(245, 129, 98)},
    "S3": {"x": 13.41, "y": 26, "width": 2.68, "color": RGBColor(69, 70, 146)}
}

#Mapping diagram Nasional
mapping_diagram_nasional = {
    "SD-SMA": {"x": 1.47, "y": 26, "width": 2.68, "color": RGBColor(92, 157, 178)},
    "DI-DIII": {"x": 4.46, "y": 26, "width": 2.68, "color": RGBColor(65, 184, 213)},
    "DIV/S1": {"x": 7.44, "y": 26, "width": 2.68, "color": RGBColor(45, 139, 186)},
    "S2": {"x": 10.45, "y": 26, "width": 2.68, "color": RGBColor(245, 129, 98)},
    "S3": {"x": 13.41, "y": 26, "width": 2.68, "color": RGBColor(69, 70, 146)}
}

#Mapping Textbox instansi
mapping_textbox_cm = {
    "SD-SMA": {"x": 1.62, "y_offset": 2, "width": 2.36},
    "DI-DIII": {"x": 4.61, "y_offset": 2, "width": 2.36},
    "DIV/S1": {"x": 7.59, "y_offset": 2, "width": 2.36},
    "S2": {"x": 10.6, "y_offset": 2, "width": 2.36},
    "S3": {"x": 13.56, "y_offset": 2, "width": 2.36}
}

#Mapping Textbox Nasional
mapping_textbox_nasional = {
    "SD-SMA": {"x": 1.62, "y_offset": 2, "width": 2.36},
    "DI-DIII": {"x": 4.61, "y_offset": 2, "width": 2.36},
    "DIV/S1": {"x": 7.59, "y_offset": 2, "width": 2.36},
    "S2": {"x": 10.6, "y_offset": 2, "width": 2.36},
    "S3": {"x": 13.56, "y_offset": 2, "width": 2.36}
}

#Mapping Color Textbox
mapping_color_textbox = {
    "SD-SMA": RGBColor(92, 157, 178),
    "DI-DIII": RGBColor(65, 184, 213),
    "DIV/S1": RGBColor(45, 139, 186),
    "S2": RGBColor(245, 129, 98),
    "S3": RGBColor(69, 70, 146)
}
'''

#Mapping Bulan
bulan_map_id = {
    1: "Januari", 2: "Februari", 3: "Maret", 4: "April",
    5: "Mei", 6: "Juni", 7: "Juli", 8: "Agustus",
    9: "September", 10: "Oktober", 11: "November", 12: "Desember"
}

#posisi table dinamis instansi
'''TABLE_POSITIONS = {
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
    "Kelompok_Generasi": {
        "slide_index": 0,
        "pos_x_cm": 1.16,
        "pos_y_cm": 9.58,
        "col_widths_cm": [4.0, 1.45],
        "label_column": "kelompok_generasi",
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
            "pos_x_cm": 8.34,
            "pos_y_cm": 10,
            "col_widths_cm": [2.26, 0.8],
            "label_column": "jabatan",
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
        "Pelaksana": {
            "slide_index": 0,
            "pos_x_cm": 11.66,
            "pos_y_cm": 10,
            "col_widths_cm": [2.26, 0.8],
            "label_column": "jabatan",
            "value_column": "count",
            "margin": {
                "left": 0,
                "right": 0.1,
                "top": 0,
                "bottom": 0
            },
            "fill_color": "CCDCF6",
            "label_order": ["PNS","PPPK","PPPK Paruh Waktu"]
        },
        "JF Dosen": {
            "slide_index": 0,
            "pos_x_cm": 14.92,
            "pos_y_cm": 9,
            "col_widths_cm": [2.16, 0.9],
            "label_column": "jabatan",
            "value_column": "count",
            "margin": {
                "left": 0,
                "right": 0.1,
                "top": 0,
                "bottom": 0
            },
            "fill_color": "F9BFD2",
            "label_order": ["PNS","PPPK","PPPK Paruh Waktu"]
        },
         "JF Guru": {
            "slide_index": 0,
            "pos_x_cm": 18.12,
            "pos_y_cm": 9,
            "col_widths_cm": [2.16, 0.9],
            "label_column": "jabatan",
            "value_column": "count",
            "margin": {
                "left": 0,
                "right": 0.1,
                "top": 0,
                "bottom": 0
            },
            "fill_color": "F9BFD2",
            "label_order": ["PNS","PPPK","PPPK Paruh Waktu"]
        },
        "JF Kesehatan": {
            "slide_index": 0,
            "pos_x_cm": 14.92,
            "pos_y_cm": 11.13,
            "col_widths_cm": [2.16, 0.9],
            "label_column": "jabatan",
            "value_column": "count",
            "margin": {
                "left": 0,
                "right": 0.1,
                "top": 0,
                "bottom": 0
            },
            "fill_color": "F9BFD2",
            "label_order": ["PNS","PPPK","PPPK Paruh Waktu"]
        },
        "JF Teknis": {
            "slide_index": 0,
            "pos_x_cm": 18.12,
            "pos_y_cm": 11.13,
            "col_widths_cm": [2.16, 0.9],
            "label_column": "jabatan",
            "value_column": "count",
            "margin": {
                "left": 0,
                "right": 0.1,
                "top": 0,
                "bottom": 0
            },
            "fill_color": "F9BFD2",
            "label_order": ["PNS","PPPK","PPPK Paruh Waktu"]
        }
    }
}'''

#posisi table dinamis nasional
'''TABLE_POSITIONS_NAS = {
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
            "pos_x_cm": 9.45,
            "pos_y_cm": 10.48,
            "col_widths_cm": [2.26, 1.2],
            "label_column": "jabatan",
            "value_column": "count",
            "margin": {
                "left": 0,
                "right": 0.1,
                "top": 0,
                "bottom": 0
            },
            "fill_color": "FDEADA",
            "label_order": ["PNS JPT Utama", "PPPK JPT Utama", "PNS JPT Madya", "PPPK JPT Madya",
                            "PNS JPT Pratama", "PPPK JPT Pratama",
                            "Administrator", "Pengawas", "Eselon V"]
        },
        "JF Dosen": {
            "slide_index": 0,
            "pos_x_cm": 13.89,
            "pos_y_cm": 9.96,
            "col_widths_cm": [2.02, 1.05],
            "label_column": "jabatan",
            "value_column": "count",
            "margin": {
                "left": 0,
                "right": 0.1,
                "top": 0,
                "bottom": 0
            },
            "fill_color": "F9BFD2",
            "label_order": ["PNS","PPPK","PPPK Paruh Waktu"]
        },
            "JF Guru": {
            "slide_index": 0,
            "pos_x_cm": 13.89,
            "pos_y_cm": 12.21,
            "col_widths_cm": [2.02, 1.05],
            "label_column": "jabatan",
            "value_column": "count",
            "margin": {
                "left": 0,
                "right": 0.1,
                "top": 0,
                "bottom": 0
            },
            "fill_color": "F9BFD2",
            "label_order": ["PNS","PPPK","PPPK Paruh Waktu"]
        },
            "JF Kesehatan": {
            "slide_index": 0,
            "pos_x_cm": 17.6,
            "pos_y_cm": 9.96,
            "col_widths_cm": [2.02, 1.05],
            "label_column": "jabatan",
            "value_column": "count",
            "margin": {
                "left": 0,
                "right": 0.1,
                "top": 0,
                "bottom": 0
            },
            "fill_color": "F9BFD2",
            "label_order": ["PNS","PPPK","PPPK Paruh Waktu"]
        },
            "JF Teknis": {
            "slide_index": 0,
            "pos_x_cm": 17.6,
            "pos_y_cm": 12.21,
            "col_widths_cm": [2.02, 1.05],
            "label_column": "jabatan",
            "value_column": "count",
            "margin": {
                "left": 0,
                "right": 0.1,
                "top": 0,
                "bottom": 0
            },
            "fill_color": "F9BFD2",
            "label_order": ["PNS","PPPK","PPPK Paruh Waktu"]
        },
            "Pelaksana": {
            "slide_index": 0,
            "pos_x_cm": 21.45,
            "pos_y_cm": 9.99,
            "col_widths_cm": [2.02, 1.05],
            "label_column": "jabatan",
            "value_column": "count",
            "margin": {
                "left": 0,
                "right": 0.1,
                "top": 0,
                "bottom": 0
            },
            "fill_color": "CCDCF6",
            "label_order": ["PNS","PPPK","PPPK Paruh Waktu"]
        }
    }
}'''

#mapping vis table
'''VIS_TABLE_POSITIONS = {
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
        "Kelompok_Generasi": {
        "slide_index": 0,
        "pos_x_cm": 6.7,
        "pos_y_cm": 9.58,
        "col_widths_cm": [0.81],
        "value_column": "persentase_vis",
        "margin": {
            "left": 0.02,
            "right": 0.02,
            "top": 0,
            "bottom": 0
        }
    }
}'''

#warna piechart
'''color_map = {
    "Gen Z (1997-2012)": "#FFAB40",
    "Gen Y (1981-1996)": "#78909C",
    "Gen X (1965-1980)": "#ED7D31",
    "Baby Boomers (1946-1964)": "#3F51B5"
}'''
