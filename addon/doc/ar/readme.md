# mp3DirectCut #

*	 المطوِّرون: عبْدُ الكريم, ريمي, عبدُ الله زين الدين, Jean-François COLAS
*	 تحميل [نسخة جاهزة][1]
*	 تحميل [نسخة في طور الإنجاز][2]

# تقديم #

هذه الإِضافةُ البرمجيةُ سَتُمَكِّنُكُم من تحسين القُدرةِ على استعمال
البرنامج mp3DirectCut مع NVDA.

It has been tested with versions of mp3DirectCut ranging from 212 up to 223.

## اختصارات لوحة المفاتيح ##

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

## مستجدات النسخة 2.2 ##

*	 تصحيح البرامج التي تُعطي أماكن تواجد مؤشرات التحديد.

## مستجدات النسخة 2.1.1 ##

*	 إزالةُ السكريبت الذي يُعطي الوقت الكامل و إضافة هذه المعلومة إلى السكريبت
   الذي يعطي الوقت المسموع;
*	 إضافةُ إمكانيةِ تشغيل أو تعطيل الإعلانات المتعلقة بزر المسافة, في إعدادات
   الإضافة البرمجية, مع فصلها عن الإعلانات الأُخرى;
*	 إضافةُ إمكانيةِ تشغيل أو تعطيل الإعلان الخاص بصِحَّة وضع مؤَ"شِرات
   التحديد, في إعدادات الإضافة البرمجية;
*	 إضافةُ إعلان الجُزْءِ الحالي عند التنقل ما بين نِقط القطع;
*	 تصحيح الإعلانات الخاصة بالأزرار : 'upArrow' و 'downArrow';
*	 إضافةُ إمكانيةِ فتح ملف المساعدة للإضافة البرمجية الجارية بالضغط على
   'NVDA+H';
*	 نقلُ القائمةِ الخاصة بإعدادات الإضافة البرمجية من قائمة الإعدادات إلى
   قائمة التفضيلات.

## مستجدات النسخة 2.1 ##

*	 إضافةُ إمكانيةِ معرفةِ مكان تواجد نقطة القطع المقبلة بالضغط على
   'Ctrl+Right Arrow';
*	 إضافةُ إمكانيةِ معرفةِ مكان تواجد نقطة القطع السابقة بالضغط على
   'Ctrl+Left Arrow';
*	 إضافةُ النُطْقِ عند التنقل أربع أجزاء من المائة إلى الأمام بالضغط على
   'Shift+Right Arrow';
*	 إضافةُ النطْقِ عند التنقل أربع أجزاء من المائة إلى الوراء بالضغط على
   'Shift+Left Arrow';
*	 تصحيح المفتاح summary للإضافة البرمجية من 'من أجل البرنامج mp3DirectCut'
   إلى 'mp3DirectCut'.

## مستجدات النسخة 2.0 ##

*	 إضافة إمكانيةِ معرفة المدة المتبقيةِ بالضغط على الإختصار 'Ctrl Shift R';
*	 تصحيح قِراءةِ المدة التي تفُوق الساعة;
*	 إضافةِ إمكانية التفريق بين الأجزاِ من المائة و الأجزاء من الإلف.

## مستجدات النسخة 1.1 ##

*	 إضافة صِنْف mp3DirectCut إلى قائمة تخصيص الإختصارات في التفضيلات;
	*	 لا يمكن الوصول إليها إلا لَمّا سيكون البرنامج mp3DirectCut مفتوحا.
*	 إضافة إمكانية تفعيل أو تعطيل القِراءةِ الأُطُوماتيكية ضمن قائمة أدوات NVDA, عند 'إعدادات الإضافة البرمجية mp3DirectCut'.

## مستجدات النسخة 1.0 ##

*	 النسخة الأولى.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
