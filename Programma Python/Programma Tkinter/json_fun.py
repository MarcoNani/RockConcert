import json

def open_json ():
    with open('../lineup.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return (data.get("lineup", []))

def sort_lineup (lineup):
    return sorted(lineup, key = lambda t: t["order"])

def search_records(self):
    """Cerca record nella tabella."""
    search_term = self.search_entry.get().lower()
        
    # Cancella dati esistenti
    for i in self.table.get_children():
        self.table.delete(i)
    
    # Se non c'è termine di ricerca, mostra tutti i dati
    if not search_term:
        for record in self.all_data:
            values = (
                record["band_name"],
                record["track_name"],
                record["track_duration"],
                record.get("time_before", "N/A"),
                record.get("time_after", "N/A")
            )
            self.table.insert("", "end", values=values)
        return
            
    # Altrimenti filtra i dati
    for record in self.all_data:
        # Converte tutti i valori in stringhe e controlla se il termine di ricerca è presente
        if any(search_term in str(value).lower() for value in record.values()):
            values = (
                record["band_name"],
                record["track_name"],
                record["track_duration"],
                record.get("time_before", "N/A"),
                record.get("time_after", "N/A")
            )
            self.table.insert("", "end", values=values)
