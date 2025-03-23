import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkfont
import json_fun
import print

DATI_JSON = "Nessun dato letto da json"

class LoginTableApp(tk.Tk):
    """Applicazione principale con sistema di navigazione tra frame."""
    
    def __init__(self):
        super().__init__()
        self.title("Login & Tabella App")
        self.geometry("800x600")
        
        # Dizionario utenti (in un'app reale, dovrebbe essere un database)
        self.users = {"admin": "password123", "user": "password"}
        
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
            self.show_frame(SearchTableFrame)
            return True
        else:
            messagebox.showerror("Errore", "Nome utente o password non validi!")
            return False


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
                                command=lambda: controller.show_frame(LoginFrame))
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

        reset_button = tk.Button(search_container, text = "Reset",
                                 command=self.reset_table)
        
        reset_button.pack(side="left")
        
        # Aggiungi pulsante per stampare la lineup
        print_button = tk.Button(search_container, text="Stampa Lineup", 
                                 command=self.print_lineup)
        print_button.pack(side="left", padx=(10, 0))
        
        # Area per la tabella
        table_frame = tk.Frame(self, padx=20, pady=20)
        table_frame.pack(fill="both", expand=True)
        
        # Crea la tabella (Treeview)
        columns = ("band_name", "track_name", "track_duration", "time_before", "time_after")
        self.table = ttk.Treeview(table_frame, columns=columns, show="headings")
        
        # Definisci le intestazioni
        self.table.heading("band_name", text="Nome Band")
        self.table.heading("track_name", text="Nome Traccia")
        self.table.heading("track_duration", text="Durata Traccia")
        self.table.heading("time_before", text="Tempo Prima")
        self.table.heading("time_after", text="Tempo Dopo")
        
        # Definisci larghezza colonne
        self.table.column("band_name", width=130)
        self.table.column("track_name", width=150)
        self.table.column("track_duration", width=100)
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
        
        # Popola la tabella con dati del json
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
            values = (
                item["band_name"],
                item["track_name"],
                item["track_duration"],
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
        # Removed the bad return statement that was causing the search to only return the first match
    
    def reset_table(self) :
        # Cancella tutti i dati esistenti nella tabella e nella searchbox
        for i in self.table.get_children():
            self.table.delete(i)
        self.search_entry.delete(0, tk.END)
        # Popola la tabella dei dati
        for record in self.all_data:
                values = (
                    record["band_name"],
                    record["track_name"],
                    record["track_duration"],
                    record.get("time_before", "N/A"),
                    record.get("time_after", "N/A")
                )
                self.table.insert("", "end", values=values)
    
    def print_lineup(self):
        """Stampa la lineup del concerto."""
        # Genera il testo da stampare
        text_to_print = "Lineup del Concerto:\n\n"
        text_to_print += f"{'Band Name':<30} {'Track Name':<30} {'Track Duration':<15} {'Time Before':<15} {'Time After':<15}\n"
        text_to_print += "-" * 105 + "\n"
        for record in self.all_data:
            text_to_print += (
            f"{record['band_name']:<30} "
            f"{record['track_name']:<30} "
            f"{record['track_duration']:<15} "
            f"{record.get('time_before', 'N/A'):<15} "
            f"{record.get('time_after', 'N/A'):<15}\n"
            )
        
        # Usa la funzione di stampa
        print.print_to_whatever(text_to_print)

if __name__ == "__main__":
    app = LoginTableApp()
    app.mainloop()