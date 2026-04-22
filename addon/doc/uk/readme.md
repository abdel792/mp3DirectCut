# mp3DirectCut

- Author(s) : Abdel, Rémy, Abdellah zineddine, Jean-François COLAS.

# Презентація

Цей додаток покращує доступність програми mp3DirectCut з NVDA.

Цей додаток перевірявся з версіями mp3DirectCut від 212 до 223.

## Гарячі клавіші

Цей додаток пропонує такі комади:

- B

  - Використовується для підтвердження правильного розміщення маркера
    початку виділення B.

- Ctrl+Shift+B

  - Використовується, щоб вказати позицію маркера початку виділення B.
  - Подвійне натискання дозволяє вказати тривалість виДІЛЕного елементА.

- Ctrl+Shift+D

  - Вказує тривалість від початку файлу до поточного положення курсора
    відтворення.
  - Подвійне натискання дозволяє визначити загальну тривалість.

- Ctrl+R

  - Підтверджує, що виДІЛЕННЯ було скасовано.

- Ctrl+Shift+R

  - Вказує час, що залишився від поточного положення курсора відтворення
    до кінця файлу.

- Ctrl+Shift+E

  - Використовується, щоб вказати позицію маркера кінця виділення N.
  - Подвійне натискання надає повторення позицій B і N, а також тривалість
    виДІЛЕного елемента.

- Ctrl+Shift+P

  - Вказує на певну частину файлу і загальну кількість частин цього файлу.

- Ctrl+Shift+пробіл

  - Використовується для визначення поточного рівня vu-meter під час
    запису.
  - Подвійне натискання скидає його.

- Стрілка вниз

  - Дозволяє побачити поточне положення заголовка відтворення.
  - Ця команда також поміщає курсор в положення маркера кінця виділення N,
    вказуючи при цьому місце розташування цього маркера, якщо виділення
    було зроблено.
  - В діалозі гучності озвучується наступне значення, яке може бути
    виконане за допомогою стрілки вниз.
  - Це значення початково не озвучується.

- В кінець

  - Переміщує курсор відтворення в кінець поточного файлу і вказує
    загальну тривалість.

- На початок

  - Переміщує курсор відтворення на початок поточного файлу.

- Стрілка вліво

  - Дозволяє зробити коротке перемотування назад на 1 секунду під час
    відтворення, вказавши поточну тривалість.
  - Ця тривалість налаштовується в налаштуваннях mp3DirectCut.

- N

  - Використовується для підтвердження правильного розміщення маркера
    кінця виділення N.

- Сторінка вниз

  - Дозволяє промотати вперед на 10 секунд під час відтворення, вказавши
    поточну тривалість.
  - Ця тривалість налаштовується в налаштуваннях mp3DirectCut.

- Сторінка вгору

  - Дозволяє промотати назад на 10 секунд під час відтворення, вказавши
    поточну тривалість.
  - Ця тривалість налаштовується в налаштуваннях mp3DirectCut.

- R

  - Дозволяє підготувати запис і визначити, чи можна натискати пробіл щоб
    почати.

- Стрілка вправо

  - Дозволяє зробити коротке перемотування на 1 секунду вперед під час
    відтворення, вказавши поточну тривалість.
  - Ця тривалість налаштовується в налаштуваннях mp3DirectCut.

- Ctrl+стрілка вправо

  - Переходить до наступної точки поділу, вказавши поточну тривалість.

- Ctrl+стрілка вліво

  - Переходить до попередньої точки поділу, вказавши поточну тривалість.

- Shift+стрілка вправо

  - Дозволяє зробити коротке перемотування вперед на чотири сотих секунди
    під час відтворення, вказавши поточну тривалість.

- Shift+стрілка вліво

  - Дозволяє зробити коротке перемотування назад на чотири сотих секунди
    під час відтворення, вказавши поточну тривалість.

- S

  - Використовується для зупинки зчитування і вказування поточної
    тривалості.

- Пробіл

  - Якщо запис готовий, запустити цей запис.
  - Якщо запис триває, зупиніть його, встановивши курсор на початок.
  - Якщо файл завантажено, почніть зчитування.
  - Якщо зчитування триває, дозволяється поставити паузу, вказавши поточну
    тривалість.
  - Якщо зчитування призупинено, дозволяється перезапустити зчитування з
    поточного місця.

- Стрілка вгору

  - Дозволяє побачити поточне положення заголовка відтворення.
  - Ця команда також поміщає курсор в місце розташування маркера початку
    виділення B, при цьому вказується місце розташування цього маркера,
    якщо виділення було зроблено.
  - В діалозі гучності озвучується наступне значення, яке може бути
    виконане за допомогою стрілки вгору.
  - Це значення початково не озвучується.

- NVDA+H

  - Дозволяє відкрити довідку поточного додатка.

## Сумісність

- This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20240327.0.0

- Fixed a bug that caused a log error when reloading plugins, thanks to Rob,
  from nvda-addons mailing list;

## Changes for 20240326.0.0

- Updated compatibility for nvda-2024.1.;
- Deleted download link from readme, the download link for future updates
  will now only be available from the add-on store.

## Changes for 20231229.0.0

- Added a backward compatible implementation to support speak on demand
  mode, which will soon be available with nvda-2024.1.

## Changes for 20231007.0.0

- After placing the cutting points and after opening the cutting properties
  window, with "Ctrl+N", adding accessibility to the title of this window by
  indicating the part index.
- In reading mode, after moving the start or end markers of selections with
  keys 1 to 6 of the alphanumeric pad, addition of automatic start of
  reading from the new position;
- Fixed a bug that occurred when consulting the remaining time with
  "control+shift+r" from the beginning of the track.

## Changes for 20230728.0.0

- Applied the flake8 and mypy rules to the code;
- Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.

## Changes for 20230508.0.0 and beyond

- Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.
- auto-update-translations - to automatically update translations from NVDA's translation system.
- release-on-tag..yaml: to build and publish the addon as soon as a new tag is pushed;
- manual-release.yaml: to build and release new versions of the add-on manually.
- Updated translations.

## Зміни у версії 20.12

- Зупинено мовлення під час запису та зчитування в новіших версіях
  mp3DirectCut;

## Зміни у версії 19.02

- Додано конфігурацію додатка в панель налаштувань, яка  доступна, починаючи
  з NVDA 2018.2;
- Змінено нумерацію версій з використанням РР.ММ (рік з 2 цифр, потім ., а
  потім місяць з 2 цифр);

## Зміни у версії 4.0

- Додано сумісність додатка з Python 2.7  і 3;
- Виправлено помилку з додатковими шляхами, які містять символи, відмінні
  від ASCII.
- Added compatibility with the new versioning format of add-on, appeared since nvda 2019.1.

## Зміни у версії 3.0

- Використовується модуль gui.guiHelper  для забезпечення правильного
  відображення діалогу конфігурації додатка;
- Використовується формат замість %s для форматованих рядків;

## Зміни у версії 2.3

- Додано ліцензію GPL для додатка;
- Змінено комбінацію клавіш скрипта, який вказує кінець виділення, з Ctrl +
  Shift + N на Ctrl + Shift + E , оскільки комбінація клавіш Ctrl + Shift +
  N  не працює з новішими версіями mp3DirectCut;
- Додано сценарій для підтвердження скасування виділення за допомогою
  'Ctrl+r';

## Зміни у версії 2.2

- Виправлено скрипти, які вказують розташування маркерів виділення.
- Changed the shortcut of the script giving the end of selection from Ctrl + Shift + N to Ctrl + Shift + E because Ctrl + Shift + N doesn't work with the latest versions of mp3DirectCut;
- Added a script to confirm that the selection has been canceled with 'Ctrl+r';
- Made some corrections in the code of the appModule 'mp3directcut.py'.

## Зміни у версії 2.1.1

- Видаленно скрипт із зазначенням загального часу і додано цю інформацію до
  скрипта, який вказує час, що залишився;

## Зміни у версії 2.1

- Додано скрипт для озвучення переміщення до наступної точки поділу за
  допомогою Control+стрілка вправо;
- Додано скрипт для озвучення переміщення до попередньої точки поділу за
  допомогою Control+стрілка вліво;
- Додано опис для озвучування перемотування на 4 сотих секунди вперед за
  допомогою Shift+стрілка вправо;
- Додано опис для озвучування перемотування на 4 сотих секунди назад за
  допомогою Shift+стрілка вліво;
- Виправлено назву додатка з 'for mp3DirectCut'  на 'mp3DirectCut'.
- Adding a script to open the help of the current add-on with 'NVDA+H';
- Displacement of the add-on's configuration menu from the Tools menu to the Preferences menu of NVDA.

## Зміни у версії 2.0

- Додано скрипт для визначення часу що залишився за допомогою 'Control Shift
  R';
- Виправлено зчитування тривалості, включаючи години;
- Додано можливість розрізняти тисячні або соті частки секунди.
- Adding a script to vocalize the displacement of 4 hundredths of second back, with Shift+Left Arrow;
- Correction of the addon's summary from 'for mp3DirectCut' to 'mp3DirectCut'.

## Зміни у версії 1.1

- Додано можливість включення категорії mp3DirectCut в жести вводу;
- Додано можливість вмикати або вимикати автоматичні повідомлення в меню
  інструментів NVDA, розділ 'mp3DirectCut configuration';
- Added ability to differentiate thousandths or hundredths of seconds.

## Зміни у версії 1.0

- Перша версія.

  - They will be visible only during use of the mp3DirectCut software.

- Added the ability to enable or disable automatic messages, in the tools menu of NVDA, item 'mp3DirectCut configuration';

## Change for version 1.0

- Initial version.
