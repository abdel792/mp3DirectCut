# mp3DirectCut #

*	 Autori: Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
*	 Descărcați [versiunea stabilă][1]
*	 Descărcați [versiunea în dezvoltare][2]

# Prezentare #

Acest supliment îmbunătățește accesibilitatea programului mp3DirectCut cu
NVDA.

A fost testat cu versiuni ale mp3DirectCut de la 212 până la 223.

## Scurtături ##

Acest supliment oferă următoarele comenzi:

*	B
	*	Folosită pentru a confirma plasarea corectă a reperului la începutul selecției B.
*	Ctrl+Shift+B
	*	Folosită pentru a indica poziția reperului a începutului selecției B.
	*	Dubla apăsare oferă durata selecției.
*	Ctrl+Shift+D
	*	Oferă durata de la începutul fișierului până la poziția curentă a cursorului de redare.
	*	Dubla apăsare oferă durata totală.
*	Ctrl+R
	*	Confirmă că selecția a fost anulată..
*	Ctrl+Shift+R
	*	Oferă timpul rămas de la poziția curentă a cursorului de redare până la sfârșitul fișierului..
*	Ctrl+Shift+E
	*	Folosită pentru indicarea poziției reperului sfârșitului de selecției N.
	*	Dubla apăsare oferă recapitularea pozițiilor B și N și durata selecției..
*	Ctrl+Shift+P
	*	Oferă referința la partea prezentă și numărul total de părți în fișierul curent.
*	Ctrl+Shift+Space
	*	Folosită pentru determinarea nivelului curent al vu-metrului, în timpul înregistrării.
	*	Dubla apăsare îl resetează.
*	Down Arrow
	*	Permite vederea poziției curente a capului de redare.
	*	Această comandă poziționează și cursorul la locația reperului sfârșitului selecției N, oferind locația acestui reper dacă a fost făcută o selecție.
	*	În caseta de dialog a volumului, pronunță următoarea valoare care poate fi atinsă în mod general cu săgeată jos.
	*	Această valoare nu este pronunțată implicit.
*	End
	*	Mută cursorul de redare la sfârșitul fișierului curent și oferă timpul total.
*	Home
	*	Mută cursorul de redare la începutul fișierului curent.
*	Left Arrow
	*	Permite execuția unei întoarceri scurte de o secundă în timpul redării, oferind și durata curentă.
	*	Acest interval este configurabil din opțiunile mp3directcut.
*	N
	*	Folosită pentru a confirma poziționarea corectă a reperului sfârșitului selecției N.
*	Page Down
	*	Permite un salt în avans cu 10 secunde în timpul redării, oferind și durata curentă.
	*	Acest interval este configurabil din opțiunile mp3directcut.
*	Page Up
	*	Permite un salt înapoi cu 10 secunde în timpul redării, oferind și durata curentă.
	*	Acest interval este configurabil din opțiunile mp3directcut.
*	R
	*	Permite pregătirea unei înregistrări și dacă puteți apăsa tasta spațiu pentru a începe.
*	Right Arrow
	*	Permite execuția unei salt scurt de o secundă în timpul redării, oferind și durata curentă.
	*	Acest interval este configurabil din opțiunile mp3directcut.
*	Ctrl+Right Arrow
	*	Mută la următorul punct de diviziune , oferind și durata curentă.
*	Ctrl+Left Arrow
	*	Mută la anteriorul punct de diviziune , oferind și durata curentă.
*	Shift+Right Arrow
	*	Permite execuția unei salt scurt înainte de patru sutimi de secundă în timpul redării, oferind și durata curentă.
*	Shift+Left Arrow
	*	Permite execuția unei salt scurt înapoi de patru sutimi de secundă în timpul redării, oferind și durata curentă.
*	S
	*	Folosită pentru a opri citirea și a oferi durata curentă.
*	Space
	*	Dacă înregistrarea este pregătită, începe această înregistrare.
	*	Dacă o înregistrare este în derulare, o oprește prin poziționarea cursorului la început.
	*	Dacă este încărcat un fișier, începeți citirea.
	*	Dacă o citire este în desfășurare, permite să faceți o pauză și oferă durata curentă.
	*	Dacă citirea e pe pauză, permite repornirea acesteia de la locația curentă.
*	Up Arrow
	*	Permite vederea poziției curente a capului de redare.
	*	Acestă comandă, de asemenea, poziționează cursorul la locația reperului începutului slecției B, oferind și locația acestui reper, dacă a fost făcută o selecție.
	*	În caseta de dialog a volumului, pronunță valoarea anterioară care poate fi atinsă în mod general cu săgeată sus.
	*	Această valoare nu este pronunțată implicit.
*	NVDA+H
	*	Permite deschiderea ajutorului pentru suplimentul curent.

## Modificări pentru versiunea 4.0 ##

*	 Adăugat compatibilitate pentru supliment atât cu Python 2.7 cât și 3;
*	 Rezolvat defect cu căile suplimentului care conțin caractere non-ASCII.

## Modificări pentru versiunea 3.0 ##

*	 Folosit modulul gui.guiHelper pentru a asigura afișarea corectă a
   dialogului de configurare pentru supliment;
*	 Folosit format în loc de %s pentru formatarea șirurilor de caractere;
*	 Folosit conformarea la principiile generale pentru implementare.

## Modificări pentru versiunea 2.3 ##

*	 Adăugat licența GPL pentru supliment;
*	 Schimbat scurtătura scriptului care dă sfârșitul selecției din
   Ctrl+Shift+N în Ctrl+Shift+E, deoarece Ctrl+Shift+N nu funcționează cu
   noile versiuni de mp3DirectCut;
*	 Adăugat un script pentru a confirma că selecția a fost anulată cu
   ‚Ctrl+r’;
*	 Făcut niște corecturi în codul modulului 'mp3directcut.py'.

## Modificări aduse în versiunea 2.2 ##

*	 Corecția scripturilor care dau locația selectată a marcajelor.

## Modificări aduse în versiunea 2.1.1 ##

*	 Eliminarea scriptului care dă timpul total și adaugă această informație
   la scriptul care dă timpul scurs.
*	 A fost adăugată abilitatea de a activa sau dezactiva anunțurile relatate
   la tasta spațiu în opțiunile de configurare ale modulelor separat din
   alte anunțuri;
*	 A fost adăugată abilitatea de a activa sau dezactiva anunțul plasat
   selecției marque în opțiunile de configurare ale modulelor;
*	 Adăugarea anunțării părții curente atunci când se deplasează prin
   punctele de tăiere;
*	 Corectarea anunțurilor relatate la tastele verticale;
*	 Adăugarea unui script pentru a deschide ajutorul add-onului curent cu
   'NVDA+H';
*	 Deplasare din meniul de configurare ale add-onurilor la meniul
   instrumente către meniul preferințe nvda.

## Modificări aduse în versiunea 2.1 ##

*	 Adăugarea unui script pentru a cânta se deplasează la următorul punct
   divizat cu control+săgeată dreapta;
*	 Adăugarea unui script pentru a cânta se deplasează la punctul anterior
   divizat cu control+săgeată stânga;
*	 Adăugarea unui script pentru a cânta se deplasează cu 400 de secunde
   înainte, cu shift+săgeată dreapta;
*	 Adăugarea unui script pentru a cânta se deplasează cu 400 de secunde în
   urmă, cu shift+săgeată stânga;
*	 Corectarea cuprinsului add-on-ului de la 'for mp3DirectCut' la
   'mp3DirectCut'.

## Modificări în versiunea 1.0 ##

*	 A fost adăugat un script pentru cunoașterea timpului rămas cu 'Control
   Shift R';
*	 A fost reparată durata orelor;
*	 A fost adăugată abilitatea de diferențiere între mi și sute de secunde;

## Modificări aduse în versiunea 1.1 ##

*	 Adăugat posibilitatea de a include categoria mp3DirectCut în gesturile de intrare;
	*	 Vor fi vizibile doar în timpul folosirii software-ului mp3DirectCut.
*	 Adăugat abilitatea de a activa sau dezactiva mesajele automate în meniul de unelte al NVDA, elementul 'configurare mp3DirectCut';

## Modificări adyse în 1.0 ##

*	 Versiunea inițială.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
