# mp3DirectCut-2.2

*	 Author(s) : Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
*	 Download [stable version][1]
*	 Download [development version][2]

# Presentation #

This add-on improves the accessibility of the software mp3DirectCut with NVDA.

It has been tested with versions of mp3DirectCut ranging from 212 up to 223.

## Keyboard shortcuts ##

This addon offers the following commands, which you can change by going to the menu Preferences / Input Gestures' in the category 'mp3DirectCut':

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

## Change for version 2.2 ##

*	 Adding a script to confirm that the selection has been canceled with 'Ctrl+r';
*	 Making some correction in the code of the appModule 'mp3directcut.py';
*	 Correction of the scripts giving the selection markers' locations.

## Change for version 2.1.1 ##

*	 Removing the script giving the total time and adding this information to the script giving the elapsed time;
*	 Added the ability to enable or disable the announcements related to the space key in the module's configuration options, separately from other announcements;
*	 Added the ability to enable or disable the announcement of placement of the selection marqueures in the module's configuration options;
*	 Adding the announcement of the current part when moving through the cutting points;
*	 Correction of announcements related to vertical keys;
*	 Adding a script to open the help of the current add-on with 'NVDA+H';
*	 Displacement of the add-on's configuration menu from the Tools menu to the Preferences menu of NVDA.

## Change for version 2.1 ##

*	 Adding a script to vocalize moving to the next splitting point with Control+Right Arrow;
*	 Adding a script to vocalize moving to the previous splitting point with Control+Left Arrow;
*	 Adding a script to vocalize the displacement of 4 hundredths of second ahead, with Shift+Right Arrow;
*	 Adding a script to vocalize the displacement of 4 hundredths of second back, with Shift+Left Arrow;
*	 Correction of the addon's summary from 'for mp3DirectCut' to 'mp3DirectCut'.

## Change for version 2.0 ##

*	 Adding a script to know the remaining time with 'Control Shift R';
*	 Fixed reading durations including hours;
*	 Added ability to differentiate thousandths or hundredths of seconds.

## Change for version 1.1 ##

*	 Added the ability to include the mp3DirectCut category into the Input Gestures;
	*	 They will be visible only during use of the mp3DirectCut software.
*	 Added the ability to enable or disable automatic messages, in the tools menu of NVDA, item 'mp3DirectCut configuration';

## Change for version 1.0 ##

*	 Initial version.

[1]: http://cyber25.free.fr/nvda-addons/mp3DirectCut-2.2.nvda-addon

[2]: http://cyber25.free.fr/nvda-addons/mp3DirectCut-2.2-dev.nvda-addon
