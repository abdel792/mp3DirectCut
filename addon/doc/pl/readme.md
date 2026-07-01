# mp3DirectCut

* Autor(zy): Abdel, Rémy, Abdellah zineddine, Jean-François COLAS.

# Prezentacja #

Ten dodatek poprawia dostępność programu mp3DirectCut w połączeniu z czytnikiem ekranu NVDA.

Został przetestowany z wersjami programu mp3DirectCut od 212 do 233.

## Skróty klawiszowe ##

Ten dodatek oferuje następujące polecenia:

* B

    * Służy do potwierdzenia prawidłowego umieszczenia znacznika początku zaznaczenia B.

* Ctrl+Shift+B

    * Służy do wskazania pozycji znacznika początku zaznaczenia B.
    * Dwukrotne naciśnięcie pozwala sprawdzić czas trwania zaznaczenia.

* Ctrl+Shift+D

    * Podaje czas trwania od początku pliku do bieżącej pozycji kursora odtwarzania.
    * Dwukrotne naciśnięcie pozwala sprawdzić całkowity czas trwania.

* Ctrl+R

    * Potwierdza, że zaznaczenie zostało anulowane.

* Ctrl+Shift+R

    * Podaje czas pozostały od bieżącej pozycji kursora odtwarzania do końca pliku.

* Ctrl+Shift+E

    * Służy do wskazania pozycji znacznika końca zaznaczenia N.
    * Dwukrotne naciśnięcie wyświetla podsumowanie pozycji B i N oraz czas trwania zaznaczenia.

* Ctrl+Shift+P

    * Podaje numer bieżącej części oraz całkowitą liczbę części w otwartym pliku.

* Ctrl+Shift+Space

    * Służy do określenia bieżącego poziomu wskaźnika wysterowania (VU-metru) podczas nagrywania.
    * Dwukrotne naciśnięcie resetuje wskaźnik.

* Strzałka w dół

    * Pozwala sprawdzić bieżącą pozycję głowicy odtwarzania.
    * To polecenie ustawia również kursor w miejscu znacznika końca zaznaczenia N, podając jednocześnie pozycję tego znacznika, jeśli dokonano zaznaczenia.
    * W oknie dialogowym głośności odczytuje kolejną wartość, którą ogólnie można osiągnąć za pomocą strzałki w dół.
    * Ta wartość nie jest odczytywana domyślnie.

* End

    * Przenosi kursor odtwarzania na koniec bieżącego pliku i podaje całkowity czas.

* Home

    * Przenosi kursor odtwarzania na początek bieżącego pliku.

* Strzałka w lewo

    * Pozwala na krótkie cofnięcie o jedną sekundę podczas odtwarzania, podając jednocześnie bieżący czas.
    * Ten czas można skonfigurować w opcjama programu mp3DirectCut.

* N

    * Służy do potwierdzenia prawidłowego umieszczenia znacznika końca zaznaczenia N.

* Page Down

    * Pozwala na skok do przodu o 10 sekund podczas odtwarzania, podając jednocześnie bieżący czas.
    * Ten czas można skonfigurować w opcjach programu mp3DirectCut.

* Page Up

    * Pozwala na cofnięcie o 10 sekund podczas odtwarzania, podając jednocześnie bieżący czas.
    * Ten czas można skonfigurować w opcjach programu mp3DirectCut.

* R

    * Pozwala przygotować nagrywanie i informuje, czy można nacisnąć spację, aby rozpocząć.

* Strzałka w prawo

    * Pozwala na krótkie przewinięcie do przodu o jedną sekundę podczas odtwarzania, podając jednocześnie bieżący czas.
    * Ten czas można skonfigurować w opcjach programu mp3DirectCut.

* Ctrl+Strzałka w prawo

    * Przenosi do następnego punktu podziału, podając jednocześnie bieżący czas.

* Ctrl+Strzałka w lewo

    * Przenosi do poprzedniego punktu podziału, podając jednocześnie bieżący czas.

* Shift+Strzałka w prawo

    * Pozwala na krótkie przewinięcie do przodu o cztery setne sekundy podczas odtwarzania, podając jednocześnie bieżący czas.

* Shift+Strzałka w lewo

    * Pozwala na krótkie cofnięcie o cztery setne sekundy podczas odtwarzania, podając jednocześnie bieżący czas.

* S

    * Służy do zatrzymania odtwarzania i podania bieżącego czasu.

* Space

    * Jeśli nagrywanie jest gotowe, uruchamia proces nagrywania.
    * Jeśli trwa nagrywanie, zatrzymuje je, ustawiając kursor na początku.
    * Jeśli plik jest załadowany, uruchamia odtwarzanie.
    * Jeśli trwa odtwarzanie, pozwala je wstrzymać (pauza), podając bieżący czas.
    * Jeśli odtwarzanie jest wstrzymane, pozwala je wznowić od bieżącego miejsca.

* Strzałka w górę

    * Pozwala sprawdzić bieżącą pozycję głowicy odtwarzania.
    * To polecenie ustawia również kursor w miejscu znacznika początku zaznaczenia B, podając jednocześnie pozycję tego znacznika, jeśli dokonano zaznaczenia.
    * W oknie dialogowym głośności odczytuje poprzednią wartość, którą ogólnie można osiągnąć za pomocą strzałki w górę.
    * Ta wartość nie jest odczytywana domyślnie.

* NVDA+H

    * Pozwala otworzyć pomoc bieżącego dodatku.

## Kompatybilność ##

* Ten dodatek jest kompatybilny z wersjami NVDA od 2019.3 i nowszymi.

## Zmiany w 20240327.0.0

* Naprawiono błąd, który powodował błąd w logu podczas przeładowywania wtyczek, podziękowania dla Roba z listy dyskusyjnej nvda-addons;

## Zmiany w 20240326.0.0

* Zaktualizowano kompatybilność dla nvda-2024.1.;
* Usunięto link do pobrania z pliku readme, link do pobrania przyszłych aktualizacji będzie teraz dostępny wyłącznie w sklepie z dodatkami (add-on store).

## Zmiany w 20231229.0.0 ##

* Dodano kompatybilną wstecznie implementację obsługującą tryb mowy na żądanie, który wkrótce będzie dostępny w nvda-2024.1.

## Zmiany w 20231007.0.0 ##

* Po umieszczeniu punktów cięcia i otwarciu okna właściwości cięcia za pomocą „Ctrl+N”, dodano dostępność do tytułu tego okna poprzez wskazywanie indeksu części.
* W trybie odczytu, po przesunięciu znaczników początku lub końca zaznaczenia za pomocą klawiszy od 1 do 6 na klawiaturze alfanumerycznej, dodano automatyczne uruchamianie odtwarzania od nowej pozycji;
* Naprawiono błąd występujący podczas sprawdzania pozostałego czasu za pomocą „control+shift+r” od początku utworu.

## Zmiany w 20230728.0.0 ##

* Zastosowano reguły flake8 i mypy do kodu;
* Zmieniono minimalną obsługiwaną wersję NVDA na 2019.3, aby zapewnić obsługę adnotacji wprowadzonych w Pythonie 3.

## Zmiany w 20230607.0.0 ##

* Dodano następujące przepływy pracy (workflows):
 * auto-update-translations - do automatycznej aktualizacji tłumaczeń z systemu tłumaczeń NVDA.
 * release-on-tag..yaml: do budowania i publikowania dodatku, gdy tylko zostanie wypchnięty nowy tag;
 * manual-release.yaml: do ręcznego budowania i wydawania nowych wersji dodatku.
* Zaktualizowano tłumaczenia.

## Zmiany w wersji 20230508.0.0 i nowszych ##

* Zmieniono numer wersji, minimalną wersję NVDA oraz link do pobrania zgodnie z konwencjami/wymaganiami sklepu.

## Zmiany w wersji 20.12 ##

* Zatrzymanie mowy podczas nagrywania i odtwarzania w najnowszych wersjach mp3DirectCut;
* Naprawiono odczyt pozostałego czasu dla nowych wersji NVDA korzystających z Pythona 3.

## Zmiany w wersji 19.02 ##

* Dodano konfigurację dodatku w panelu ustawień dostępnym od wersji nvda 2018.2;
* Zmieniono numerację wersji na format RR.MM (rok zapisany za pomocą 2 cyfr, kropka, miesiąc zapisany za pomocą 2 cyfr);
* Dodano kompatybilność z nowym formatem wersjonowania dodatków, który pojawił się od wersji nvda 2019.1.

## Zmiany w wersji 4.0 ##

* Dodano kompatybilność dodatku zarówno z Pythonem 2.7, jak i 3;
* Naprawiono błąd związany ze ścieżkami dodatku zawierającymi znaki spoza zestawu ASCII.

## Zmiany w wersji 3.0 ##

* Użyto modułu gui.guiHelper w celu zapewnienia prawidłowego wyglądu okna dialogowego konfiguracji dodatku;
* Użyto metody format zamiast %s dla sformatowanych ciągów znaków;
* Zastosowano zgodność z wytycznymi dotyczącymi implementacji.

## Zmiany w wersji 2.3 ##

* Dodano licencję GPL do dodatku;
* Zmieniono skrót skryptu podającego koniec zaznaczenia z Ctrl + Shift + N na Ctrl + Shift + E, ponieważ Ctrl + Shift + N nie działa w najnowszych wersjach mp3DirectCut;
* Dodano skrypt potwierdzający anulowanie zaznaczenia za pomocą 'Ctrl+r';
* Wprowadzono kilka poprawek w kodzie appModule 'mp3directcut.py'.

## Zmiany w wersji 2.2 ##

* Korekta skryptów podających lokalizacje znaczników zaznaczenia.

## Zmiany w wersji 2.1.1 ##

* Usunięto skrypt podający całkowity czas i dodano tę informację do skryptu podającego czas, który upłynął;
* Dodano możliwość włączania lub wyłączania komunikatów związanych z klawiszem spacji w opcjach konfiguracji modułu, niezależnie od innych komunikatów;
* Dodano możliwość włączania lub wyłączania komunikatów o umieszczeniu znaczników zaznaczenia w opcjach konfiguracji modułu;
* Dodano komunikaty o bieżącej części podczas poruszania się po punktach podziału;
* Korekta komunikatów związanych z klawiszami pionowymi;
* Dodano skrypt do otwierania pomocy bieżącego dodatku za pomocą 'NVDA+H';
* Przeniesiono menu konfiguracji dodatku z menu Narzędzia do menu Preferencje w NVDA.

## Zmiany w wersji 2.1 ##

* Dodano skrypt odczytujący przejście do następnego punktu podziału za pomocą Control+Strzałka w prawo;
* Dodano skrypt odczytujący przejście do poprzedniego punktu podziału za pomocą Control+Strzałka w lewo;
* Dodano skrypt odczytujący przesunięcie o 4 setne sekundy do przodu za pomocą Shift+Strzałka w prawo;
* Dodano skrypt odczytujący przesunięcie o 4 setne sekundy do tyłu za pomocą Shift+Strzałka w lewo;
* Skorygowano podsumowanie dodatku z 'for mp3DirectCut' na 'mp3DirectCut'.

## Zmiany w wersji 2.0 ##

* Dodano skrypt pozwalający poznać pozostały czas za pomocą 'Control Shift R';
* Naprawiono odczyt czasów trwania zawierających godziny;
* Dodano możliwość rozróżniania tysięcznych lub setnych części sekundy.

## Zmiany w wersji 1.1 ##

* Dodano możliwość włączenia kategorii mp3DirectCut do zdarzeń wprowadzania (Input Gestures);

    * Będą one widoczne tylko podczas korzystania z programu mp3DirectCut.

* Dodano możliwość włączania lub wyłączania automatycznych komunikatów w menu narzędzi NVDA, pozycja 'Konfiguracja mp3DirectCut';

## Zmiany w wersji 1.0 ##

* Wersja początkowa.
