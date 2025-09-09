import argparse
from template.query_templates import get_wilker_prefix

#Untuk instansi dinamis
def get_instansi_filter():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--instansi', type=str, help='Nama instansi untuk filter dengan ILIKE')
    group.add_argument('--wilker', type=str, help='Prefix Wilker untuk filter dengan ILIKE')
    args = parser.parse_args()
    return args

#untuk memisahkan logika filter yang berhubung dengan conn
def resolve_filter(args, conn):    
    if args.instansi:
        return args.instansi
    elif args.wilker:
        return  get_wilker_prefix(conn, args.wilker)
    else:
        try:
            with open('instansi_filter.txt', 'r', encoding="utf-8") as file:
                return file.read().strip()
        except FileNotFoundError:
            print("File instansi_filter.txt tidak ditemukan. Silahkan ketik --nama instansi saat run")
            return None
        