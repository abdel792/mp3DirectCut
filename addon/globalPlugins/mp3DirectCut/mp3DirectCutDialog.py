# -*- coding: utf-8 -*-

# mp3DirectCutDialog.py

import addonHandler
addonHandler.initTranslation()
import config
from gui.settingsDialogs import SettingsDialog
import wx
import os

class Mp3DirectCutDialog(SettingsDialog):

	# Translators: The title of the add-on configuration dialog box.
	title = _("Configuration of the addon {0}").format("mp3DirectCut")

	def makeSettings(self, settingsSizer):
		dialogSizer=wx.BoxSizer(wx.VERTICAL)
		reportSpaceID = wx.NewId()
		# Translators: The label of the checkbox to enable or disable the spacebar announcements.
		self.reportSpace=wx.CheckBox(parent = self, id = reportSpaceID, label=_("Enable announcements of the space key"))
		self.reportSpace.SetValue(config.conf['mp3DCReport']['space'])
		dialogSizer.Add(item=self.reportSpace)
		reportMarkerID = wx.NewId()
		# Translators: The label of the checkbox to enable or disable the announcements of the selection markers.
		self.reportMarker=wx.CheckBox(parent = self, id = reportMarkerID, label=_("Announce the placement of the selection markers"))
		self.reportMarker.SetValue(config.conf['mp3DCReport']['marker'])
		dialogSizer.Add(item=self.reportMarker)
		reportOtherID = wx.NewId()
		# Translators: The label of the checkbox to enable or disable the other announcements.
		self.reportOther=wx.CheckBox(parent = self, id = reportOtherID, label=_("Enable the other announces"))
		self.reportOther.SetValue(config.conf['mp3DCReport']['other'])
		dialogSizer.Add(item=self.reportOther)
		settingsSizer.Add(dialogSizer, border=10, flag=wx.BOTTOM)

	def postInit(self):
		self.reportSpace.SetFocus()

	def onOk(self, evt):
		config.conf['mp3DCReport']['space'] = self.reportSpace.GetValue()
		config.conf['mp3DCReport']['marker'] = self.reportMarker.GetValue()
		config.conf['mp3DCReport']['other'] = self.reportOther.GetValue()
		super(Mp3DirectCutDialog, self).onOk(evt)

