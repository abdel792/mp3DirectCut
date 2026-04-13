# mp3DirectCut #

* Author(s) : Abdel, Rémy, Abdellah zineddine, Jean-François COLAS.

# Presentazione #

Questo add-on migliora l'accessibilità del programma mp3DirectCut con NVDA.

E' stato testato con le versioni di mp3DirectCut dalla 212 alla 223.

## Comandi da tastiera ##

Questo add-on offre i seguenti comandi:

* B

    * Utilizzato per confermare il corretto posizionamento del marcatore di
      inizio della selezione B.

* Ctrl+Shift+B

    * Utilizzato per indicare la posizione del marcatore di inizio della
      selezione B.
    * Una doppia pressione del tasto consente di conoscere la durata della
      selezione.

* Ctrl+Shift+D

    * Fornisce la durata dell'area tra l'inizio del file e la posizione
      corrente del cursore di riproduzione.
    * Se premuto due volte, legge la durata totale.

* Ctrl+R

    * Conferma che la selezione è stata annullata.

* Ctrl+Shift+R

    * Fornisce il tempo rimanente dalla posizione corrente del cursore di
      riproduzione fino alla fine del file.

* Ctrl+Shift+E

    * Utilizzato per indicare la posizione del marcatore di fine selezione
      N.
    * La doppia pressione fornisce un riepilogo delle posizioni B e N e la
      durata della selezione.

* Ctrl+Shift+P

    * Dà un riscontro sulla parte attuale e sul numero di parti nel file in
      uso.

* Ctrl+Shift+Spazio

    * Utilizzato per determinare il livello attuale del vu-meter, durante la
      registrazione.
    * La doppia pressione lo resetta.

* Freccia giù

    * Mostra la posizione attuale della testina di riproduzione.
    * Se è stata fatta una selezione, inoltre, questo comando sposta il
      cursore sul marcatore di fine della selezione N, fornendone la
      posizione.
    * Nella finestra di dialogo Volume, vocalizza il valore successivo che
      può essere raggiunto generalmente con freccia giù.
    * Questo valore non è vocalizzato per default.

* End

    * Sposta il cursore di riproduzione alla fine del file corrente e ne
      fornisce la durata totale.

* Home

    * Sposta il cursore di riproduzione all'inizio del file corrente.

* Freccia sinistra

    * Torna indietro di un secondo durante l'ascolto, fornendo il nuovo
      tempo di riproduzione.
    * Tale tempo è configurabile nelle opzioni di mp3directcut.

* N

    * Utilizzato per confermare il corretto posizionamento del marcatore di
      fine della selezione N.

* Pagina giù

    * Va avanti di 10 secondi durante l'ascolto, fornendo il nuovo tempo di
      riproduzione.
    * Tale tempo è configurabile nelle opzioni di mp3directcut.

* Pagina su

    * Va indietro di 10 secondi durante l'ascolto, fornendo il nuovo tempo
      di riproduzione.
    * Tale tempo è configurabile nelle opzioni di mp3directcut.

* R

    * Consente di preparare una registrazione; premete spazio per avviarla.

* Freccia destra

    * Va avanti di un secondo durante l'ascolto, fornendo il nuovo tempo di
      riproduzione.
    * Tale tempo è configurabile nelle opzioni di mp3directcut.

* Ctrl+Freccia destra

    * Sposta al punto di taglio successivo, fornendone il tempo di
      riproduzione.

* Ctrl+Freccia sinistra

    * Sposta al punto di taglio precedente, fornendone il tempo di
      riproduzione.

* Shift+Freccia destra

    * Va avanti di 4 centesimi di secondo durante l'ascolto, fornendo il
      nuovo tempo di riproduzione.

* Shift+Freccia sinistra

    * Va indietro di 4 centesimi di secondo durante l'ascolto, fornendo il
      nuovo tempo di riproduzione.

* S

    * Utilizzato per interrompere l'ascolto e fornire il tempo di
      riproduzione attuale.

* Spazio

    * Se la registrazione è pronta, la fa partire.
    * Se la registrazione è in corso, la interrompe e posiziona il cursore
      all'inizio.
    * Se è stato caricato un file, inizia la riproduzione.
    * Se è in corso una riproduzione, consente di metterla in pausa fornendo
      il tempo di riproduzione attuale.
    * Se una riproduzione è in pausa, consente di riprenderla dalla
      posizione attuale.

* Freccia su

    * Mostra la posizione attuale della testina di riproduzione.
    * Se è stata effettuata una selezione, sposta il cursore sul marcatore
      di inizio della selezione B, fornendone la posizione.
    * Nella finestra di dialogo Volume, vocalizza il valore precedente che
      può essere raggiunto generalmente con freccia su.
    * Questo valore non è vocalizzato per default.

* NVDA+H

    * Apre la guida di questo add-on.

## Compatibilità ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20240327.0.0

* Fixed a bug that caused a log error when reloading plugins, thanks to Rob,
  from nvda-addons mailing list;

## Changes for 20240326.0.0

* Updated compatibility for nvda-2024.1.;
* Deleted download link from readme, the download link for future updates
  will now only be available from the add-on store.

## Changes for 20231229.0.0 ##

* Added a backward compatible implementation to support speak on demand
  mode, which will soon be available with nvda-2024.1.

## Changes for 20231007.0.0 ##

* After placing the cutting points and after opening the cutting properties
  window, with "Ctrl+N", adding accessibility to the title of this window by
  indicating the part index.
* In reading mode, after moving the start or end markers of selections with
  keys 1 to 6 of the alphanumeric pad, addition of automatic start of
  reading from the new position;
* Fixed a bug that occurred when consulting the remaining time with
  "control+shift+r" from the beginning of the track.

## Changes for 20230728.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.

## Changes for 20230508.0.0 and beyond ##

* Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.

## Novità nella versione 20.12 ##

* Disattivazione della sintesi durante la registrazione o la riproduzione
  nelle versioni più recenti di mp3directcut;
* Corretta la vocalizzazione del tempo di riproduzione rimanente per le
  nuove versioni di NVDA, utilizzando Python 3.

## Novità nella versione 19.02 ##

* Aggiunta la possibilità di configurare l'add-on nella finestra
  Impostazioni, disponibile a partire da NVDA 2018.2;
* Modificato il sistema di numerazione delle versioni, che ora è del tipo
  YY.MM (due cifre per l'anno, seguite da un punto, seguito da due cifre per
  il mese);
* Aggiunta la compatibilità con il nuovo formato per il numero di versione
  degli add-on, presente a partire da NVDA 2019.1.

## Novità nella versione 4.0 ##

* Aggiunta la compatibilità dell'add-on con Python 2.7 e Python 3;
* Risolto un problema con i percorsi dell'add-on che non contengono
  caratteri non ASCII .

## Novità nella versione 3.0 ##

* Si utilizza il modulo gui.guiHelper per assicurare il corretto layout
  della finestra di configurazione dell'add-on;
* Per le stringhe formattate, si utilizza format invece di %s;
* Si utilizza la compatibilità con le linee guida per l'implementazione.

## Novità nella versione 2.3 ##

* Aggiunta all'add-on la licenza GPL;
* Modificato il comando associato allo script che indica la posizione del
  marcatore di fine selezione da Ctrl + Shift + N a Ctrl + Shift + E, perché
  Ctrl + Shift + N non funziona con le ultime versioni di mp3DirectCut;
* Aggiunto uno script per confermare che la selezione è stata annullata con
  'Ctrl+r';
* Effettuata qualche correzione nel codice del modulo 'mp3directcut.py'.

## Novità nella versione 2.2 ##

* Correzione degli script che forniscono la posizione dei marcatori di
  selezione.

## Novità nella versione 2.1.1 ##

* Rimosso lo script che fornisce la durata totale e aggiunta
  quest'informazione nello script che fornisce il tempo di riproduzione
  corrente;
* Aggiunta la possibilità di attivare o disattivare le vocalizzazioni
  relative al tasto spazio nella configurazione dell'add-on, separatamente
  rispetto ad altre vocalizzazioni;
* Aggiunta la possibilità di attivare o disattivare le vocalizzazioni
  relative alla posizione dei marcatori di selezione nella configurazione
  dell'add-on;
* Aggiunta la vocalizzazione della parte attuale quando ci si sposta tra i
  punti di taglio;
* Correzione delle vocalizzazioni relative ai tasti verticali;
* Aggiunto uno script per aprire la guida di questo add-on con 'NVDA+H';
* Spostamento del menù di configurazione dell'add-on dal menù Strumenti al
  menù Preferenze di NVDA.

## Novità nella versione 2.1 ##

* Aggiunto uno script per vocalizzare lo spostamento al punto di taglio
  successivo con Control+Freccia destra;
* Aggiunto uno script per vocalizzare lo spostamento al punto di taglio
  precedente con Control+Freccia sinistra;
* Aggiunto uno script per vocalizzare lo spostamento in avanti di 4
  centesimi di secondo con Shift+Freccia destra;
* Aggiunto uno script per vocalizzare lo spostamento all'indietro di 4
  centesimi di secondo con Shift+Freccia sinistra;
* Correzione del titolo dell'add-on da 'per mp3DirectCut' a 'mp3DirectCut'.

## Novità nella versione 2.0 ##

* Aggiunto uno script per conoscere il tempo rimanente con 'Control Shift
  R';
* Sistemata la durata della riproduzione, che ora comprende anche le ore;
* Aggiunta la capacità di differenziare i millesimi e i centesimi di
  secondo.

## Novità nella versione 1.1 ##

* Aggiunta la capacità di includere la categoria mp3DirectCut nella finestra
  gesti e tasti di immissione;

    * Questi tasti saranno visibili solo durante l'utilizzo del prodotto.

* Aggiunta la possibilità di attivare o disattivare i messaggi automatici,
  nel menù strumenti di NVDA, elemento 'configurazione di mp3DirectCut';

## Novità nella versione 1.0 ##

* Versione iniziale.

[[!tag dev stable]]
