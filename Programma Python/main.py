import json
from datetime import datetime, timedelta

# Constants
DATI_JSON = "Nessun dato letto da json"
START_TIME = timedelta(hours=21, minutes=0, seconds=0)


def open_json ():
    with open('./lineup.json', mode='r', encoding='utf-8') as f:
        global DATI_JSON
        DATI_JSON = f.read()

def sort_lineup (lineup):
    return sorted(lineup, key = lambda t: t["order"])

# Shows lineup in chronologycal order
def show_lineup_chronologycal ():
    sorted_tracks = sort_lineup(lineup)
    for lineup in sorted_tracks:
        print(f"{lineup['order']} - {lineup['band_name']}, {lineup['track_name']}")

# Shows lineup just like the file
def show_lineup ():
    lineup = json_data.get("lineup", [])
    for lineup in lineup:
        print(f"{lineup['order']} - {lineup['band_name']}, {lineup['track_name']}")

# Returns when the track will be played after the start of the concert
def when_track(lineup, trackName, default_interval=1.5):
    default_interval=timedelta(minutes=default_interval)

    timePassed = START_TIME

    for lineup_item in lineup:
        timePassed += default_interval
        
        duration = timedelta(
            hours=int(lineup_item['track_duration'].split(':')[0]),
            minutes=int(lineup_item['track_duration'].split(':')[1]),
            seconds=int(lineup_item['track_duration'].split(':')[2])
        )

        timePassed += duration

        if lineup_item['track_name'] == trackName:
            return str(timePassed)


# Returns details of a track
def track_details(trackName):
    for lineup_item in lineup:
        if lineup_item['track_name'] == trackName:
            return(f"{lineup_item['order']} - {lineup_item['band_name']}, {lineup_item['track_name']}, {lineup_item['track_duration']}")
    

def print_track_in_order_nicely(lineup, interval=1.5):
    sorted_tracks = sort_lineup(lineup)
    print(f"{'Order':<10}{'Band Name':<30}{'Track Name':<30}{'Duration':<15}{'Time of Track':<20}")
    print("-" * 105)
    for current_song in sorted_tracks:
        order = current_song['order']
        band_name = current_song['band_name']
        track_name = current_song['track_name']
        track_duration = current_song['track_duration']
        time_of_track = when_track(lineup, track_name, interval)

        print(f"{order:<10}{band_name:<30}{track_name:<30}{track_duration:<15}{time_of_track:<20}")
    




open_json()
json_data = json.loads(DATI_JSON)



lineup = json_data.get("lineup", [])

print_track_in_order_nicely(lineup)

#print(when_track("Stairway to Heaven", default_interval=0))
#print(track_details("Paranoid Android"))
#show_lineup()