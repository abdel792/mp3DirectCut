# mp3DirectCut

* Autore/i: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS.

# Presentazione #

Questo componente aggiuntivo migliora l'accessibilità del software mp3DirectCut con NVDA.

È stato testato con versioni di mp3DirectCut che vanno dalla 212 fino alla 233.

## Scorciatoie da tastiera ##

Questo componente aggiuntivo offre i seguenti comandi:

* B

    * Utilizzato per confermare il corretto posizionamento del marcatore dell'inizio della selezione B.

* Ctrl+Shift+B

    * Utilizzato per indicare la posizione del marcatore dell'inizio della selezione B.
    * Una doppia pressione consente di ottenere la durata della selezione.

* Ctrl+Shift+D

    * Fornisce la durata dall'inizio del file fino alla posizione attuale del cursore di riproduzione.
    * Una doppia pressione consente di ottenere la durata totale.

* Ctrl+R

    * Conferma che la selezione è stata annullata.

* Ctrl+Shift+R

    * Fornisce il tempo rimanente dalla posizione attuale del cursore di riproduzione fino alla fine del file.

* Ctrl+Shift+E

    * Utilizzato per indicare la posizione del marcatore della fine della selezione N.
    * Una doppia pressione fornisce un riepilogo delle posizioni B e N, e la durata della selezione.

* Ctrl+Shift+P

    * Fornisce il riferimento della parte corrente e il numero totale di parti nel file corrente.

* Ctrl+Shift+Space

    * Utilizzato per determinare il livello attuale del vu-meter, durante la registrazione.
    * Una doppia pressione lo azzera.

* Freccia Giù

    * Consente di visualizzare la posizione attuale del cursore di riproduzione.
    * Questo comando posiziona anche il cursore nella posizione del marcatore della fine della selezione N, fornendo la posizione di questo marcatore se è stata effettuata una selezione.
    * Nella finestra di dialogo del volume, vocalizza il valore successivo che può essere raggiunto generalmente con frecciaGiù.
    * Questo valore non viene vocalizzato per impostazione predefinita.

* End

    * Sposta il cursore di riproduzione alla fine del file corrente e fornisce il tempo totale.

* Home

    * Sposta il cursore di riproduzione all'inizio del file corrente.

* Freccia Sinistra

    * Consente di effettuare un breve ritorno indietro di un secondo durante la riproduzione, fornendo la durata corrente.
    * Questa durata è configurabile nelle opzioni di mp3DirectCut.

* N

    * Utilizzato per confermare il corretto posizionamento del marcatore della fine della selezione N.

* Page Down

    * Consente di fare un salto in avanti di 10 secondi durante la riproduzione, fornendo la durata corrente.
    * Questa durata è configurabile nelle opzioni di mp3DirectCut.

* Page Up

    * Consente di fare un ritorno indietro di 10 secondi durante la riproduzione, fornendo la durata corrente.
    * Questa durata è configurabile nelle opzioni di mp3DirectCut.

* R

    * Consente di preparare una registrazione e di sapere se è possibile premere la barra spaziatrice per iniziare.

* Freccia Destra

    * Consente di effettuare un breve avanzamento di un secondo durante la riproduzione, fornendo la durata corrente.
    * Questa durata è configurabile nelle opzioni di mp3DirectCut.

* Ctrl+Freccia Destra

    * Sposta al punto di divisione successivo, fornendo la durata corrente.

* Ctrl+Freccia Sinistra

    * Sposta al punto di divisione precedente, fornendo la durata corrente.

* Shift+Freccia Destra

    * Consente di effettuare un breve avanzamento di quattro centesimi di secondo durante la riproduzione, fornendo la durata corrente.

* Shift+Freccia Sinistra

    * Consente di effettuare un breve ritorno indietro di quattro centesimi di secondo durante la riproduzione, fornendo la durata corrente.

* S

    * Utilizzato per interrompere la riproduzione e fornire la durata corrente.

* Space

    * Se la registrazione è pronta, avvia questa registrazione.
    * Se una registrazione è in corso, la interrompe posizionando il cursore all'inizio.
    * Se un file è caricato, avvia la riproduzione.
    * Se una riproduzione è in corso, consente di mettere in pausa fornendo la durata corrente.
    * Se la riproduzione è in pausa, consente di riavviare la riproduzione dalla posizione corrente.

* Freccia Su

    * Consente di visualizzare la posizione attuale del cursore di riproduzione.
    * Questo comando posiziona anche il cursore nella posizione del marcatore dell'inizio della selezione B, fornendo la posizione di questo marcatore se è stata effettuata una selezione.
    * Nella finestra di dialogo del volume, vocalizza il valore precedente che può essere raggiunto generalmente con frecciaSu.
    * Questo valore non viene vocalizzato per impostazione predefinita.

* NVDA+H

    * Consente di aprire la guida del componente aggiuntivo corrente.

## Compatibilità ##

* Questo componente aggiuntivo è compatibile con le versioni di NVDA a partire dalla 2019.3 e successive.

## Modifiche per 20240327.0.0

* Corretto un bug che causava un errore di registro durante il ricaricamento dei plugin, grazie a Rob, dalla mailing list nvda-addons;

## Modifiche per 20240326.0.0

* Aggiornata la compatibilità per nvda-2024.1.;
* Eliminato il link per il download dal file readme, il link per il download dei futuri aggiornamenti sarà ora disponibile solo dall'add-on store.

## Modifiche per 20231229.0.0 ##

* Aggiunta un'implementazione retrocompatibile per supportare la modalità di sintesi vocale su richiesta, che sarà presto disponibile con nvda-2024.1.

## Modifiche per 20231007.0.0 ##

* Dopo aver posizionato i punti di taglio e dopo aver aperto la finestra delle proprietà di taglio con "Ctrl+N", è stata aggiunta l'accessibilità al titolo di questa finestra indicando l'indice della parte.
* In modalità lettura, dopo aver spostato i marcatori di inizio o fine selezione con i tasti da 1 a 6 del tastierino alfanumerico, è stato aggiunto l'avvio automatico della lettura dalla nuova posizione;
* Corretto un bug che si verificava quando si consultava il tempo rimanente con "control+shift+r" dall'inizio della traccia.

## Modifiche per 20230728.0.0 ##

* Applicate le regole flake8 e mypy al codice;
* Modificata la versione minima di NVDA supportata alla 2019.3 per supportare le annotazioni introdotte in Python 3.

## Modifiche per 20230607.0.0 ##

* Aggiunti i seguenti flussi di lavoro:
 * auto-update-translations - per aggiornare automaticamente le traduzioni dal sistema di traduzione di NVDA.
 * release-on-tag..yaml: per compilare e pubblicare l'add-on non appena viene inviato un nuovo tag;
 * manual-release.yaml: per compilare e rilasciare manualmente nuove versioni del componente aggiuntivo.
* Traduzioni aggiornate.

## Modifiche per la versione 20230508.0.0 e successive ##

* Modificati il numero di versione, la versione minima di NVDA e il link per il download in base alle convenzioni/requisiti dello store.

## Modifiche per la versione 20.12 ##

* Interruzione della sintesi vocale durante la registrazione e la lettura per le ultime versioni di mp3DirectCut;
* Corretta la lettura del tempo rimanente per le nuove versioni di NVDA che utilizzano Python 3.

## Modifiche per la versione 19.02 ##

* Aggiunta la configurazione del componente aggiuntivo nel pannello delle impostazioni disponibile da nvda 2018.2;
* Modificata la numerazione delle versioni utilizzando AA.MM (l'anno in 2 cifre, seguito da un punto, seguito dal mese in 2 cifre);
* Aggiunta la compatibilità con il nuovo formato di numerazione delle versioni dei componenti aggiuntivi, apparso a partire da nvda 2019.1.

## Modifiche per la versione 4.0 ##

* Aggiunta la compatibilità del componente aggiuntivo sia con Python 2.7 che con 3;
* Corretto un bug con i percorsi dei componenti aggiuntivi che contengono caratteri non ASCII.

## Modifiche per la versione 3.0 ##

* Utilizzato il modulo gui.guiHelper per garantire il corretto aspetto della finestra di dialogo di configurazione dell'add-on;
* Utilizzato format invece di %s per le stringhe formattate;
* Utilizzata la conformità alle linee guida per l'implementazione.

## Modifiche per la versione 2.3 ##

* Aggiunta la licenza GPL al componente aggiuntivo;
* Modificata la scorciatoia dello script che fornisce la fine della selezione da Ctrl + Shift + N a Ctrl + Shift + E perché Ctrl + Shift + N non funziona con le ultime versioni di mp3DirectCut;
* Aggiunto uno script per confermare che la selezione è stata annullata con 'Ctrl+r';
* Apportate alcune correzioni nel codice dell'appModule 'mp3directcut.py'.

## Modifiche per la versione 2.2 ##

* Correzione degli script che forniscono le posizioni dei marcatori di selezione.

## Modifiche per la versione 2.1.1 ##

* Rimozione dello script che fornisce il tempo totale e aggiunta di questa informazione allo script che fornisce il tempo trascorso;
* Aggiunta la possibilità di abilitare o disabilitare gli annunci relativi al tasto spazio nelle opzioni di configurazione del modulo, separatamente dagli altri annunci;
* Aggiunta la possibilità di abilitare o disabilitare l'annuncio del posizionamento dei marcatori di selezione nelle opzioni di configurazione del modulo;
* Aggiunta dell'annuncio della parte corrente quando ci si sposta attraverso i punti di taglio;
* Correzione degli annunci relativi ai tasti verticali;
* Aggiunta di uno script per aprire la guida del componente aggiuntivo corrente con 'NVDA+H';
* Spostamento del menu di configurazione del componente aggiuntivo dal menu Strumenti al menu Preferenze di NVDA.

## Modifiche per la versione 2.1 ##

* Aggiunta di uno script per vocalizzare lo spostamento al punto di divisione successivo con Control+Freccia Destra;
* Aggiunta di uno script per vocalizzare lo spostamento al punto di divisione precedente con Control+Freccia Sinistra;
* Aggiunta di uno script per vocalizzare lo spostamento di 4 centesimi di secondo in avanti, con Shift+Freccia Destra;
* Aggiunta di uno script per vocalizzare lo spostamento di 4 centesimi di secondo indietro, con Shift+Freccia Sinistra;
* Correzione del riepilogo del componente aggiuntivo da 'for mp3DirectCut' a 'mp3DirectCut'.

## Modifiche per la versione 2.0 ##

* Aggiunta di uno script per conoscere il tempo rimanente con 'Control Shift R';
* Corretta la lettura delle durate che includono le ore;
* Aggiunta la capacità di differenziare i millesimi o i centesimi di secondo.

## Modifiche per la versione 1.1 ##

* Aggiunta la possibilità di includere la categoria mp3DirectCut nei Gesti di Input;

    * Saranno visibili solo durante l'uso del software mp3DirectCut.

* Aggiunta la possibilità di abilitare o disabilitare i messaggi automatici, nel menu degli strumenti di NVDA, voce 'Configurazione di mp3DirectCut';

## Modifiche per la versione 1.0 ##

* Versione iniziale.
