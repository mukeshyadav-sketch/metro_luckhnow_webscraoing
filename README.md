# Lucknow Metro Web Scraper & Fare Collector

This project extracts station data and fare information for the Lucknow Metro (UP Metro Rail Corporation) from their official portal and consolidates it into a structured SQLite database (`metro.db`).

## Project Overview

The tool serves two main purposes:
1.  **Station Discovery**: Fetches a complete list of active metro stations.
2.  **Fare Matrix Generation**: Calculates the fare for every possible trip between any two stations.

## Files Description

-   **`main.py`**: The primary script to fetch station details (IDs, names, codes) and initialize the database with this data.
-   **`fare_collector.py`**: Iterates through all station pairs to query the API for fare details and populates the `fares` table. Uses delays to be a polite scraper.
-   **`db.py`**: Handles database schema creation (`stations` and `fares` tables).
-   **`ingest.py`**: Utility for inserting station data into the database.
-   **`command.txt`**: Contains handy commands and SQL queries for testing.

## Setup & Usage

### 1. Requirements
Ensure you have Python installed. Install the required libraries:
```bash
pip install requests pandas
```

### 2. Run the Scraper
Execute the scripts in the following order:

**Step A: Get Stations**
```bash
python main.py
```
*Creates `metro.db` and fills the `stations` table.*

**Step B: Get Fares**
```bash
python fare_collector.py
```
*Populates the `fares` table with prices for all routes.*

## Accessing the Data

The data is stored in `metro.db`. You can query it using `sqlite3`:

```bash
sqlite3 metro.db
```

**Sample Query: Check fare from Airport to Alambagh**
```sql
SELECT s1.st_name, s2.st_name, f.fare 
FROM fares f
JOIN stations s1 ON f.from_station_id = s1.id
JOIN stations s2 ON f.to_station_id = s2.id
WHERE s1.st_name = 'CCS AIRPORT' AND s2.st_name = 'ALAMBAGH';
```
