# mp3DirectCut #

* Authorzy : Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
* Pobierz [wersja stabilna][1]
* Pobierz [wersja rozwojowa][2]

# Prezentacja #

Ten dodatek ulepsza dostępność programu mp3DirectCut z NVDA.

Został przetestowany z wersjami mp3DirectCut od 212 do 223.

## Skróty klawiszowe ##

Ten dodatek oferuje następujące polecenia:

* B

    * Służy do potwierdzenia prawidłowego umieszczenia znacznika początku
      zaznaczenia B.

* Ctrl+Shift+B

    * Służy do wskazania położenia znacznika początku zaznaczenia B.
    * Podwójne naciśnięcie pozwala podać czas trwania wyboru.

* Ctrl+Shift+D

    * Podaje czas trwania od początku pliku do bieżącej pozycji kursora
      odtwarzania.
    * Podwójne naciśnięcie pozwala uzyskać całkowity czas trwania.

* Ctrl+R

    * Potwierdza, że wybór został anulowany.

* Ctrl+Shift+R

    * Podaje czas pozostały od bieżącej pozycji kursora odtwarzania do końca
      pliku.

* Ctrl+Shift+E

    * Służy do wskazania położenia znacznika końca zaznaczenia N.
    * Podwójne ciśnienie daje pozycje recapitulatif B i N oraz czas trwania
      zaznaczenia.

* Ctrl+Shift+P

    * Podaje odniesienie do rzeczywistej części i całkowitą liczbę części w
      bieżącym pliku.

* Ctrl+Shift+spacja

    * Służy do określania aktualnego poziomu vu-miernika, podczas
      nagrywania.
    * Podwójne naciśnięcie resetuje go.

* Strzałka w dół

    * Umożliwia wyświetlenie bieżącej pozycji głowicy odtwarzania.
    * To polecenie umieszcza również kursor w miejscu znacznika końca
      zaznaczenia N, podając jednocześnie położenie tego znacznika, jeśli
      dokonano wyboru.
    * W oknie dialogowym głośności odczyta następną wartość, do której można
      dotrzeć zazwyczaj za pomocą strzałki w dół.
    * Ta wartość nie jest domyślnie wymawiana.

* End

    * Przesuwa kursor odtwarzania na końcu bieżącego pliku i podaje
      całkowity czas.

* Home

    * Przesuwa kursor odtwarzania na początku bieżącego pliku.

* Strzałka w lewo

    * Zróbmy krótki powrót o jedną sekundę podczas odtwarzania, podając
      bieżący czas trwania.
    * Ten czas trwania jest konfigurowalny w opcjach mp3directcut.

* N

    * Służy do potwierdzenia prawidłowego umieszczenia znacznika końca
      zaznaczenia N.

* Page Down

    * Zróbmy skok do przodu o 10 sekund podczas odtwarzania, podając bieżący
      czas trwania.
    * Ten czas trwania jest konfigurowalny w opcjach mp3directcut.

* Page Up

    * Przywróćmy 10 sekund podczas odtwarzania, podając bieżący czas
      trwania.
    * Ten czas trwania jest konfigurowalny w opcjach mp3directcut.

* R

    * Umożliwia przygotowanie nagrywania i to, czy można nacisnąć spację,
      aby rozpocząć.

* Strzałka w prawo

    * Zróbmy krótki czas do przodu o jedną sekundę podczas odtwarzania,
      podając bieżący czas trwania.
    * Ten czas trwania jest konfigurowalny w opcjach mp3directcut.

* Ctrl+strzałka w prawo

    * Przechodzi do następnego punktu podziału, podając bieżący czas
      trwania.

* Ctrl+strzałka w lewo

    * Przechodzi do poprzedniego punktu podziału, podając bieżący czas
      trwania.

* Shift+strzałka w prawo

    * Zróbmy krótki czas do przodu o cztery setne sekundy podczas
      odtwarzania, podając bieżący czas trwania.

* Shift+strzałka w lewo

    * Zróbmy krótki czas do tyłu o cztery setne sekundy podczas odtwarzania,
      podając bieżący czas trwania.

* S

    * Służy do zatrzymania odczytu i podania bieżącego czasu trwania.

* Spacja

    * Jeśli nagrywanie jest gotowe, rozpocznij nagrywanie.
    * Jeśli nagrywanie jest w toku, zatrzymaj je, umieszczając kursor na
      początku.
    * Jeśli plik jest załadowany, rozpocznij odczyt.
    * Jeśli odczyt jest w toku, pozwala na zrobienie przerwy, podając
      bieżący czas trwania.
    * Jeśli odczyt jest wstrzymany, umożliwia ponowne uruchomienie odczytu z
      bieżącej lokalizacji.

* Strzałka w górę

    * Umożliwia wyświetlenie bieżącej pozycji głowicy odtwarzania.
    * To polecenie umieszcza również kursor w miejscu znacznika początku
      zaznaczenia B, podając jednocześnie położenie tego znacznika, jeśli
      dokonano wyboru.
    * W oknie dialogowym głośności swokalizuj poprzednią wartość, do której
      można dotrzeć zazwyczaj za pomocą upArrow.
    * Ta wartość nie jest domyślnie wymawiana.

* NVDA+H

    * Otwórzmy pomoc bieżącego dodatku.

## Zgodność ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20230728.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.

## Changes for 20230508.0.0 and beyond ##

* • Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.

## Zmiana wersji 20.12 ##

* Zatrzymaj mowę podczas nagrywania i czytania dla najnowszych wersji
  mp3directcut;
* Naprawiono pozostały czas odczytu dla nowych wersji NVDA przy użyciu
  Pythona 3.

## Zmiana wersji 19.02 ##

* Dodano konfigurację dodatku w panelu ustawień dostępnym od nvda 2018.2;
* Zmieniono numerację wersji przy użyciu YY. MM (Rok w 2 cyfrach, po którym
  następuje kropka, a następnie miesiąc w 2 cyfrach);
* Dodano kompatybilność z nowym formatem wersjonowania dodatku, pojawił się
  od nvda 2019.1.

## Zmiana w wersji 4.0 ##

* Dodano kompatybilność dodatku z Pythonem 2.7 i 3;
* Poprawiono błąd dotyczący ścieżek dodatku, które zawierają znaki spoza
  łacińskiego alfabetu.

## Zmiana w wersji 3.0 ##

* Użyto modułu gui.guiHelper, aby zapewnić poprawny wygląd okna dialogowego
  konfiguracji dodatku;
* Używany format zamiast %s dla sformatowanych ciągów;
* Wykorzystano zgodność z wytycznymi dotyczącymi wdrażania.

## Zmiana wersji 2.3 ##

* Dodano licencję GPL;
* Zmieniono skrót skryptu podający koniec zaznaczenia z Ctrl + Shift + N na
  Ctrl + Shift + E, ponieważ Ctrl + Shift + N nie działa z najnowszymi
  wersjami mp3DirectCut;
* Dodano skrypt potwierdzający, że wybór został anulowany za pomocą "Ctrl +
  r";
* Wprowadzono pewne poprawki w kodzie appModule "mp3directcut.py".

## Zmiana w wersji 2.2 ##

* Korekta skryptów z podaniem położenia znaczników wyboru.

## Zmiana wersji 2.1.1 ##

* Usunięcie skryptu podającego całkowity czas i dodanie tej informacji do
  skryptu podającego czas, który upłynął;
* Dodano możliwość włączania lub wyłączania ogłoszeń związanych z spacji w
  opcjach konfiguracyjnych modułu, niezależnie od innych ogłoszeń;
* Dodano możliwość włączenia lub wyłączenia zapowiedzi umieszczenia namiotów
  zaznaczenia w opcjach konfiguracyjnych modułu;
* Dodanie ogłoszenia bieżącej części podczas przechodzenia przez punkty
  cięcia;
* Korekta ogłoszeń związanych z pionowymi;
* Dodanie skryptu do otwierania pomocy bieżącego dodatku z "NVDA + H";
* Przesunięcie menu konfiguracyjnego dodatku z menu Narzędzia do menu
  Preferencje NVDA.

## Zmiana w wersji 2.1 ##

* Dodanie skryptu do wokalizacji przechodzącej do następnego punktu podziału
  za pomocą Control+strzałki w prawo;
* Dodanie skryptu do wokalizacji przechodzącej do poprzedniego punktu
  podziału za pomocą Control+strzałki w lewo;
* Dodanie skryptu do wokalizacji przemieszczenia o 4 setne sekundy do
  przodu, z Shift + strzałka w prawo;
* Dodanie skryptu do wokalizacji przemieszczenia 4 setnych sekundy do tyłu,
  z Shift + strzałka w lewo;
* Korekta podsumowania dodatku z 'for mp3DirectCut' na 'mp3DirectCut'.

## Zmiana w wersji 2.0 ##

* Dodanie skryptu, aby poznać pozostały czas za pomocą "Control Shift R";
* Stały czas czytania, w tym godziny;
* Dodano możliwość różnicowania tysięcznych lub setnych części sekundy.

## Zmiana wersji 1.1 ##

* Dodano możliwość włączenia kategorii mp3DirectCut do gestów wejściowych;

    * Będą one widoczne tylko podczas korzystania z oprogramowania
      mp3DirectCut.

* Dodano możliwość włączania lub wyłączania automatycznych wiadomości, w
  menu narzędzi NVDA, pozycja "konfiguracja mp3DirectCut";

## Zmiana w wersji 1.0 ##

* Wstępne wydanie.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=mp3DirectCut


[2]: https://www.nvaccess.org/addonStore/legacy?file=mp3DirectCut
