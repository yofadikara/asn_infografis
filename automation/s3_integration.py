import os
import boto3
from botocore.config import Config
from dotenv import load_dotenv
import uuid
import psycopg2
from dataconfig.mapping import logger

load_dotenv()

aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_bucket_name = os.getenv("AWS_BUCKET_NAME")
endpoint_url = os.getenv("ENDPOINT_URL")

dashboard_host = os.getenv("DB_DASHBOARD_HOST")
dashboard_port = os.getenv("DB_DASHBOARD_PORT")
dashboard_user = os.getenv("DB_DASHBOARD_USER")
dashboard_password = os.getenv("DB_DASHBOARD_PASS")
dashboard_name = os.getenv("DB_DASHBOARD_NAME")

def get_dashboard_conn():
    return psycopg2.connect(
        host=dashboard_host,
        port=dashboard_port,
        user=dashboard_user,
        password=dashboard_password,
        dbname=dashboard_name
    )

def get_s3_client():
    return boto3.client(
        "s3",
        aws_access_key_id = aws_access_key_id,
        aws_secret_access_key = aws_secret_access_key,
        endpoint_url = endpoint_url,
        config=Config(
            request_checksum_calculation="when_required",
            response_checksum_validation="when_required",
        )
    )

def upload_file_s3(local_file, s3_path):
    s3 = get_s3_client()
    '''s3.upload_file(local_file, aws_bucket_name, s3_path)
    s3_url = f"{endpoint_url}/{aws_bucket_name}/{s3_path}"'''
    with open(local_file, "rb") as f:
        s3.put_object(
            Bucket=aws_bucket_name,
            Key=s3_path,
            Body=f
        )
    s3_url = f"{endpoint_url}/{aws_bucket_name}{s3_path}"
    return s3_url

def save_to_db(periode, instansi_id, path):
    conn = get_dashboard_conn()
    try: 
        uid = uuid.uuid4().hex  # generate uid otomatis
        query = """
            INSERT INTO dash_portal.path_infografis_cc (id, periode, instansi_id, path)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (instansi_id, periode) DO NOTHING
            """
        with conn.cursor() as cur:
            cur.execute(query, (uid, periode, instansi_id, path))
        conn.commit()
        if cur.rowcount > 0:
            logger.info(f"Data berhasil disimpan ke DB: {instansi_id} | {periode} | {path}")
        else:
            logger.warning(f"Data sudah ada, skip insert: {instansi_id} | {periode}")
    finally:
        conn.close()