# mp3DirectCut-NVDA支持插件 #

* Author(s) : Abdel, Rémy, Abdellah zineddine, Jean-François COLAS
* 下载 [稳定版][1]
* 下载 [开发板][2]

# 插件介绍 #

此插件改进了mp3DirectCut的无障碍支持。

插件已经过mp3DirectCut版本的测试，范围从212到223。

## 键盘快捷键 ##

此插件提供以下快捷键：

* B

    * 确认标记区间B的开头。

* Ctrl+Shift+B

    * 标记区间B的开头。
    * 按两次选择时长。

* Ctrl+Shift+D

    * 给出从文件开头到当前位置的时间。
    * 按两次朗读总时长。

* Ctrl + R

    * 确认所选内容已被取消。

* Ctrl+Shift+R

    * 读出当前位置到文件末尾的剩余时间。

* Ctrl+Shift+E

    * 标记区间N的结束位置。
    * 按两次读出区间B和N的位置和时长。

* Ctrl+Shift+P

    * 给出当前文件中实际零件和零件总数的参考。

* Ctrl + Shift + 空格

    * 用于在录制过程中确定流量计的当前级别。
    * 按两次重置。

* 下箭头

    * 让您看到播放头的当前位置。
    * 此命令还将光标定位在选择 N 结束的标记的位置, 同时在进行选择时给出此标记的位置。
    * 在音量对话框中, 说出通常可以用向下箭头到达的下一个值。
    * 这个数值默认不朗读。

* 动作按钮: 结束

    * 将播放光标移动到当前文件的末尾, 并给出总时间。

* 动作按钮: 第一张

    * 将播放光标移动到当前文件的开头。

* 左箭头

    * 让我们在播放过程中短暂返回一秒, 同时给出当前持续时间。
    * 此持续时间可在 mp3directcut 选项中进行配置。

* N

    * 用于确认选择 N 的末尾标记的正确位置。

* 下翻页

    * 让我们在播放过程中进行10秒的飞跃, 同时给出当前持续时间。
    * 此持续时间可在 mp3directcut 选项中进行配置。

* 上翻页

    * 让我们在播放过程中返回 10秒, 同时给出当前持续时间。
    * 此持续时间可在 mp3directcut 选项中进行配置。

* R

    * 允许准备记录以及是否可以按空格键启动。

* 右箭头

    * 让我们在播放过程中做一秒钟的短暂转发, 同时给出当前的持续时间。
    * 此持续时间可在 mp3directcut 选项中进行配置。

* Ctrl + 右箭头

    * 移动到下一个拆分点, 同时给出当前持续时间。

* Ctrl + 左箭头

    * 移动到上一个拆分点, 同时给出当前持续时间。

* Shift+右箭头

    * 让我们在播放过程中做一个四百分之一秒的简短转发, 同时给出当前的持续时间。

* Shift+左箭头

    * 让我们在播放过程中做一个简短的向后四百分之一秒, 同时给出当前的持续时间。

* S

    * 用于停止读取并给出当前持续时间。

* 空格

    * 如果录制已准备就绪, 请启动此录制。
    * 如果录制正在进行中, 请通过将光标定位在开始处来停止录制。
    * 如果加载了文件, 则开始朗读。
    * 如果读取正在进行中, 则允许通过给出当前持续时间来进行暂停。
    * 如果暂停读取, 则允许从当前位置重新启动读取。

* 上箭头

    * 让您看到播放头的当前位置。
    * 此命令还将光标定位在选择 B 开头的标记位置, 同时在进行选择时给出此标记的位置。
    * 在音量对话框中, 将通常可以用 upArrow 到达的上一个值发声。
    * 这个数值默认不朗读。

* NVDA+H

    * 添加快捷键使用'NVDA + H'打开当前插件的帮助;。

## 兼容性 ##

* This add-on is compatible with the versions of NVDA ranging from 2019.3
  and beyond.

## Changes for 20231229.0.0 ##

* Added a backward compatible implementation to support speak on demand
  mode, which will soon be available with nvda-2024.1.

## Changes for 20231007.0.0 ##

* After placing the cutting points and after opening the cutting properties
  window, with "Ctrl+N", adding accessibility to the title of this window by
  indicating the part index.
* In reading mode, after moving the start or end markers of selections with
  keys 1 to 6 of the alphanumeric pad, addition of automatic start of
  reading from the new position;
* Fixed a bug that occurred when consulting the remaining time with
  "control+shift+r" from the beginning of the track.

## Changes for 20230728.0.0 ##

* Applied the flake8 and mypy rules to the code;
* Changed the minimum supported NVDA version to 2019.3 to support
  annotations introduced in Python 3.

## Changes for 20230508.0.0 and beyond ##

* Changed version number, minimum NVDA version and download link according
  to store conventions/requirements.

## 20.12 更新日志 ##

* 在录制和阅读最新版本的 mp3 直接切割时停止语音;
* 修复了使用Python 3读取NVDA新版本的剩余时间的问题。

## 19.02版的更改 ##

* 在 nvda 2018.2新增的设置面板中添加了插件的配置;
* 现在使用YY.MM形式的版本号（年份为2位数，后跟一个点，后跟月份为2位数）;
* 兼容nvda 2019.1的插件新版本格式。

## 版本4.0 ##

* 添加了Python 2.7和3的插件的兼容性;
* 修复了包含非ASCII字符的附加路径的错误。

## 版本3.0 ##

* 使用gui.guiHelper模块确保插件配置对话框的正确外观;
* 格式化字符串使用格式而不是 %s;
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

* 添加一个快捷键, 朗读剩余的时间与 "Ctrl+Shift+R";
* 固定阅读时间，包括小时;
* 增加了区分千分之一秒或百分之一秒的功能。

## 版本1.1 ##

* 可以在输入手势中mp3DirectCut这个分类里修改快捷键;

    * 它们将仅在使用 mp3DirectCut 软件时可见。

* 添加了在NVDA配置选项中启用或禁用朗读选择范围的功能;

## 版本1.0 ##

* 发布初始版本。

[[!tag dev stable]]

[1]:
https://github.com/abdel792/mp3DirectCut/releases/download/v23.12.29/mp3DirectCut-20231229.0.0.nvda-addon

[2]:
https://github.com/abdel792/mp3DirectCut/releases/download/v23.12.29-beta/mp3DirectCut-20231229.0.1.nvda-addon
