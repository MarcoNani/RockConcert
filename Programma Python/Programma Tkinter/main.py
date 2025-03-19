import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkfont

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
        
        # Area per la tabella
        table_frame = tk.Frame(self, padx=20, pady=20)
        table_frame.pack(fill="both", expand=True)
        
        # Crea la tabella (Treeview)
        columns = ("id", "nome", "cognome", "email", "telefono")
        self.table = ttk.Treeview(table_frame, columns=columns, show="headings")
        
        # Definisci le intestazioni
        self.table.heading("id", text="ID")
        self.table.heading("nome", text="Nome")
        self.table.heading("cognome", text="Cognome")
        self.table.heading("email", text="Email")
        self.table.heading("telefono", text="Telefono")
        
        # Definisci larghezza colonne
        self.table.column("id", width=50)
        self.table.column("nome", width=100)
        self.table.column("cognome", width=100)
        self.table.column("email", width=200)
        self.table.column("telefono", width=120)
        
        # Aggiungi scrollbar
        scrollbar_y = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        scrollbar_x = ttk.Scrollbar(table_frame, orient="horizontal", command=self.table.xview)
        self.table.configure(yscrollcommand=scrollbar_y.set, xscrollcommand=scrollbar_x.set)
        
        # Posiziona tabella e scrollbar
        scrollbar_y.pack(side="right", fill="y")
        scrollbar_x.pack(side="bottom", fill="x")
        self.table.pack(side="left", fill="both", expand=True)
        
        # Popola la tabella con dati di esempio
        self.populate_table()
    
    def populate_table(self):
        """Popola la tabella con dati di esempio."""
        # Cancella dati esistenti
        for i in self.table.get_children():
            self.table.delete(i)
            
        # Dati di esempio
        sample_data = [
            (1, "Mario", "Rossi", "mario.rossi@example.com", "333-1234567"),
            (2, "Luigi", "Verdi", "luigi.verdi@example.com", "333-7654321"),
            (3, "Anna", "Bianchi", "anna.bianchi@example.com", "333-9876543"),
            (4, "Giulia", "Neri", "giulia.neri@example.com", "333-3456789"),
            (5, "Marco", "Gialli", "marco.gialli@example.com", "333-5678901"),
            (6, "Laura", "Bruno", "laura.bruno@example.com", "333-1122334"),
            (7, "Roberto", "Ferrari", "roberto.ferrari@example.com", "333-5566778"),
            (8, "Sofia", "Esposito", "sofia.esposito@example.com", "333-9988776"),
            (9, "Andrea", "Russo", "andrea.russo@example.com", "333-1234987"),
            (10, "Chiara", "Romano", "chiara.romano@example.com", "333-6543219"),
        ]
        
        # Inserisci dati nella tabella
        for record in sample_data:
            self.table.insert("", "end", values=record)
        
        # Salva i dati originali per la funzionalità di ricerca
        self.all_data = sample_data
    
    def search_records(self):
        """Cerca record nella tabella."""
        search_term = self.search_entry.get().lower()
        
        # Cancella dati esistenti
        for i in self.table.get_children():
            self.table.delete(i)
        
        # Se non c'è termine di ricerca, mostra tutti i dati
        if not search_term:
            for record in self.all_data:
                self.table.insert("", "end", values=record)
            return
            
        # Altrimenti filtra i dati
        for record in self.all_data:
            # Converte tutti i valori in stringhe e controlla se il termine di ricerca è presente
            if any(search_term in str(value).lower() for value in record):
                self.table.insert("", "end", values=record)


if __name__ == "__main__":
    app = LoginTableApp()
    app.mainloop()