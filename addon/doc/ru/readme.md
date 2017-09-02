# mp3DirectCut #

*	 Автор(ы) : Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
*	 Загрузить [стабильную версию][1]
*	 Загрузить [разрабатываемую версию][2]

# Презентация #

Это дополнение улучшает доступность программы mp3DirectCut в NVDA.

It has been tested with versions of mp3DirectCut ranging from 212 up to 223.

## Горячие клавиши ##

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

## Изменение версии 2.2 ##

*	 Исправление скриптов для предоставления расположения меток выделения.

## Изменение версии 2.1.1 ##

*	 Удалён скрипт, предоставляющий общее время, и эта информация добавлена в
   скрипт оставшегося времени;
*	 Added the ability to enable or disable the announcements related to the
   space key in the module's configuration options, separately from other
   announcements;
*	 Added the ability to enable or disable the announcement of placement of
   the selection marqueures in the module's configuration options;
*	 Adding the announcement of the current part when moving through the
   cutting points;
*	 Исправление объявлений, касающихся клавиш вертикальных стрелок;
*	 Добавлен скрипт для открытия справки текущего дополнения при запущеной
   программе 'NVDA+H';
*	 Перемещено меню конфигурации из меню Сервис в меню параметров программы
   NVDA.

## Изменение версии 2.1 ##

*	 Adding a script to vocalize moving to the next splitting point with
   Control+Right Arrow;
*	 Adding a script to vocalize moving to the previous splitting point with
   Control+Left Arrow;
*	 Adding a script to vocalize the displacement of 4 hundredths of second
   ahead, with Shift+Right Arrow;
*	 Adding a script to vocalize the displacement of 4 hundredths of second
   back, with Shift+Left Arrow;
*	 Исправлена суммарная информация дополнения  С 'for mp3DirectCut' на
   'mp3DirectCut'.

## Изменение версии 2.0 ##

*	 Добавлен скрипт для выяснения оставшегося времени 'Control Shift R';
*	 Исправлено чтение длительности, включая часы;
*	 Добавлена возможность разделять тысячные или сотые доли секунд.

## Изменение версии 1.1 ##

*	 Добавлена возможность включения категории mp3DirectCut в жесты ввода;
	*	 Она будет видна только во время использования программы mp3DirectCut.
*	 Добавлена возможность включить или отключить автоматические сообщения, в меню параметров NVDA, пункт 'mp3DirectCut addon configuration';

## Изменение версии 1.0 ##

*	 Первоначальная версия.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
