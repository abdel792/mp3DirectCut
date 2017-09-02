# mp3DirectCut #

*	 Автори: Abdel, Rémy, Abdellah Zineddine, Jean-François COLAS
*	 Изтегляне на [стабилна версия][1]
*	 Изтегляне на [работна версия][2]

# Представяне #

Тази добавка подобрява достъпността на програмата mp3DirectCut при работа с
NVDA.

It has been tested with versions of mp3DirectCut ranging from 212 up to 223.

## Клавишни комбинации ##

This addon offers the following commands:

*	B
	*	Used to confirm correct placement of the marker of the beginning of the selection B.
*	Ctrl+Shift+B
	*	Used to indicate the position of the marker of the beginning of selection B.
	*	Double pressure lets give you the duration of the selection.
*	Ctrl+Shift+D
	*	Gives the duration from the beginning of the file to the current position of the playback cursor.
	*	Double pressure lets give you the total duration.
*	Ctrl+R
	*	Confirms that the selection has been canceled.
*	Ctrl+Shift+R
	*	Gives the time remaining from the current position of the playback cursor to the end of the file.
*	Ctrl+Shift+E
	*	Used to indicate the position of the marker of the end of selection N.
	*	Double pressure gives recapitulatif positions B and N, and the duration of the selection.
*	Ctrl+Shift+P
	*	Give the reference of the actual part and the total number of parts in the current file.
*	Ctrl+Shift+Space
	*	Used to determine the current level of the vu-meter, during recording.
	*	Double pressure reset it.
*	Down Arrow
	*	Lets you see the current position of the playhead.
	*	This command also position the cursor at the location of the marker of the end of selection N, while giving the location of this marker if a selection has been made.
	*	In the volume dialog box, vocalise the next value that can be reached generally with downArrow.
	*	This value is not vocalized default.
*	End
	*	Moves the playback cursor at the end of the current file and give the total time.
*	Home
	*	Moves the playback cursor at the beginning of the current file.
*	Left Arrow
	*	Lets make a brief return back of one second during playback, while giving the current duration.
	*	This duration is configurable in the options of mp3directcut.
*	N
	*	Used to confirm correct placement of the marker of the end of the selection N.
*	Page Down
	*	Lets make a leap forward of 10 seconds during playback, while giving the current duration.
	*	This duration is configurable in the options of mp3directcut.
*	Page Up
	*	Lets make a return back of 10 seconds during playback, while giving the current duration.
	*	This duration is configurable in the options of mp3directcut.
*	R
	*	Allows to prepare a record and whether you can press spacebar to start.
*	Right Arrow
	*	Lets do a brief forward of one second during playback, while giving the current duration.
	*	This duration is configurable in the options of mp3directcut.
*	Ctrl+Right Arrow
	*	Moves to the next splitting point, while giving the current duration.
*	Ctrl+Left Arrow
	*	Moves to the previous splitting point, while giving the current duration.
*	Shift+Right Arrow
	*	Lets do a brief forward of four hundredths of seconds during playback, while giving the current duration.
*	Shift+Left Arrow
	*	Lets do a brief backwards of four hundredths of seconds during playback, while giving the current duration. 
*	S
	*	Used to stop the reading and give the current duration.
*	Space
	*	If the recording is ready, start this recording.
	*	If a recording is in progress, stop it by positioning the cursor at the beginning.
	*	If a file is loaded, start the reading.
	*	If a read is in progress, allows to do a pause by giving current duration.
	*	If read is paused, allows to restart the reading from the current location.
*	Up Arrow
	*	Lets you see the current position of the playhead.
	*	This command also position the cursor at the location of the marker of the beginning of selection B, while giving the location of this marker if a selection has been made.
	*	In the volume dialog box, vocalise the previous value that can be reached generally with upArrow.
	*	This value is not vocalized default.
*	NVDA+H
	*	Lets open the help of the current add-on.

## Change for version 3.0 ##

*	 Used the gui.guiHelper module to ensure the correct appearance of the
   addon's configuration dialog;
*	 Used format instead of %s for formatted strings;
*	 Used compliance with guidelines for implementation.

## Change for version 2.3 ##

*	 Added the GPL license to the addon;
*	 Changed the shortcut of the script giving the end of selection from Ctrl
   + Shift + N to Ctrl + Shift + E because Ctrl + Shift + N doesn't work
   with the latest versions of mp3DirectCut;
*	 Added a script to confirm that the selection has been canceled with
   'Ctrl+r';
*	 Maked some correction in the code of the appModule 'mp3directcut.py'.

## Промени във версия 2.2 ##

*	 Поправка на скриптовете даващи информация за позицията на маркерите за
   селекция.

## Промени във версия 2.1.1 ##

*	 Премахната е командата за съобщаване на общото времетраене, а тази
   информация е добавена към командата за съобщаване на изминалото
   времетраене;
*	 Добавена е възможност да разрешите или забраните съобщенията, свързани с
   клавиша за интервал в прозореца с настройките на добавката, отделно от
   другите съобщения;
*	 Добавена е възможност да разрешите или забраните съобщаването за
   поставянето на маркерите за селекция в прозореца с настройките на
   добавката;
*	 Добавено е съобщаване на текущата част, при преминаване през точките за
   разделяне;
*	 Корекция на съобщенията, свързани с вертикалните клавиши;
*	 Добавена е команда за отваряне на помощната документация за добавката с
   'NVDA+H';
*	 Преместен е пункта в менюто за конфигуриране на добавката от меню
   "Инструменти" в меню "Настройки" на NVDA.

## Промени във версия 2.1 ##

*	 Добавена е функция за съобщаване на преместването до следващата точка за
   разделяне с Control+Стрелка надясно;
*	 Добавена е функция за съобщаване на преместването до предишната точка за
   разделяне с Control+Стрелка наляво;
*	 Добавена е функция за съобщаване на преминаването с 4 стотни от секундата
   напред чрез Shift+Стрелка надясно;
*	 Добавена е функция за съобщаване на преминаването с 4 стотни от секундата
   назад чрез Shift+Стрелка наляво;
*	 Корекция в резюмето за добавката от "за mp3DirectCut" на "mp3DirectCut".

## Промени във версия 2.0 ##

*	 Добавена е команда за съобщаване на оставащото времетраене с
   Control+Shift+R;
*	 Поправено е четенето на времетраенето съдържащо часове;
*	 Добавена е способността за открояване на хилядни и стотни от секундата.

## Промени във версия 1.1 ##

*	Вече може да се променят командите за добавката от категорията "mp3DirectCut" в прозореца "Жестове на въвеждане" на NVDA;
	*	Те ще се показват там само ако е стартирана програмата "mp3DirectCut".
*	Добавена е възможността за разрешаването и забраняването на автоматичните съобщения, в меню "Инструменти" на NVDA, пункта "Настройки на mp3DirectCut";

## Промени във версия 1.0 ##

*	 Първо издание.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
