# -*- coding: UTF-8 -*-

# globalPlugins/mp3DirectCut/__init__.py.

# Copyright 2017-2018 Abdelkrim Bensaïd and other contributors, released under gPL.
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import globalPluginHandler
import globalVars
import addonHandler
from .mp3DirectCutDialog import Mp3DirectCutPanel, Mp3DirectCutDialog
import gui
import wx
import os
addonHandler.initTranslation ()
import config

### Constants
ADDON_SUMMARY = addonHandler.getCodeAddon ().manifest["summary"]

confSpec = {
	'space': 'boolean(default = True)',
	'marker': 'boolean(default = True)',
	'other': 'boolean(default = True)'
	}
config.conf.spec['mp3DCReport'] = confSpec

class GlobalPlugin (globalPluginHandler.GlobalPlugin):

	scriptCategory = ADDON_SUMMARY

	def __init__(self, *args, **kwargs):
		super (GlobalPlugin, self).__init__(*args, **kwargs)
		if globalVars.appArgs.secure or (hasattr (config, "isAppX") and config.isAppX): return
		# This block ensures compatibility with NVDA versions prior to 2018.2 which includes the settings panel.
		if hasattr (gui, "NVDASettingsDialog"):
			from gui import NVDASettingsDialog
			NVDASettingsDialog.categoryClasses.append(Mp3DirectCutPanel)
		else:
			self.createSubMenu ()

	def createSubMenu (self):
		self.preferencesMenu = gui.mainFrame.sysTrayIcon.preferencesMenu
		self.mp3DirectCut = self.preferencesMenu.Append (wx.ID_ANY,
		# Translators: name of the option in the menu.
		_("{0} addon configuration").format ("mp3DirectCut"), "")
		gui.mainFrame.sysTrayIcon.Bind (wx.EVT_MENU, self.onMp3DirectCutDialog, self.mp3DirectCut)

	def terminate (self):
		super(GlobalPlugin, self).terminate()
		if hasattr (gui, "NVDASettingsDialog"):
			gui.NVDASettingsDialog.categoryClasses.remove(Mp3DirectCutPanel)
		try:
			if wx.version().startswith("4"):
				self.preferencesMenu.Remove (self.mp3DirectCut)
			else:
				self.preferencesMenu.RemoveItem (self.mp3DirectCut)
		except:
			pass

	def onMp3DirectCutDialog (self, evt):
		gui.mainFrame._popupSettingsDialog (Mp3DirectCutDialog)

	def script_activateMP3DirectCutConfigurationDialog (self, gesture):
		wx.CallAfter (self.onMp3DirectCutDialog, None)

	# Translators: message presented in input mode.
	script_activateMP3DirectCutConfigurationDialog.__doc__ = _("Allows you display the configuration dialog of {0} addon.").format ("mp3DirectCut")
