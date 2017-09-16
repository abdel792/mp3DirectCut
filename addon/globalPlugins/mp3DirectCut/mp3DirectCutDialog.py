# -*- coding: UTF-8 -*-

# globalPlugins/mp3DirectCut/mp3DirectCutDialog.py.

# Copyright 2017-2018 Abdelkrim Bensaïd and other contributors, released under gPL.
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import addonHandler
addonHandler.initTranslation ()
import config
from gui.settingsDialogs import SettingsDialog
import wx
import os
import globalVars
from gui import guiHelper

class Mp3DirectCutDialog (SettingsDialog):

	# Translators: The title of the add-on configuration dialog box.
	title = _("Configuration of the addon {0}").format ("mp3DirectCut")

	def makeSettings (self, settingsSizer):
		settingsSizerHelper = guiHelper.BoxSizerHelper (self, sizer = settingsSizer)
		# Translators: The label of the checkbox to enable or disable the spacebar announcements.
		self.reportSpaceCheckBox = wx.CheckBox (parent = self, label = _("Enable announcements of the space key"))
		self.reportSpaceCheckBox.SetValue (config.conf['mp3DCReport']['space'])
		if globalVars.appArgs.secure:
			self.reportSpaceCheckBox.Disable ()
		settingsSizerHelper.addItem (self.reportSpaceCheckBox)

		# Translators: The label of the checkbox to enable or disable the announcements of the selection markers.
		self.reportMarkerCheckBox = wx.CheckBox (parent = self, label = _("Announce the placement of the selection markers"))
		self.reportMarkerCheckBox.SetValue (config.conf['mp3DCReport']['marker'])
		if globalVars.appArgs.secure:
			self.reportMarkerCheckBox.Disable ()
		settingsSizerHelper.addItem (self.reportMarkerCheckBox)

		# Translators: The label of the checkbox to enable or disable the other announcements.
		self.reportOtherCheckBox = wx.CheckBox (parent = self, label = _("Enable the other announces"))
		self.reportOtherCheckBox.SetValue (config.conf['mp3DCReport']['other'])
		if globalVars.appArgs.secure:
			self.reportOtherCheckBox.Disable ()
		settingsSizerHelper.addItem (self.reportOtherCheckBox)

	def postInit (self):
		self.reportSpaceCheckBox.SetFocus ()

	def onOk (self, evt):
		config.conf['mp3DCReport']['space'] = self.reportSpaceCheckBox.GetValue ()
		config.conf['mp3DCReport']['marker'] = self.reportMarkerCheckBox.GetValue ()
		config.conf['mp3DCReport']['other'] = self.reportOtherCheckBox.GetValue ()
		super (Mp3DirectCutDialog, self).onOk (evt)

