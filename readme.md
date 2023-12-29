# mp3DirectCut

* Author(s) : Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
* Download [stable version][1]
* Download [development version][2]

# Presentation #

This add-on improves the accessibility of the software mp3DirectCut with NVDA.

It has been tested with versions of mp3DirectCut ranging from 212 up to 233.

## Keyboard shortcuts ##

This addon offers the following commands:

* B

    * Used to confirm correct placement of the marker of the beginning of the selection B.

* Ctrl+Shift+B

    * Used to indicate the position of the marker of the beginning of selection B.
    * Double pressure lets give you the duration of the selection.

* Ctrl+Shift+D

    * Gives the duration from the beginning of the file to the current position of the playback cursor.
    * Double pressure lets give you the total duration.

* Ctrl+R

    * Confirms that the selection has been canceled.

* Ctrl+Shift+R

    * Gives the time remaining from the current position of the playback cursor to the end of the file.

* Ctrl+Shift+E

    * Used to indicate the position of the marker of the end of selection N.
    * Double pressure gives recapitulatif positions B and N, and the duration of the selection.

* Ctrl+Shift+P

    * Give the reference of the actual part and the total number of parts in the current file.

* Ctrl+Shift+Space

    * Used to determine the current level of the vu-meter, during recording.
    * Double pressure reset it.

* Down Arrow

    * Lets you see the current position of the playhead.
    * This command also position the cursor at the location of the marker of the end of selection N, while giving the location of this marker if a selection has been made.
    * In the volume dialog box, vocalise the next value that can be reached generally with downArrow.
    * This value is not vocalized default.

* End

    * Moves the playback cursor at the end of the current file and give the total time.

* Home

    * Moves the playback cursor at the beginning of the current file.

* Left Arrow

    * Lets make a brief return back of one second during playback, while giving the current duration.
    * This duration is configurable in the options of mp3directcut.

* N

    * Used to confirm correct placement of the marker of the end of the selection N.

* Page Down

    * Lets make a leap forward of 10 seconds during playback, while giving the current duration.
    * This duration is configurable in the options of mp3directcut.

* Page Up

    * Lets make a return back of 10 seconds during playback, while giving the current duration.
    * This duration is configurable in the options of mp3directcut.

* R

    * Allows to prepare a record and whether you can press spacebar to start.

* Right Arrow

    * Lets do a brief forward of one second during playback, while giving the current duration.
    * This duration is configurable in the options of mp3directcut.

* Ctrl+Right Arrow

    * Moves to the next splitting point, while giving the current duration.

* Ctrl+Left Arrow

    * Moves to the previous splitting point, while giving the current duration.

* Shift+Right Arrow

    * Lets do a brief forward of four hundredths of seconds during playback, while giving the current duration.

* Shift+Left Arrow

    * Lets do a brief backwards of four hundredths of seconds during playback, while giving the current duration.

* S

    * Used to stop the reading and give the current duration.

* Space

    * If the recording is ready, start this recording.
    * If a recording is in progress, stop it by positioning the cursor at the beginning.
    * If a file is loaded, start the reading.
    * If a read is in progress, allows to do a pause by giving current duration.
    * If read is paused, allows to restart the reading from the current location.

* Up Arrow

    * Lets you see the current position of the playhead.
    * This command also position the cursor at the location of the marker of the beginning of selection B, while giving the location of this marker if a selection has been made.
    * In the volume dialog box, vocalise the previous value that can be reached generally with upArrow.
    * This value is not vocalized default.

* NVDA+H

    * Lets open the help of the current add-on.

## Compatibility ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3 and beyond.

## Changes for 20231229.0.0 ##

* Added a backward compatible implementation to support speak on demand mode, which will soon be available with nvda-2024.1.

## Changes for 20231007.0.0 ##

* After placing the cutting points and after opening the cutting properties window, with "Ctrl+N", adding accessibility to the title of this window by indicating the part index.
* In reading mode, after moving the start or end markers of selections with keys 1 to 6 of the alphanumeric pad, addition of automatic start of reading from the new position;
* Fixed a bug that occurred when consulting the remaining time with "control+shift+r" from the beginning of the track.

## Changes for 20230728.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support annotations introduced in Python 3.

## Changes for 20230607.0.0 ##

* Added the following workflows:
 * auto-update-translations - to automatically update translations from NVDA's translation system.
 * release-on-tag..yaml: to build and publish the addon as soon as a new tag is pushed;
 * manual-release.yaml: to build and release new versions of the add-on manually.
* Updated translations.

## Changes for version 20230508.0.0 and beyond ##

* • Changed version number, minimum NVDA version and download link according to store conventions/requirements.

## Change for version 20.12 ##

* Stop speech during recording and reading for the latest versions of mp3directcut;
* Fixed reading remaining time for new versions of NVDA using Python 3.

## Change for version 19.02 ##

* Added the add-on's configuration in the settings panel available since nvda 2018.2;
* Changed version numbering using YY.MM (The year in 2 digits, followed by a dot, followed by the month in 2 digits);
* Added compatibility with the new versioning format of add-on, appeared since nvda 2019.1.

## Change for version 4.0 ##

* Added the Compatibility of the add-on with both Python 2.7 and 3;
* Fixed a bug with add-on paths that contain non-ASCII characters.

## Change for version 3.0 ##

* Used the gui.guiHelper module to ensure the correct appearance of the addon's configuration dialog;
* Used format instead of %s for formatted strings;
* Used compliance with guidelines for implementation.

## Change for version 2.3 ##

* Added the GPL license to the addon;
* Changed the shortcut of the script giving the end of selection from Ctrl + Shift + N to Ctrl + Shift + E because Ctrl + Shift + N doesn't work with the latest versions of mp3DirectCut;
* Added a script to confirm that the selection has been canceled with 'Ctrl+r';
* Made some corrections in the code of the appModule 'mp3directcut.py'.

## Change for version 2.2 ##

* Correction of the scripts giving the selection markers' locations.

## Change for version 2.1.1 ##

* Removing the script giving the total time and adding this information to the script giving the elapsed time;
* Added the ability to enable or disable the announcements related to the space key in the module's configuration options, separately from other announcements;
* Added the ability to enable or disable the announcement of placement of the selection marqueures in the module's configuration options;
* Adding the announcement of the current part when moving through the cutting points;
* Correction of announcements related to vertical keys;
* Adding a script to open the help of the current add-on with 'NVDA+H';
* Displacement of the add-on's configuration menu from the Tools menu to the Preferences menu of NVDA.

## Change for version 2.1 ##

* Adding a script to vocalize moving to the next splitting point with Control+Right Arrow;
* Adding a script to vocalize moving to the previous splitting point with Control+Left Arrow;
* Adding a script to vocalize the displacement of 4 hundredths of second ahead, with Shift+Right Arrow;
* Adding a script to vocalize the displacement of 4 hundredths of second back, with Shift+Left Arrow;
* Correction of the addon's summary from 'for mp3DirectCut' to 'mp3DirectCut'.

## Change for version 2.0 ##

* Adding a script to know the remaining time with 'Control Shift R';
* Fixed reading durations including hours;
* Added ability to differentiate thousandths or hundredths of seconds.

## Change for version 1.1 ##

* Added the ability to include the mp3DirectCut category into the Input Gestures;

    * They will be visible only during use of the mp3DirectCut software.

* Added the ability to enable or disable automatic messages, in the tools menu of NVDA, item 'mp3DirectCut configuration';

## Change for version 1.0 ##

* Initial version.

[1]: https://github.com/abdel792/mp3DirectCut/releases/download/v23.12.29/mp3DirectCut-20231229.0.0.nvda-addon

[2]: https://github.com/abdel792/mp3DirectCut/releases/download/v23.12.29-beta/mp3DirectCut-20231229.0.1.nvda-addon
