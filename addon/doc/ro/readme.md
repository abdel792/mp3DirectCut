# mp3DirectCut

* Autor(i): Abdel, Rémy, Abdellah zineddine, Jean-François COLAS.

# Prezentare #

Acest supliment îmbunătățește accesibilitatea software-ului mp3DirectCut cu NVDA.

A fost testat cu versiuni de mp3DirectCut de la 212 până la 233.

## Scurtături de tastatură ##

Acest supliment oferă următoarele comenzi:

* B

    * Folosit pentru a confirma plasarea corectă a marcatorului de început al selecției B.

* Ctrl+Shift+B

    * Folosit pentru a indica poziția marcatorului de început al selecției B.
    * O apăsare dublă vă permite să aflați durata selecției.

* Ctrl+Shift+D

    * Oferă durata de la începutul fișierului până la poziția curentă a cursorului de redare.
    * O apăsare dublă vă permite să aflați durata totală.

* Ctrl+R

    * Confirmă că selecția a fost anulată.

* Ctrl+Shift+R

    * Oferă timpul rămas de la poziția curentă a cursorului de redare până la sfârșitul fișierului.

* Ctrl+Shift+E

    * Folosit pentru a indica poziția marcatorului de sfârșit al selecției N.
    * O apăsare dublă oferă o recapitulare a pozițiilor B și N, precum și durata selecției.

* Ctrl+Shift+P

    * Oferă referința părții curente și numărul total de părți din fișierul curent.

* Ctrl+Shift+Space

    * Folosit pentru a determina nivelul curent al indicatorului de volum (vu-metru) în timpul înregistrării.
    * O apăsare dublă îl resetează.

* Săgeată în Jos

    * Vă permite să vizualizați poziția curentă a cursorului de redare.
    * Această comandă plasează, de asemenea, cursorul la locația marcatorului de sfârșit al selecției N, oferind în același timp locația acestui marcator dacă a fost făcută o selecție.
    * În caseta de dialog pentru volum, vocalizează următoarea valoare care poate fi atinsă în general cu săgeată în jos.
    * Această valoare nu este vocalizată în mod implicit.

* End

    * Mută cursorul de redare la sfârșitul fișierului curent și oferă timpul total.

* Home

    * Mută cursorul de redare la începutul fișierului curent.

* Săgeată Stânga

    * Permite efectuarea unei scurte întoarceri înapoi de o secundă în timpul redării, oferind în același timp durata curentă.
    * Această durată este configurabilă în opțiunile mp3DirectCut.

* N

    * Folosit pentru a confirma plasarea corectă a marcatorului de sfârșit al selecției N.

* Page Down

    * Permite efectuarea unui salt înainte de 10 secunde în timpul redării, oferind în același timp durata curentă.
    * Această durată este configurabilă în opțiunile mp3DirectCut.

* Page Up

    * Permite efectuarea unei întoarceri înapoi de 10 secunde în timpul redării, oferind în același timp durata curentă.
    * Această durată este configurabilă în opțiunile mp3DirectCut.

* R

    * Permite pregătirea unei înregistrări și aflarea dacă puteți apăsa bara de spațiu pentru a începe.

* Săgeată Dreapta

    * Permite efectuarea unui scurt avans de o secundă în timpul redării, oferind în același timp durata curentă.
    * Această durată este configurabilă în opțiunile mp3DirectCut.

* Ctrl+Săgeată Dreapta

    * Mută la următorul punct de divizare, oferind în același timp durata curentă.

* Ctrl+Săgeată Stânga

    * Mută la punctul de divizare anterior, oferind în același timp durata curentă.

* Shift+Săgeată Dreapta

    * Permite efectuarea unui scurt avans de patru sutimi de secundă în timpul redării, oferind în același timp durata curentă.

* Shift+Săgeată Stânga

    * Permite efectuarea unei scurte întoarceri înapoi de patru sutimi de secundă în timpul redării, oferind în același timp durata curentă.

* S

    * Folosit pentru a opri redarea și a oferi durata curentă.

* Space

    * Dacă înregistrarea este gata, pornește această înregistrare.
    * Dacă o înregistrare este în curs, o oprește plasând cursorul la început.
    * Dacă un fișier este încărcat, pornește redarea.
    * Dacă o redare este în curs, permite punerea în pauză oferind în același timp durata curentă.
    * Dacă redarea este în pauză, permite repornirea redării de la locația curentă.

* Săgeată în Sus

    * Vă permite să vizualizați poziția curentă a cursorului de redare.
    * Această comandă plasează, de asemenea, cursorul la locația marcatorului de început al selecției B, oferind în același timp locația acestui marcator dacă a fost făcută o selecție.
    * În caseta de dialog pentru volum, vocalizează valoarea anterioară care poate fi atinsă în general cu săgeată în sus.
    * Această valoare nu este vocalizată în mod implicit.

* NVDA+H

    * Permite deschiderea ajutorului pentru suplimentul curent.

## Compatibilitate ##

* Acest supliment este compatibil cu versiunile de NVDA de la 2019.3 și ulterioare.

## Modificări pentru 20240327.0.0

* S-a corectat o eroare care cauza o eroare de jurnal la reîncărcarea pluginurilor, datorită lui Rob de pe lista de discuții nvda-addons;

## Modificări pentru 20240326.0.0

* S-a actualizat compatibilitatea pentru nvda-2024.1.;
* S-a eliminat linkul de descărcare din readme, linkul de descărcare pentru viitoarele actualizări va fi acum disponibil doar din magazinul de suplimente (add-on store).

## Modificări pentru 20231229.0.0 ##

* S-a adăugat o implementare compatibilă cu versiunile anterioare pentru a susține modul de vorbire la cerere, care va fi disponibil în curând cu nvda-2024.1.

## Modificări pentru 20231007.0.0 ##

* După plasarea punctelor de tăiere și după deschiderea ferestrei cu proprietățile de tăiere prin „Ctrl+N”, s-a adăugat accesibilitate la titlul acestei ferestre prin indicarea indexului părții.
* În modul de citire, după mutarea marcatorilor de început sau de sfârșit ai selecțiilor cu tastele de la 1 la 6 ale blocului alfanumeric, s-a adăugat pornirea automată a redării de la noua poziție;
* S-a corectat o eroare care apărea la consultarea timpului rămas cu „control+shift+r” de la începutul piesei.

## Modificări pentru 20230728.0.0 ##

* S-au aplicat regulile flake8 și mypy asupra codului;
* S-a schimbat versiunea minimă de NVDA suportată la 2019.3 pentru a susține adnotările introduse în Python 3.

## Modificări pentru 20230607.0.0 ##

* S-au adăugat următoarele fluxuri de lucru (workflows):
 * auto-update-translations - pentru actualizarea automată a traducerilor din sistemul de traducere al NVDA.
 * release-on-tag..yaml: pentru construirea și publicarea suplimentului imediat ce este trimis un nou tag;
 * manual-release.yaml: pentru construirea și lansarea manuală a noilor versiuni ale suplimentului.
* Traduceri actualizate.

## Modificări pentru versiunea 20230508.0.0 și ulterioare ##

* S-au modificat numărul versiunii, versiunea minimă de NVDA și linkul de descărcare conform convențiilor/cerințelor magazinului.

## Modificare pentru versiunea 20.12 ##

* Oprirea vorbirii în timpul înregistrării și redării pentru cele mai recente versiuni de mp3DirectCut;
* S-a corectat citirea timpului rămas pentru noile versiuni de NVDA care utilizează Python 3.

## Modificare pentru versiunea 19.02 ##

* S-a adăugat configurația suplimentului în panoul de setări disponibil începând cu nvda 2018.2;
* S-a modificat numerotarea versiunilor utilizând AA.MM (anul din 2 cifre, urmat de punct, urmat de luna din 2 cifre);
* S-a adăugat compatibilitatea cu noul format de versiune pentru suplimente, apărut începând cu nvda 2019.1.

## Modificare pentru versiunea 4.0 ##

* S-a adăugat compatibilitatea suplimentului atât cu Python 2.7, cât și cu 3;
* S-a corectat o eroare cu căile suplimentului care conțin caractere non-ASCII.

## Modificare pentru versiunea 3.0 ##

* S-a utilizat modulul gui.guiHelper pentru a asigura aspectul corect al ferestrei de dialog pentru configurarea suplimentului;
* S-a utilizat format în loc de %s pentru șirurile formatate;
* S-a aplicat conformitatea cu ghidurile de implementare.

## Modificare pentru versiunea 2.3 ##

* S-a adăugat licența GPL la supliment;
* S-a modificat scurtătura scriptului care oferă sfârșitul selecției de la Ctrl + Shift + N la Ctrl + Shift + E deoarece Ctrl + Shift + N nu funcționează cu cele mai recente versiuni de mp3DirectCut;
* S-a adăugat un script pentru a confirma că selecția a fost anulată cu „Ctrl+r”;
* S-au efectuat câteva corecții în codul appModule „mp3directcut.py”.

## Modificare pentru versiunea 2.2 ##

* Corectarea scripturilor care oferă locațiile marcatorilor de selecție.

## Modificare pentru versiunea 2.1.1 ##

* Eliminarea scriptului care oferă timpul total și adăugarea acestei informații la scriptul care oferă timpul scurs;
* S-a adăugat posibilitatea de a activa sau dezactiva anunțurile legate de tasta spațiu în opțiunile de configurare ale modulului, separat de alte anunțuri;
* S-a adăugat posibilitatea de a activa sau dezactiva anunțul de plasare a marcatorilor de selecție în opțiunile de configurare ale modulului;
* Adăugarea anunțului piesei curente la deplasarea prin punctele de tăiere;
* Corectarea anunțurilor legate de tastele verticale;
* Adăugarea unui script pentru a deschide ajutorul suplimentului curent cu „NVDA+H”;
* Deplasarea meniului de configurare al suplimentului din meniul Instrumente în meniul Preferințe al NVDA.

## Modificare pentru versiunea 2.1 ##

* Adăugarea unui script pentru a vocaliza deplasarea la următorul punct de divizare cu Control+Săgeată Dreapta;
* Adăugarea unui script pentru a vocaliza deplasarea la punctul de divizare anterior cu Control+Săgeată Stânga;
* Adăugarea unui script pentru a vocaliza deplasarea cu 4 sutimi de secundă înainte, cu Shift+Săgeată Dreapta;
* Adăugarea unui script pentru a vocaliza deplasarea cu 4 sutimi de secundă înapoi, cu Shift+Săgeată Stânga;
* Corectarea rezumatului suplimentului de la „for mp3DirectCut” la „mp3DirectCut”.

## Modificare pentru versiunea 2.0 ##

* Adăugarea unui script pentru a afla timpul rămas cu „Control Shift R”;
* S-a corectat citirea duratelor care includ ore;
* S-a adăugat capacitatea de a diferenția miimile sau sutimile de secundă.

## Modificare pentru versiunea 1.1 ##

* S-a adăugat posibilitatea de a include categoria mp3DirectCut în Gesturile de Intrare;

    * Acestea vor fi vizibile doar în timpul utilizării software-ului mp3DirectCut.

* S-a adăugat posibilitatea de a activa sau dezactiva mesajele automate, în meniul de instrumente al NVDA, elementul „Configurare mp3DirectCut”;

## Modificare pentru versiunea 1.0 ##

* Versiune inițială.
