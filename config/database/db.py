import psycopg2

def connection_db():
    """Connection driver postgresql"""
    conn = psycopg2.connect(
        host="db",
        port=5432,
        dbname="desafiodev",
        user="postgres",
        password="postgrespw",
        sslmode="disable",
        connect_timeout=5
    )
    conn.autocommit = True
    return conn.cursor()
