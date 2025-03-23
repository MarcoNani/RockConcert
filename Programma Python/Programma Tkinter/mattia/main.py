import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkfont
import json_fun

class LoginTableApp(tk.Tk):
    """Applicazione principale con sistema di navigazione tra frame."""
    
    def __init__(self):
        super().__init__()
        self.title("Login & Tabella App")
        self.geometry("800x600")
        
        # Dizionario utenti (in un'app reale, dovrebbe essere un database)
        self.users = {"admin": "password123", "user": "password"}
        
        # Mantieni traccia dell'utente corrente
        self.current_user = None
        
        # Configura il font dell'applicazione
        self.title_font = tkfont.Font(family="Helvetica", size=18, weight="bold")
        
        # Crea un container per impilare i frame
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # Crea dizionario dei frame
        self.frames = {}
        
        # Inizializza i frame
        for F in (LoginFrame, SearchTableFrame):
            frame = F(parent=container, controller=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Mostra il frame di login all'avvio
        self.show_frame(LoginFrame)
    
    def show_frame(self, frame_class):
        """Solleva il frame specificato in cima."""
        frame = self.frames[frame_class]
        frame.tkraise()
        
    def login(self, username, password):
        """Verifica le credenziali di login."""
        if username in self.users and self.users[username] == password:
            self.current_user = username
            self.show_frame(SearchTableFrame)
            # Aggiorna la tabella con i controlli dell'ordine se l'utente è admin
            self.frames[SearchTableFrame].update_table_for_user(username == "admin")
            return True
        else:
            messagebox.showerror("Errore", "Nome utente o password non validi!")
            return False
            
    def is_admin(self):
        """Controlla se l'utente corrente è un admin."""
        return self.current_user == "admin"


class LoginFrame(tk.Frame):
    """Frame per la pagina di login."""
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        
        # Crea layout di login
        login_container = tk.Frame(self, padx=80, pady=80)
        login_container.place(relx=0.5, rely=0.5, anchor="center")
        
        # Titolo
        title = tk.Label(login_container, text="Login", font=controller.title_font)
        title.grid(row=0, column=0, columnspan=2, pady=(0, 30))
        
        # Username
        username_label = tk.Label(login_container, text="Nome Utente:")
        username_label.grid(row=1, column=0, sticky="e", padx=(0, 10), pady=10)
        self.username_entry = tk.Entry(login_container, width=25)
        self.username_entry.grid(row=1, column=1, pady=10)
        
        # Password
        password_label = tk.Label(login_container, text="Password:")
        password_label.grid(row=2, column=0, sticky="e", padx=(0, 10), pady=10)
        self.password_entry = tk.Entry(login_container, show="*", width=25)
        self.password_entry.grid(row=2, column=1, pady=10)
        
        # Pulsante Login
        login_button = tk.Button(login_container, text="Accedi", 
                                command=self.attempt_login, width=15)
        login_button.grid(row=3, column=0, columnspan=2, pady=(30, 0))
        
    def attempt_login(self):
        """Tenta il login con le credenziali inserite."""
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.controller.login(username, password)


class SearchTableFrame(tk.Frame):
    """Frame con una barra di ricerca e una tabella."""
    
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.is_admin_view = False
        
        # Area superiore per la ricerca
        search_frame = tk.Frame(self, padx=20, pady=20)
        search_frame.pack(fill="x")
        
        # Etichetta di benvenuto e logout
        welcome_frame = tk.Frame(search_frame)
        welcome_frame.pack(fill="x", pady=(0, 20))
        
        welcome_label = tk.Label(welcome_frame, text="Benvenuto nella pagina principale", 
                               font=controller.title_font)
        welcome_label.pack(side="left")
        
        logout_button = tk.Button(welcome_frame, text="Logout", 
                                command=self.logout)
        logout_button.pack(side="right")
        
        # Barra di ricerca
        search_container = tk.Frame(search_frame)
        search_container.pack(fill="x")
        
        search_label = tk.Label(search_container, text="Cerca:")
        search_label.pack(side="left", padx=(0, 10))
        
        self.search_entry = tk.Entry(search_container, width=40)
        self.search_entry.pack(side="left", padx=(0, 10))
        
        search_button = tk.Button(search_container, text="Cerca", 
                                 command=self.search_records)
        search_button.pack(side="left")

        reset_button = tk.Button(search_container, text="Reset",
                                 command=self.reset_table)
        reset_button.pack(side="left")
        
        # Salva modifiche (visibile solo per admin)
        self.save_button = tk.Button(search_container, text="Salva Modifiche",
                                command=self.save_changes, state=tk.DISABLED)
        self.save_button.pack(side="right", padx=(10, 0))
        
        # Area per la tabella
        table_frame = tk.Frame(self, padx=20, pady=20)
        table_frame.pack(fill="both", expand=True)
        
        # Crea la tabella (Treeview)
        self.columns = ("band_name", "track_name", "track_duration", "hour_track", "time_before", "time_after")
        self.admin_columns = self.columns + ("order_controls",)
        
        self.table = ttk.Treeview(table_frame, columns=self.columns, show="headings")
        
        # Definisci le intestazioni
        self.table.heading("band_name", text="Nome Band")
        self.table.heading("track_name", text="Nome Traccia")
        self.table.heading("track_duration", text="Durata Traccia")
        self.table.heading("hour_track", text="Orario Esecuzione")  # Aggiungi questa riga
        self.table.heading("time_before", text="Tempo Prima")
        self.table.heading("time_after", text="Tempo Dopo")        
        # Definisci larghezza colonne
        self.table.column("band_name", width=130)
        self.table.column("track_name", width=150)
        self.table.column("track_duration", width=100)
        self.table.heading("hour_track", width=100)
        self.table.column("time_before", width=100)
        self.table.column("time_after", width=100)
        
        # Aggiungi scrollbar
        scrollbar_y = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        scrollbar_x = ttk.Scrollbar(table_frame, orient="horizontal", command=self.table.xview)
        self.table.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        
        # Posiziona tabella e scrollbar
        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x.pack(side="bottom", fill="x")
        self.table.pack(side="left", fill="both", expand=True)
        
        # Frame per i pulsanti di ordinamento
        self.buttons_frame = tk.Frame(table_frame)
        self.buttons_frame.pack(side="right", fill="y")
        
        # Popola la tabella con dati del json
        self.populate_table()
        
        # Bind eventi di selezione della tabella
        self.table.bind("<<TreeviewSelect>>", self.on_select)
        
    def logout(self):
        """Effettua il logout dell'utente corrente."""
        self.controller.current_user = None
        self.controller.show_frame(LoginFrame)
        
    def on_select(self, event):
        """Gestisce l'evento di selezione della tabella."""
        if not self.is_admin_view:
            return
            
        selected_items = self.table.selection()
        if not selected_items:
            return
            
        # Aggiorna i pulsanti di ordinamento
        self.update_order_buttons(selected_items[0])
    
    def update_order_buttons(self, selected_item):
        """Aggiorna i pulsanti di ordinamento per la riga selezionata."""
        # Rimuovi i vecchi pulsanti
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()
            
        # Ottieni l'indice dell'elemento selezionato
        index = self.table.index(selected_item)
        item_id = self.get_item_id_from_index(index)
        
        # Crea nuovi pulsanti
        up_button = tk.Button(self.buttons_frame, text="▲", 
                            command=lambda: self.move_item_up(item_id))
        up_button.pack(pady=5)
        
        down_button = tk.Button(self.buttons_frame, text="▼", 
                               command=lambda: self.move_item_down(item_id))
        down_button.pack(pady=5)
        
        # Disabilita i pulsanti se necessario
        if index == 0:
            up_button.config(state=tk.DISABLED)
        if index == len(self.all_data) - 1:
            down_button.config(state=tk.DISABLED)
    
    def get_item_id_from_index(self, index):
        """Ottiene l'ID dell'elemento dalla sua posizione nell'elenco."""
        return self.all_data[index]["order"]
    
    def move_item_up(self, item_id):
        """Sposta un elemento una posizione in su."""
        self.move_item(item_id, -1)
        
    def move_item_down(self, item_id):
        """Sposta un elemento una posizione in giù."""
        self.move_item(item_id, 1)
        
    def move_item(self, item_id, direction):
        """Sposta un elemento nella direzione specificata."""
        # Trova l'indice dell'elemento con l'ID specificato
        current_index = None
        for i, item in enumerate(self.all_data):
            if item["order"] == item_id:
                current_index = i
                break
                
        if current_index is None:
            return
            
        # Calcola il nuovo indice
        new_index = current_index + direction
        
        # Verifica che il nuovo indice sia valido
        if new_index < 0 or new_index >= len(self.all_data):
            return
            
        # Scambia gli elementi
        self.all_data[current_index], self.all_data[new_index] = self.all_data[new_index], self.all_data[current_index]
        
        # IMPORTANTE: Rinumera gli order in base alla nuova posizione
        for i, item in enumerate(self.all_data):
            item["order"] = i + 1
        
        # Aggiorna la tabella
        self.refresh_table()
        
        # Attiva il pulsante di salvataggio
        self.save_button.config(state=tk.NORMAL) 
        
    def refresh_table(self):
        """Aggiorna la tabella con i dati correnti."""
        # Cancella dati esistenti
        for i in self.table.get_children():
            self.table.delete(i)
            
        # Ordina lineup per order
        sorted_data = json_fun.sort_lineup(self.all_data)
        
        # Inserisci dati nella tabella
        for item in sorted_data:
            # Calcola l'orario di esecuzione del brano
            hour_track = json_fun.when_track(sorted_data, item["track_name"])
            
            values = (
                item.get("band_name", ""),
                item.get("track_name", ""),
                item.get("track_duration", ""),
                hour_track,  # Aggiungo l'orario calcolato
                item.get("time_before", "N/A"),
                item.get("time_after", "N/A")
            )
            self.table.insert("", "end", values=values)
    def update_table_for_user(self, is_admin):
        """Aggiorna la tabella in base ai privilegi dell'utente."""
        self.is_admin_view = is_admin
        
        # Mostra/nascondi pulsante di salvataggio
        if is_admin:
            self.save_button.config(state=tk.DISABLED)  # Disabilitato finché non ci sono modifiche
            self.save_button.pack(side="right", padx=(10, 0))
            self.buttons_frame.pack(side="right", fill="y")
        else:
            self.save_button.pack_forget()
            self.buttons_frame.pack_forget()
            
        # Aggiorna la tabella
        self.populate_table()
    
    def populate_table(self):
        """Popola la tabella con dati del json."""
        # Cancella dati esistenti
        for i in self.table.get_children():
            self.table.delete(i)
            
        # Importa dati da JSON
        lineup = json_fun.open_json()

        # Ordina lineup per order
        sorted_lineup = json_fun.sort_lineup(lineup)
        
        # Inserisci dati nella tabella
        for item in sorted_lineup:
            # Verifica che l'elemento abbia tutti i campi necessari
            if "band_name" not in item or "track_name" not in item or "track_duration" not in item:
                continue
            
            # Calcola l'orario di esecuzione del brano
            hour_track = json_fun.when_track(sorted_lineup, item["track_name"])
                
            values = (
                item.get("band_name", ""),
                item.get("track_name", ""),
                item.get("track_duration", ""),
                hour_track,  # Aggiungo l'orario calcolato
                item.get("time_before", "N/A"),
                item.get("time_after", "N/A")
            )
            self.table.insert("", "end", values=values)
        
        # Salva i dati originali per la funzionalità di ricerca
        self.all_data = sorted_lineup
    def search_records(self):
        """Cerca record nella tabella."""
        search_term = self.search_entry.get().lower()
        
        # Cancella dati esistenti
        for i in self.table.get_children():
            self.table.delete(i)
        
        # Se non c'è termine di ricerca, mostra tutti i dati
        if not search_term:
            for record in self.all_data:
                # Calcola l'orario di esecuzione del brano
                hour_track = json_fun.when_track(self.all_data, record["track_name"])
                
                values = (
                    record.get("band_name", ""),
                    record.get("track_name", ""),
                    record.get("track_duration", ""),
                    hour_track,  # Aggiungo l'orario calcolato
                    record.get("time_before", "N/A"),
                    record.get("time_after", "N/A")
                )
                self.table.insert("", "end", values=values)
            return
            
        # Altrimenti filtra i dati
        for record in self.all_data:
            # Converte tutti i valori in stringhe e controlla se il termine di ricerca è presente
            if any(search_term in str(value).lower() for value in record.values()):
                # Calcola l'orario di esecuzione del brano
                hour_track = json_fun.when_track(self.all_data, record["track_name"])
                
                values = (
                    record.get("band_name", ""),
                    record.get("track_name", ""),
                    record.get("track_duration", ""),
                    hour_track,  # Aggiungo l'orario calcolato
                    record.get("time_before", "N/A"),
                    record.get("time_after", "N/A")
                )
                self.table.insert("", "end", values=values)
    def reset_table(self):
        """Resetta la tabella allo stato originale."""
        self.search_entry.delete(0, tk.END)  # Cancella il testo di ricerca
        self.populate_table()  # Ricarica tutti i dati
        
    def save_changes(self):
        """Salva le modifiche apportate all'ordine."""
        try:
            # Salva le modifiche nel file JSON
            json_fun.save_lineup(self.all_data)
            messagebox.showinfo("Successo", "Modifiche salvate con successo!")
            self.save_button.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Errore", f"Impossibile salvare le modifiche: {str(e)}")


if __name__ == "__main__":
    app = LoginTableApp()
    app.mainloop()