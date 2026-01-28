from db import get_connection

def insert_stations(df):
    conn = get_connection()
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute("""
        INSERT OR IGNORE INTO stations (id, st_name, st_code)
        VALUES (?, ?, ?)
        """, (row.id, row.st_name, row.st_code))

    conn.commit()
    conn.close()

    print("Stations inserted successfully")