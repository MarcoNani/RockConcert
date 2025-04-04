import json
from datetime import datetime, timedelta

START_TIME = timedelta(hours=21, minutes=0, seconds=0)

def open_json():
    """Apre il file JSON e restituisce i dati della lineup."""
    with open('../lineup.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return (data.get("lineup", []))

def sort_lineup(lineup):
    """Ordina la lineup in base all'attributo 'order'."""
    return sorted(lineup, key=lambda t: t["order"])
    
def save_lineup(lineup_data):
    """Salva la lineup nel file JSON."""
    with open('../lineup.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    # Aggiorna la lineup nel dizionario
    data["lineup"] = lineup_data
    
    # Salva il file aggiornato
    with open('../lineup.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def when_track(lineup, trackName, default_interval=1.5):
    """Calcola l'orario di esecuzione di un brano dopo l'inizio del concerto."""
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