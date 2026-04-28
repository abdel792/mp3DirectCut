# mp3DirectCut

- Autori: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS

# Prezentare

Acest supliment îmbunătățește accesibilitatea programului mp3DirectCut cu
NVDA.

A fost testat cu versiuni ale mp3DirectCut de la 212 până la 223.

## Scurtături

Acest supliment oferă următoarele comenzi:

- B

  - Folosită pentru a confirma plasarea corectă a reperului la începutul selecției B.

- Ctrl+Shift+B

  - Folosită pentru a indica poziția reperului a începutului selecției B.
  - Dubla apăsare oferă durata selecției.

- Ctrl+Shift+D

  - Oferă durata de la începutul fișierului până la poziția curentă a cursorului de redare.
  - Dubla apăsare oferă durata totală.

- Ctrl+R

  - Confirmă că selecția a fost anulată..

- Ctrl+Shift+R

  - Oferă timpul rămas de la poziția curentă a cursorului de redare până la sfârșitul fișierului..

- Ctrl+Shift+E

  - Folosită pentru indicarea poziției reperului sfârșitului de selecției N.
  - Dubla apăsare oferă recapitularea pozițiilor B și N și durata selecției..

- Ctrl+Shift+P

  - Oferă referința la partea prezentă și numărul total de părți în fișierul curent.

- Ctrl+Shift+Space

  - Folosită pentru determinarea nivelului curent al vu-metrului, în timpul înregistrării.
  - Dubla apăsare îl resetează.

- Down Arrow

  - Permite vederea poziției curente a capului de redare.
  - Această comandă poziționează și cursorul la locația reperului sfârșitului selecției N, oferind locația acestui reper dacă a fost făcută o selecție.
  - În caseta de dialog a volumului, pronunță următoarea valoare care poate fi atinsă în mod general cu săgeată jos.
  - Această valoare nu este pronunțată implicit.

- End

  - Mută cursorul de redare la sfârșitul fișierului curent și oferă timpul total.

- Home

  - Mută cursorul de redare la începutul fișierului curent.

- Left Arrow

  - Permite execuția unei întoarceri scurte de o secundă în timpul redării, oferind și durata curentă.
  - Acest interval este configurabil din opțiunile mp3directcut.

- N

  - Folosită pentru a confirma poziționarea corectă a reperului sfârșitului selecției N.

- Page Down

  - Permite un salt în avans cu 10 secunde în timpul redării, oferind și durata curentă.
  - Acest interval este configurabil din opțiunile mp3directcut.

- Page Up

  - Permite un salt înapoi cu 10 secunde în timpul redării, oferind și durata curentă.
  - Acest interval este configurabil din opțiunile mp3directcut.

- R

  - Permite pregătirea unei înregistrări și dacă puteți apăsa tasta spațiu pentru a începe.

- Right Arrow

  - Permite execuția unei salt scurt de o secundă în timpul redării, oferind și durata curentă.
  - Acest interval este configurabil din opțiunile mp3directcut.

- Ctrl+Right Arrow

  - Mută la următorul punct de diviziune , oferind și durata curentă.

- Ctrl+Left Arrow

  - Mută la anteriorul punct de diviziune , oferind și durata curentă.

- Shift+Right Arrow

  - Permite execuția unei salt scurt înainte de patru sutimi de secundă în timpul redării, oferind și durata curentă.

- Shift+Left Arrow

  - Permite execuția unei salt scurt înapoi de patru sutimi de secundă în timpul redării, oferind și durata curentă.

- S

  - Folosită pentru a opri citirea și a oferi durata curentă.

- Space

  - Dacă înregistrarea este pregătită, începe această înregistrare.
  - Dacă o înregistrare este în derulare, o oprește prin poziționarea cursorului la început.
  - Dacă este încărcat un fișier, începeți citirea.
  - Dacă o citire este în desfășurare, permite să faceți o pauză și oferă durata curentă.
  - Dacă citirea e pe pauză, permite repornirea acesteia de la locația curentă.

- Up Arrow

  - Permite vederea poziției curente a capului de redare.
  - Acestă comandă, de asemenea, poziționează cursorul la locația reperului începutului slecției B, oferind și locația acestui reper, dacă a fost făcută o selecție.
  - În caseta de dialog a volumului, pronunță valoarea anterioară care poate fi atinsă în mod general cu săgeată sus.
  - Această valoare nu este pronunțată implicit.

- NVDA+H

  - Permite deschiderea ajutorului pentru suplimentul curent.

## Modificări pentru versiunea 4.0

- Adăugat compatibilitate pentru supliment atât cu Python 2.7 cât și 3;

## Modificări pentru versiunea 3.0

- Folosit modulul gui.guiHelper pentru a asigura afișarea corectă a
  dialogului de configurare pentru supliment;

## Modificări pentru versiunea 2.3

- Adăugat licența GPL pentru supliment;
- Schimbat scurtătura scriptului care dă sfârșitul selecției din
  Ctrl+Shift+N în Ctrl+Shift+E, deoarece Ctrl+Shift+N nu funcționează cu
  noile versiuni de mp3DirectCut;

## Modificări aduse în versiunea 2.2

- Corecția scripturilor care dau locația selectată a marcajelor.

## Modificări aduse în versiunea 2.1.1

- Eliminarea scriptului care dă timpul total și adaugă această informație
  la scriptul care dă timpul scurs.
- A fost adăugată abilitatea de a activa sau dezactiva anunțurile relatate
  la tasta spațiu în opțiunile de configurare ale modulelor separat din
  alte anunțuri;
- A fost adăugată abilitatea de a activa sau dezactiva anunțul plasat
  selecției marque în opțiunile de configurare ale modulelor;

## Modificări aduse în versiunea 2.1

- Adăugarea unui script pentru a cânta se deplasează la următorul punct
  divizat cu control+săgeată dreapta;
- Adăugarea unui script pentru a cânta se deplasează la punctul anterior
  divizat cu control+săgeată stânga;

## Modificări în versiunea 1.0

- A fost adăugat un script pentru cunoașterea timpului rămas cu 'Control
  Shift R';
- A fost reparată durata orelor;
- A fost adăugată abilitatea de diferențiere între mi și sute de secunde;
- manual-release.yaml: to build and release new versions of the add-on manually.
- Updated translations.

## Modificări aduse în versiunea 1.1

- Adăugat posibilitatea de a include categoria mp3DirectCut în gesturile de intrare;
  \*	 Vor fi vizibile doar în timpul folosirii software-ului mp3DirectCut.

## Modificări adyse în 1.0

- Versiunea inițială.
- Fixed reading remaining time for new versions of NVDA using Python 3.

## Change for version 19.02

- Added the add-on's configuration in the settings panel available since nvda 2018.2;
- Changed version numbering using YY.MM (The year in 2 digits, followed by a dot, followed by the month in 2 digits);
- Added compatibility with the new versioning format of add-on, appeared since nvda 2019.1.

## Change for version 4.0

- Added the Compatibility of the add-on with both Python 2.7 and 3;
- Fixed a bug with add-on paths that contain non-ASCII characters.

## Change for version 3.0

- Used the gui.guiHelper module to ensure the correct appearance of the addon's configuration dialog;
- Used format instead of %s for formatted strings;
- Used compliance with guidelines for implementation.

## Change for version 2.3

- Added the GPL license to the addon;
- Changed the shortcut of the script giving the end of selection from Ctrl + Shift + N to Ctrl + Shift + E because Ctrl + Shift + N doesn't work with the latest versions of mp3DirectCut;
- Added a script to confirm that the selection has been canceled with 'Ctrl+r';
- Made some corrections in the code of the appModule 'mp3directcut.py'.

## Change for version 2.2

- Correction of the scripts giving the selection markers' locations.

## Change for version 2.1.1

- Removing the script giving the total time and adding this information to the script giving the elapsed time;
- Added the ability to enable or disable the announcements related to the space key in the module's configuration options, separately from other announcements;
- Added the ability to enable or disable the announcement of placement of the selection marqueures in the module's configuration options;
- Adding the announcement of the current part when moving through the cutting points;
- Correction of announcements related to vertical keys;
- Adding a script to open the help of the current add-on with 'NVDA+H';
- Displacement of the add-on's configuration menu from the Tools menu to the Preferences menu of NVDA.

## Change for version 2.1

- Adding a script to vocalize moving to the next splitting point with Control+Right Arrow;
- Adding a script to vocalize moving to the previous splitting point with Control+Left Arrow;
- Adding a script to vocalize the displacement of 4 hundredths of second ahead, with Shift+Right Arrow;
- Adding a script to vocalize the displacement of 4 hundredths of second back, with Shift+Left Arrow;
- Correction of the addon's summary from 'for mp3DirectCut' to 'mp3DirectCut'.

## Change for version 2.0

- Adding a script to know the remaining time with 'Control Shift R';
- Fixed reading durations including hours;
- Added ability to differentiate thousandths or hundredths of seconds.

## Change for version 1.1

- Added the ability to include the mp3DirectCut category into the Input Gestures;

  - They will be visible only during use of the mp3DirectCut software.

- Added the ability to enable or disable automatic messages, in the tools menu of NVDA, item 'mp3DirectCut configuration';

## Change for version 1.0

- Initial version.
