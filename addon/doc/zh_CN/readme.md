# mp3DirectCut-NVDA支持插件 #

* 作者(s) : Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
* 下载 [稳定版][1]
* 下载 [开发板][2]

# 插件介绍 #

此插件改进了NVDA使用mp3DirectCut的可访问性。

插件已经过mp3DirectCut版本的测试，范围从212到223。

## 键盘快捷键 ##

此插件提供以下快捷键：

* B

    * Used to confirm correct placement of the marker of the beginning of
      the selection B.

* Ctrl+Shift+B

    * Used to indicate the position of the marker of the beginning of
      selection B.
    * Double pressure lets give you the duration of the selection.

* Ctrl+Shift+D

    * Gives the duration from the beginning of the file to the current
      position of the playback cursor.
    * Double pressure lets give you the total duration.

* Ctrl+R

    * 确认所选内容已被取消。

* Ctrl+Shift+R

    * Gives the time remaining from the current position of the playback
      cursor to the end of the file.

* Ctrl+Shift+E

    * Used to indicate the position of the marker of the end of selection N.
    * Double pressure gives recapitulatif positions B and N, and the
      duration of the selection.

* Ctrl+Shift+P

    * Give the reference of the actual part and the total number of parts in
      the current file.

* Ctrl+Shift+Space

    * Used to determine the current level of the vu-meter, during recording.
    * Double pressure reset it.

* 下箭头

    * Lets you see the current position of the playhead.
    * This command also position the cursor at the location of the marker of
      the end of selection N, while giving the location of this marker if a
      selection has been made.
    * In the volume dialog box, vocalise the next value that can be reached
      generally with downArrow.
    * This value is not vocalized default.

* 动作按钮: 结束

    * Moves the playback cursor at the end of the current file and give the
      total time.

* 动作按钮: 第一张

    * Moves the playback cursor at the beginning of the current file.

* 左箭头

    * Lets make a brief return back of one second during playback, while
      giving the current duration.
    * This duration is configurable in the options of mp3directcut.

* N

    * Used to confirm correct placement of the marker of the end of the
      selection N.

* Page Down

    * Lets make a leap forward of 10 seconds during playback, while giving
      the current duration.
    * This duration is configurable in the options of mp3directcut.

* Page Up

    * Lets make a return back of 10 seconds during playback, while giving
      the current duration.
    * This duration is configurable in the options of mp3directcut.

* R

    * Allows to prepare a record and whether you can press spacebar to
      start.

* 右箭头

    * Lets do a brief forward of one second during playback, while giving
      the current duration.
    * This duration is configurable in the options of mp3directcut.

* Ctrl+Right Arrow

    * Moves to the next splitting point, while giving the current duration.

* Ctrl+Left Arrow

    * Moves to the previous splitting point, while giving the current
      duration.

* Shift+Right Arrow

    * Lets do a brief forward of four hundredths of seconds during playback,
      while giving the current duration.

* Shift+Left Arrow

    * Lets do a brief backwards of four hundredths of seconds during
      playback, while giving the current duration.

* S

    * Used to stop the reading and give the current duration.

* Space

    * If the recording is ready, start this recording.
    * If a recording is in progress, stop it by positioning the cursor at
      the beginning.
    * If a file is loaded, start the reading.
    * If a read is in progress, allows to do a pause by giving current
      duration.
    * If read is paused, allows to restart the reading from the current
      location.

* 上箭头

    * Lets you see the current position of the playhead.
    * This command also position the cursor at the location of the marker of
      the beginning of selection B, while giving the location of this marker
      if a selection has been made.
    * In the volume dialog box, vocalise the previous value that can be
      reached generally with upArrow.
    * This value is not vocalized default.

* NVDA+H

    * 添加快捷键使用'NVDA + H'打开当前插件的帮助;

## 兼容性 ##

* 此插件与2016.4到2019.1的NVDA版本兼容。

## 19.02版的更改 ##

* 在 nvda 2018.2新增的设置面板中添加了插件的配置;
* 现在使用YY.MM形式的版本号（年份为2位数，后跟一个点，后跟月份为2位数）;
* 兼容nvda 2019.1的插件新版本格式。

## 版本4.0 ##

* 添加了Python 2.7和3的插件的兼容性;
* 修复了包含非ASCII字符的附加路径的错误。

## 版本3.0 ##

* 使用gui.guiHelper模块确保插件配置对话框的正确外观;
* 格式化字符串使用格式而不是％s;
* 使用遵守实施准则。

## 版本2.3 ##

* 给插件添加了GPL许可证;
* 将选择结束的脚本快捷方式从Ctrl + Shift + N更改为Ctrl + Shift + E，因为Ctrl + Shift +
  N不能与最新版本的mp3DirectCut一起使用;
* 添加了一个脚本，以确认已使用“Ctrl + r”取消选择;
* 在appModule'mp3directcut.py'的代码中做了一些更正。

## 版本2.2 ##

* 更正给出选择标记位置的脚本。

## 版本2.1.1 ##

* 删除脚本，给出总时间并将此信息添加到脚本中，给出经过的时间;
* 添加了与其他公告分开启用或禁用模块配置选项中与空格键相关的通知的功能;
* 添加了在模块的配置选项中启用或禁用选择范围放置的通知的功能;
* 在切割点移动时添加当前零件的通知;
* 更正与垂直键相关的公告;
* 添加脚本以使用'NVDA + H'打开当前加载项的帮助;
* 将插件的配置菜单从“工具”菜单移动到NVDA的“首选项”菜单。

## 版本2.1 ##

* 使用Control + Right Arrow添加脚本以发声移动到下一个分割点;
* 使用Control +左光标添加脚本以发声移动到上一个分割点;
* 使用Shift +右光标添加一个脚本，用于向前方播放百分之四秒的位移;
* 使用Shift +左光标添加一个脚本来发出第二百分之二秒位移的位移;
* 将“for mp3DirectCut”中的插件摘要更正为“mp3DirectCut”。

## 版本2.0 ##

* Adding a script to know the remaining time with 'Control Shift R';
* 固定阅读时间，包括小时;
* 增加了区分千分之一秒或百分之一秒的功能。

## 版本1.1 ##

* Added the ability to include the mp3DirectCut category into the Input
  Gestures;

    * They will be visible only during use of the mp3DirectCut software.

* Added the ability to enable or disable automatic messages, in the tools
  menu of NVDA, item 'mp3DirectCut configuration';

## 版本1.0 ##

* 发布初始版本

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=mp3dc

[2]: https://addons.nvda-project.org/files/get.php?file=mp3dc-dev
