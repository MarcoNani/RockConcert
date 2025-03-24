# Relazione gestione attività concerto rock

## Organizzazione concerto rock
Si vuole organizzare un concerto rock. Dopo un'analisi delle attività necessarie si è stabilito che per la realizzazione di quest'ultimo sono necessarie le attività illustrate di seguito nel diagramma di Gantt.
![Diagramma di Gantt](./Parte%20progettuale/Gantt.png)
> In arancione sono evidenziate le attività critiche

### Numero minimo di giorni necessari per l'organizzazione
Analizzando il diagramma di Gantt abbiamo stabilito che il numero minimo di giorni necessari per l'organizzazione del concerto rock sono ***17 giorni***.

### Attvità che incrementano la durata del progetto
Analizzando ulteriormente il diagramma abbiamo stabilito che le attività che incrementano la data del progetto sarebbero le seguenti:
- Individuazione del sito
- Assunzione del personale
- Dettagli ultimo minuto
- Affitto apparecchiature
- Prove generali
- Preparazione dei trasporti
- Installazione impianto acustico

### Cosa succede se la tipografia consegna i volantini in ritardo
Abbiamo inoltre analizzato cosa succede se la tipografia consegna i volantini in ritardo (la durata dell'attività va da 5 a 9 giorni):

![Diagramma di Gantt con tipografia in ritardo](./Parte%20progettuale/Print%20delay.png)

Se la tipografia consegna in ritardo i volantini e si considera la stampa dei volantini come un'attività fondamentale per la buona riuscita del concerto rock (non era stata considerata tale nell'analisi iniziale) bisognerà posticipare il giorno del concerto di minimo un giorno (se si considera accettabile il fatto di distribuire i volantini il giorno prima) probabilmente si posticiperà invece il concerto di 4/5 giorni (considerando anche il fatto che bisognerà considerare un finesettimana in più).

## Applicazione gestione scaletta concerto
Abbiamo realizzato una applicazione per gestire la scaletta del concerto in Python compatibile sia con Windows che con MacOS.

## Features

### Use case diagram
L'applicazione permette di svolgere le attività mostrate nello use case diagram quì riportato:
![Use case diagram](./Programma%20Python/UML_ITA.jpeg)


L'applicazione permete quindi l'accesso a due tipologie di utenti:
- Organizzazione
- Membro dello staff

I primi hanno i privilegi necessari per eseguire il CRUD sulle tracce mentre i membri dello staf possono solamente visualizzare e stampare la scaletta del concerto.

### Schermata di Login
> L'applicazione all'avvio mostra una maschera per farsi riconoscere dal sistema.  
![Empty login](./Programma%20Python/screenshots/1-login_vuoto.png)

> Una volta autenticati, viene mostrata la schermata di login per l'admin.  
![Admin login](./Programma%20Python/screenshots/2-login_admin.png)

L'applicazione all'avvio mostra una maschera per farsi riconoscere dal sistema. Una volta autenticati viene mostrata la scaletta del concerto e si ha la possibilità di effettuare il CRUD sulle tracce (se si è organizzatori).

### Vista dell'App per Admin
> Dopo l'accesso, gli organizzatori possono visualizzare e modificare la scaletta del concerto.  
![Admin app view](./Programma%20Python/screenshots/3-app_admin.png)


È possibile riordinare le tracce con la pressione dei relativi tasti, cercare una traccia tramite Autore, titolo ecc... all'interno della scaletta e modificare i dettagli di queste ultime.

### Funzionalità di Ricerca
> È possibile cercare una traccia tramite autore, titolo, ecc., all'interno della scaletta.  
![Search](./Programma%20Python/screenshots/4-search.png)

### Modifica dell'Ordine delle Tracce
> Gli organizzatori possono riordinare le tracce con la pressione dei relativi tasti.  
![Modify track order](./Programma%20Python/screenshots/5-modify.png)

> Esempio di spostamento di una traccia verso l'alto o verso il basso.  
![Moving track](./Programma%20Python/screenshots/6-moving_track.png)

> Conferma visiva di una modifica completata con successo.  
![Moving track successfully](./Programma%20Python/screenshots/7-successful_modification.png)

Le tracce vengono lette e salvate su disco tramite un file JSON.

#### Possibilità di stampare la scaletta
> Grazie a due librerie diverse, è possibile selezionare una stampante e avviare una stampa della scaletta direttamente dalla applicazione!
![Stampa Scaletta](./Programma%20Python/screenshots/13-print.png)
![Stampa riuscita](./Programma%20Python/screenshots/14-print_successful.png)

### Vista dell'App per Utenti
> Gli utenti dello staff possono accedere con una schermata dedicata.  
![User login](./Programma%20Python/screenshots/9-login_user.png)

> Se sbaglia le credenziali l'utente viene avvisato
![Credenziali incorrette](./Programma%20Python/screenshots/8-incorrect_login.png)

> Dopo l'accesso, gli utenti possono visualizzare la scaletta del concerto.  
![User view app](./Programma%20Python/screenshots/10-user_app.png)

Il programma permette infine di stampare su un file o su carta l'elenco delle tracce.

### Modalità Scura
> L'applicazione supporta la modalità scura su MacOS.  
![App in dark mode](./Programma%20Python/screenshots/12-dark_mode.png)

### Work Breakdown Structure (WBS):
Quì sotto è riportato il Work Breakdown Structure dell'applicazione:

- Memorizzazzione tracce
    - Salvataggio dati su file
    - Lettura dati da file
- Gestione account
    - Divisione ruoli
    - Autenticazione
- CRUD tracce
    - Aggiungi traccia
    - Aggiorna dettagli traccia
    - Rimuovi traccia
    - Lettura dettagli scaletta
        - Stampa su file/stampante
        - Stampa su schermo