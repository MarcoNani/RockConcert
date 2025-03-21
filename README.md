# Relazione gestione attività concerto rock

## Organizzazione concerto rock
Si vuole organizzare un concerto rock. Dopo un'analisi delle attività necessarie si è stabilito che per la realizzazione di quest'ultimo sono necessarie le attività illustrate di seguito nel diagramma di Gantt.
![Diagramma di Gantt](./Parte%20progettuale/Gantt.png)
> In arancione sono evidenziate le attività critiche

### Numero minimo di giorni necessari per l'organizzazione
Analizzando il diagramma di Gantt abbiamo stabilito che il numero minimo di giorni necessari per l'organizzazione del concerto rock sono ***17 giorni***.

### Attvità che incrementano la durata del progetto
Analizzando ulteriormente il diagramma abbiamo stabilito che le attività che incrementano la data del progetto sarebbero le seguenti:
1. Individuazione del sito
2. Assunzione del personale
4. Dettagli ultimo minuto
6. Affitto apparecchiature
7. Prove generali
8. Preparazione dei trasporti
9. Installazione impianto acustico

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

L'applicazione all'avvio mostra una maschera per farsi riconoscere dal sistema. Una volta autenticati viene mostrata la scaletta del concerto e si ha la possibilità di effettuare il CRUD sulle tracce (se si è organizzatori).

È possibile riordinare le tracce con la pressione dei relativi tasti, cercare una traccia tramite Autore, titolo ecc... all'interno della scaletta e modificare i dettagli di queste ultime.
Le tracce vengono lette e salvate su disco tramite un file JSON.
Il programma permette infine di stampare su un file o su carta l'elenco delle tracce.

Su MacOS il programma è disponibile in modalità chiara e modalità scura.

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