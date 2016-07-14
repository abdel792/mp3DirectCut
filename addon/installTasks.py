# -*- coding: UTF-8 -*-

import addonHandler
import gui
import wx

addonHandler.initTranslation()

def onInstall():
	addon = [x for x in addonHandler.getAvailableAddons() if x.manifest["name"] == "mp3directcut"]
	if len(addon) > 0:
		addon = addon[0]
		if gui.messageBox(
		_("You have installed the mp3DirectCut-1.1 add-on which is incompatible with this one. Do you want to uninstall this old version?"),
		_("Uninstall incompatible version"),
		wx.YES|wx.NO|wx.ICON_WARNING)==wx.YES:
			addon.requestRemove()
