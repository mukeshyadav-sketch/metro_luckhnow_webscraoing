# import requests

# URL = "https://portal.upmetrorail.com/en/api/v2/stations_localities_by_keyword/1/"

# res = requests.get(URL)
# res.raise_for_status()

# data = res.json()

# print(type(data))        # should be list
# print(type(data[0]))     # should be dict
# print(data[0].keys())    # see station fields


import requests
import pandas as pd
from ingest import insert_stations

URL = "https://portal.upmetrorail.com/en/api/v2/stations_localities_by_keyword/1/"

res = requests.get(URL)
res.raise_for_status()

data = res.json()

# Extract stations correctly
stations_list = data[0]["stations"]

df = pd.json_normalize(stations_list)

df = df[["id", "st_name", "st_code"]]

print(df)

insert_stations(df)