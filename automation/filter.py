import argparse
from template.query_templates import get_wilker_prefix, get_kanreg_prefix
import re

#Untuk instansi dinamis
def get_instansi_filter():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--instansi', type=str, help='Nama instansi untuk filter dengan ILIKE')
    group.add_argument('--provinsi', type=str, help='Prefix Wilker untuk filter dengan ILIKE')
    group.add_argument('--kanreg', type=str, help='Prefix Kanreg untuk filter dengan ILIKE')
    group.add_argument('--nasional', action='store_true', help='Data Nasional tidak perlu input Prefix')
    args = parser.parse_args()
    if args.kanreg and not re.match(r'^\d{2}$', args.kanreg):
        parser.error("Kanreg harus berupa 2 digit angka. Misal : 07")
    return args

#untuk memisahkan logika filter yang berhubung dengan conn
def resolve_filter(args, conn):    
    if args.instansi:
        return args.instansi
    elif args.provinsi:
        return  get_wilker_prefix(conn, args.provinsi)
    elif args.kanreg:
        return get_kanreg_prefix(conn, args.kanreg)
    else:
        try:
            with open('instansi_filter.txt', 'r', encoding="utf-8") as file:
                return file.read().strip()
        except FileNotFoundError:
            print("File instansi_filter.txt tidak ditemukan. Silahkan ketik --nama instansi saat run")
            return None
        