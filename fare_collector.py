import requests
import sqlite3
import itertools
import time

DB_NAME = "metro.db"

ROUTE_API = (
    "https://portal.upmetrorail.com/en/api/v2/route/"
    "{from_code}/{to_code}/station/station/least-distance/1970-01-01/"
)

def get_stations():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("SELECT id, st_code FROM stations")
    stations = cur.fetchall()  # [(id, code), ...]

    conn.close()
    return stations


def insert_fare(from_id, to_id, fare):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    INSERT OR IGNORE INTO fares (from_station_id, to_station_id, fare)
    VALUES (?, ?, ?)
    """, (from_id, to_id, fare))

    conn.commit()
    conn.close()


def fetch_and_store_fares():
    stations = get_stations()

    # unique combinations → no same station, no duplicates
    for (from_id, from_code), (to_id, to_code) in itertools.combinations(stations, 2):

        url = ROUTE_API.format(
            from_code=from_code,
            to_code=to_code
        )

        try:
            res = requests.get(url, timeout=10)
            res.raise_for_status()
            data = res.json()

            fare = data.get("fare")

            if fare is not None:
                insert_fare(from_id, to_id, fare)
                print(f"{from_code} ({from_id}) → {to_code} ({to_id}) : ₹{fare}")
            else:
                print(f"No fare for {from_code} → {to_code}")

            time.sleep(0.5)

        except Exception as e:
            print(f"Failed {from_code} → {to_code} : {e}")


if __name__ == "__main__":
    fetch_and_store_fares()