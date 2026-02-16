import psycopg

conn = psycopg.connect(
    host="localhost",
    port=5432,
    dbname="lab1",
    user="postgres",
    password="mattinaomi"
)

conn.close()