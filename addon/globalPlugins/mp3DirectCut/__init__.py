# coding: utf-8

import globalPluginHandler
import addonHandler
from mp3DirectCutDialog import Mp3DirectCutDialog
import gui
import wx
import os
addonHandler.initTranslation()
import config

_addonDir = os.path.join(os.path.dirname(__file__), "..", "..").decode("mbcs")
_curAddon = addonHandler.Addon(_addonDir)
_addonSummary = _curAddon.manifest['summary']

confSpec = {
	'space': 'boolean(default=True)',
	'marker': 'boolean(default=True)',
	'other': 'boolean(default=True)'
	}
config.conf.spec['mp3DCReport'] = confSpec

class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	scriptCategory = _addonSummary

	def __init__(self, *args, **kwargs):
		super(GlobalPlugin, self).__init__(*args, **kwargs)
		self.createSubMenu()

	def createSubMenu(self):
		self.preferencesMenu = gui.mainFrame.sysTrayIcon.preferencesMenu
		self.mp3DirectCut = self.preferencesMenu.Append(wx.ID_ANY,
		# Translators: name of the option in the menu.
		_("{0} addon configuration").format("mp3DirectCut"), "")
		gui.mainFrame.sysTrayIcon.Bind(wx.EVT_MENU, self.onMp3DirectCutDialog, self.mp3DirectCut)

	def terminate(self):
		try:
			self.preferencesMenu.RemoveItem(self.mp3DirectCut)
		except wx.PyDeadObjectError:
			pass

	def onMp3DirectCutDialog(self, evt):
		gui.mainFrame._popupSettingsDialog(Mp3DirectCutDialog)

	def script_activateMP3DirectCutConfigurationDialog(self, gesture):
		wx.CallAfter(self.onMp3DirectCutDialog, None)

	# Translators: message presented in input mode.
	script_activateMP3DirectCutConfigurationDialog.__doc__ = _("Allows you display the configuration dialog of {0} addon.").format("mp3DirectCut")
