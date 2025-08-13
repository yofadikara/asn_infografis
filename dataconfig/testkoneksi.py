import psycopg2

conn = psycopg2.connect(
    host="10.100.9.46",
    port="5432",
    dbname="db_backup",
    user="yofa",
    password="ay@mT3rb4n9"
)
print("✅ Terhubung ke database!")
