import json
from datetime import datetime, timedelta

DATI_JSON = "Nessun dato letto da json"

START_TIME = datetime.strptime("21:00", "%H:%M")

def open_json ():
    with open('./lineup.json', mode='r', encoding='utf-8') as f:
        global DATI_JSON
        DATI_JSON = f.read()

# Shows lineup in chronologycal order
def show_lineup_chronologycal ():
    sorted_tracks = sorted(lineup, key = lambda t: t["order"])
    for lineup in sorted_tracks:
        print(f"{lineup['order']} - {lineup['band_name']}, {lineup['track_name']}")

# Shows lineup just like the file
def show_lineup ():
    lineup = json_data.get("lineup", [])
    for lineup in lineup:
        print(f"{lineup['order']} - {lineup['band_name']}, {lineup['track_name']}")

# Returns when the track will be played after the start of the concert
def when_track(trackName):
    timePassed = timedelta()
    for lineup_item in lineup:
        timePassed += timedelta(minutes=1.5) #in media un minuto e mezzo tra una canzone e l'altra
        hours, minutes, seconds = map(int, lineup_item['track_duration'].split(':'))
        if lineup_item["track_name"] == trackName:
            return str(timePassed)
        timePassed += timedelta(hours=hours, minutes=minutes, seconds=seconds)
    return "Nessuna traccia trovata, controlla che esista o che l'hai scritta in modo corretto"

# Returns details of a track
def track_details(trackName):
    for lineup_item in lineup:
        if lineup_item['track_name'] == trackName:
            return(f"{lineup_item['order']} - {lineup_item['band_name']}, {lineup_item['track_name']}, {lineup_item['track_duration']}")
    

open_json()
json_data = json.loads(DATI_JSON)
lineup = json_data.get("lineup", [])
print(when_track("Stairway to Heaven"))
print(track_details("Paranoid Android"))

#show_lineup()