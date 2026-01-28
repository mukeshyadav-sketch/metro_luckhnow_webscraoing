import sqlite3

DB_NAME = "metro.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    # stations table (unchanged)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS stations (
        id INTEGER,
        st_name TEXT,
        st_code TEXT PRIMARY KEY
    )
    """)

    # fares table (UPDATED)
    cur.execute("""
    CREATE TABLE IF NOT EXISTS fares (
        from_station_id INTEGER,
        to_station_id   INTEGER,
        fare            INTEGER,
        PRIMARY KEY (from_station_id, to_station_id)
    )
    """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()
    print("Database and tables created")