import json
from datetime import datetime, timedelta

DATI_JSON = "Nessun dato letto da json"

START_TIME = datetime.strptime("21:00", "%H:%M")

def open_json ():
    with open('./lineup.json', mode='r', encoding='utf-8') as f:
        global DATI_JSON
        DATI_JSON = f.read()

def show_lineup_chronologycal ():
    sorted_tracks = sorted(lineup, key = lambda t: t["order"])
    for lineup in sorted_tracks:
        print(f"{lineup['order']} - {lineup['band_name']}, {lineup['track_name']}")

def show_lineup ():
    lineup = json_data.get("lineup", [])
    for lineup in lineup:
        print(f"{lineup['order']} - {lineup['band_name']}, {lineup['track_name']}")

def when_track(trackName):
    timePassed = timedelta()
    for lineup_item in lineup:
        timePassed += timedelta(minutes=3)
        minutes, seconds = map(int, lineup_item['track_duration'].split(':'))
        timePassed += timedelta(minutes=minutes, seconds=seconds)
        if lineup_item["track_name"] == trackName:
            return str(timePassed)

open_json()
json_data = json.loads(DATI_JSON)
lineup = json_data.get("lineup", [])
when_track("Stairway to Heaven")

show_lineup()