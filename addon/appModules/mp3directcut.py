# -*- coding: UTF-8 -*-

# appModules/mp3directcut.py.

# Copyright 2017-2018 Abdelkrim Bensaïd and other contributors, released under gPL.
# This file is covered by the GNU General Public License.
# See the file COPYING for more details.

from __future__ import unicode_literals  # To ensure unicode compatibility with both python 2 and 3.
import appModuleHandler
import windowUtils
from typing import Callable
import controlTypes
if hasattr(controlTypes, "ROLE_PANE"):
	from controlTypes import ROLE_PANE, ROLE_EDITABLETEXT
else:
	ROLE_PANE = controlTypes.Role.PANE
	ROLE_EDITABLETEXT = controlTypes.Role.EDITABLETEXT
from datetime import datetime
import os
import api
from scriptHandler import getLastScriptRepeatCount
from winUser import (
	CHILDID_SELF,
	OBJID_CLIENT,
	setFocus,
	mouse_event,
	MOUSEEVENTF_LEFTDOWN,
	MOUSEEVENTF_LEFTUP
)
from ui import message
import sys
from NVDAObjects.IAccessible import IAccessible, getNVDAObjectFromEvent

import addonHandler
addonHandler.initTranslation()
_: Callable[[str], str]
# Constants
PROGRAM_NAME = 'mp3DirectCut'
ADDON_SUMMARY = addonHandler.getCodeAddon().manifest["summary"]
hr, min, sec, hun, th = _('hours'), _('minutes'), _('seconds'), _('hundredths'), _('thousandths')

announce = (
	# Translators: Message to inform that no selection has been realized.
	_('No selection'),
	# Translators: Message to inform the user that the playback cursor is at the top of the file.
	_('Beginning of the file.'),
	# Translators: Message to inform the user that the playback cursor is at the end of the file.
	_('End of the file.'),
	# Translators: Message to inform the user that not file is loaded.
	_('Not file is loaded. Please check that you are in a file, open one with Control O,\
	or R to start recording.'),
	# Translators: Message to inform the user that the current command is not available in a recording mode.
	_('This command is not available in a recording mode, it is available only in a reading mode !'),
	# Translators: Message to indicate the position of the selection start marker.
	_('The marker of the beginning of selection B is at'),
	# Translators: Message to indicate the position of the selection end marker.
	_('The marker of the End of selection N is at'),
	# Translators: Message to indicate the level of the vu-meter.
	_('The level of the vu-meter is at'),
	# Translators: Message to indicate the total duration of the current file.
	_('Total time: '),
	# Translators: Message to indicate the duration of the selection.
	_('Duration of selection'),
	# Translators: Message to indicate the actual part.
	_('Actual part'),
	# Translators: Message to inform that no selection was found.
	_('Selection not found.'),
	# Translators: Message to indicate that the information of the current part is not available.
	_('Information specific to the actual part is not available.'),
	# Translators: Message to prompt the user to verify that no selection has been made.
	_('Please check that no selection has been made.'),
	# Translators: Message to prompt the user to verify that it is not in recording mode.
	_('Please chek that you are not in a recording mode.'),
	# Translators: Message to inform the user that the recording is ready.
	_('The recording is ready ! It remains only to press spacebar for begin the recording.\
	This same spacebar  will stop the recording !'),
	# Translators: Message to inform the user that a recording is in progress.
	_('A recording is in progress, please press spacebar for stop it and start a new one.'),
	# Translators: Message to inform the user that the recording is not ready.
	_('The recording is not ready !'),
	# Translators: Message to indicate that the vu-meter is not available.
	_('The vu-meter is not available. Please verify if a recording is in progress,\
	and that the checkbox enable the margin button is checked in the options of {0}.').format(PROGRAM_NAME),
	# Translators: Message to confirm that the level of the vu-meter has been reset.
	_('The level of the vu-meter has been reset !'),
	# Translators: Message to confirm the placement of the selection start marker.
	_("Start selection marker set."),
	# Translators: Message to confirm the placement of the selection end marker.
	_("End selection marker set."),
	# Translators: Message to confirm that the selection has been canceled.
	_('Selection canceled.')
)


def timeSplitter(time):  # noqa: C901
	hours = minutes = seconds = hundredths = thousandths = ''
	if ':' in time:
		hrs = time.split(':')
		if hrs[0] != '00' and hrs[0] != '0':
			hours = '{0} {1}, '.format(hrs[0], hr)
		if hrs[1].split("'")[0] != '00':
			minutes = hrs[1].split("'")[0]
	else:
		mnts = time.split("'")
		if mnts[0] != '00' and mnts[0] != '0':
			minutes = mnts[0]
	if minutes:
		if len(minutes) > 1:
			if minutes[0] == '0':
				minutes = minutes[1]
		minutes = '{0} {1}, '.format(minutes, min)
	scnds = time.split("'")[1].split('.')[0]
	if scnds != '00' and scnds != '0':
		seconds = scnds
	if seconds:
		if len(seconds) > 1:
			if seconds[0] == '0':
				seconds = seconds[1]
		seconds = '{0} {1}, '.format(seconds, sec)
	hd = time.split('.')[1].split()[0]
	if hd != '00' and hd != '000':
		if len(hd) == 3:
			thousandths = '{0} {1}.'.format(hd, th)
		else:
			hundredths = '{0} {1}.'.format(hd, hun)
	timeSplitter = hours + minutes + seconds + hundredths if not thousandths\
		else hours + minutes + seconds + thousandths
	return timeSplitter


def isRecordingReady():
	time = readingWindow()
	record = recAndSelWindow()
	text = getTextFromWindow(time)
	text1 = getTextFromWindow(record)
	if not text1 and (text and not text.isspace()):
		return True
	return False


def sayMessage(msg, space=None, marker=None):
	import config
	if space:
		if config.conf['mp3DCReport']['space']:
			message(msg)
	elif marker:
		if config.conf['mp3DCReport']['marker']:
			message(msg)
	else:
		if config.conf['mp3DCReport']['other']:
			message(msg)


def isReading():
	import time
	firstValue = actualDuration()
	time.sleep(0.2)
	secondValue = actualDuration()
	return firstValue != secondValue


def readingWindow():
	fg = api.getForegroundObject()
	hwnd = windowUtils.findDescendantWindow(fg.windowHandle, controlID=161)
	return hwnd


def recAndSelWindow():
	fg = api.getForegroundObject()
	hwnd = windowUtils.findDescendantWindow(fg.windowHandle, controlID=160)
	return hwnd


def getTextFromWindow(hwnd):
	obj = getNVDAObjectFromEvent(hwnd, OBJID_CLIENT, CHILDID_SELF)
	return obj.value


def isStarting():
	focus = api.getFocusObject()
	if focus.role == ROLE_PANE and focus.name == 'mp3DirectCut':
		hwnd = readingWindow()
		starting = getTextFromWindow(hwnd)
		if not starting:
			return True
	return False


def vuMeterHandle():
	fg = api.getForegroundObject()
	hwnd = windowUtils.findDescendantWindow(fg.windowHandle, controlID=138)
	return hwnd


def isRecording():
	hwnd = recAndSelWindow()
	text = getTextFromWindow(hwnd)
	if text and not text.isspace():
		text = text.split()
		if text[1].startswith("'"):
			return True
	return False


def checkPart():
	hwnd = recAndSelWindow()
	text = getTextFromWindow(hwnd)
	if text and not text.isspace():
		text = text.split()
		if text[1].startswith('('):
			return True
	return False


def checkSelection():
	hwnd = recAndSelWindow()
	text = getTextFromWindow(hwnd)
	if text and not text.isspace():
		text = text.split()
		if text[0].endswith(':'):
			return True
	return False


def part(flag=None):
	hwnd = recAndSelWindow()
	text = getTextFromWindow(hwnd)
	text = text.split('(')
	text = text[1]
	text = text.split(')')
	text = text[0]
	text = text.replace('/', ' {0} '.format(_('of')))
	return '{0} {1}'.format(announce[10], text) if not flag else '{0} {1}'.format(_('Part'), text)


def selectionDuration():
	hwnd = recAndSelWindow()
	text = getTextFromWindow(hwnd)
	selectionDuration = text.split('(')
	selectionDuration = selectionDuration[1]
	selectionDuration = selectionDuration[:-1]
	selectionDuration = timeSplitter(selectionDuration) if timeSplitter(selectionDuration) else announce[0]
	return selectionDuration


def beginSelection():
	hwnd = recAndSelWindow()
	text = getTextFromWindow(hwnd)
	beginSelection = text.split(' - ')
	beginSelection = beginSelection[0]
	beginSelection = beginSelection.split()[1]
	beginSelection = timeSplitter(beginSelection) if timeSplitter(beginSelection) else announce[1]
	return beginSelection


def endSelection():
	hwnd = recAndSelWindow()
	text = getTextFromWindow(hwnd)
	endSelection = text.split(' - ')
	endSelection = endSelection[1]
	endSelection = endSelection.split(' ')
	endSelection = endSelection[0]
	endSelection = timeSplitter(endSelection) if timeSplitter(endSelection) else announce[1]
	return endSelection


def actualDuration():
	hwnd = readingWindow()
	actual = getTextFromWindow(hwnd)
	if actual and not actual.isspace() and '   ' in actual:
		actual = actual.split(': ')
		actual = actual[2].split()
		actual = actual[0]
		actual = timeSplitter(actual)
	return actual


def actualDurationPercentage():
	hwnd = readingWindow()
	actual = getTextFromWindow(hwnd)
	if '(' in actual:
		actual = actual.split('(')
		actual = actual[1]
		actual = actual[:-1]
	return actual


def totalTime():
	if checkPart() or checkSelection():
		hwnd = readingWindow()
		time = getTextFromWindow(hwnd)
		time = time.split(': ')
		time = time[1].split('   ')[0]
		total = timeSplitter(time)
		return total


def timeRemaining():
	hwnd = readingWindow()
	actual = getTextFromWindow(hwnd)
	if actual != '' and not actual.isspace() and '   ' in actual:
		actual = actual.split(': ')
		actual = actual[2].split()
		actual = actual[0]
	total = getTextFromWindow(hwnd)
	total = total.split(': ')
	total = total[1]
	total = total.split('   ')[0]
	if total == actual:
		# Translators: Message to inform the user that there is no remaining time.
		return _('No time remaining !')
	hORm = len(total.split('.')[1])
	fmt = "%H:%M'%S.%f"
	if ':' not in actual:
		actual = '0:{0}'.format(actual)
	if ':' not in total:
		total = '0:{0}'.format(total)
	result = datetime.strptime(total, fmt) - datetime.strptime(actual, fmt)
	result = str(result).decode('utf-8') if sys.version_info.major == 2 else str(result)
	result = result.replace(':', "'")
	result = result.replace("'", ':', 1)
	result = result[:-4] if hORm == 2 else result[:-3]
	return timeSplitter(result)


class SoundManager   (IAccessible):

	scriptCategory = ADDON_SUMMARY

	def script_checkRecording(self, gesture):
		gesture.send()
		if isRecordingReady():
			sayMessage(announce[15])
		elif isRecording():
			sayMessage(announce[16])
		else:
			sayMessage(announce[17])

	def script_cancelSelection(self, gesture):
		selection = checkSelection()
		gesture.send()
		if isStarting():
			sayMessage(announce[3])
			return
		text = announce[22] if selection else announce[0]
		message(text)

	def script_space(self, gesture):
		if isRecordingReady():
			self.appModule.runValueChange = False
			gesture.send()
			api.processPendingEvents()
			self.appModule.runValueChange = True
			return
		gesture.send()
		if isReading():
			return
		if isStarting():
			sayMessage(announce[3])
			return
		actual = actualDuration()
		self.appModule.runValueChange = False
		api.processPendingEvents()
		if not actual:
			sayMessage(announce[1], space=True)
			return
		actual = actual + ' ' + actualDurationPercentage() if not actual == totalTime()\
			else announce[2] + ' ' + actual + ' ' + actualDurationPercentage()
		sayMessage(actual, space=True)
		self.appModule.runValueChange = True

	def script_nextSplittingPoint(self, gesture):
		gesture.send()
		if isStarting():
			sayMessage(announce[3])
			return
		if checkPart() or checkSelection():
			actual = actualDuration()
			if actual == totalTime():
				actual = announce[2] + ' ' + actualDuration() + ' ' + actualDurationPercentage() if checkSelection()\
					else announce[2] + ' ' + actualDuration() + ' ' + part(flag=True)
			else:
				actual = actual + ' ' + actualDurationPercentage() if checkSelection()\
					else actual + ' ' + part(flag=True)
			if not isReading():
				self.appModule.runValueChange = False
				api.processPendingEvents()
				sayMessage(actual)
				self.appModule.runValueChange = True

	def script_previousSplittingPoint(self, gesture):
		gesture.send()
		if isStarting():
			sayMessage(announce[3])
			return
		if checkSelection() or checkPart():
			actual = actualDuration()
			if not actual:
				actual = announce[1] + ' ' + actualDurationPercentage() if checkSelection()\
					else announce[1] + ' ' + part(flag=True)
			else:
				actual = actual + ' ' + actualDurationPercentage() if checkSelection()\
					else actual + ' ' + part(flag=True)
			if not isReading():
				self.appModule.runValueChange = False
				api.processPendingEvents()
				sayMessage(actual)
				self.appModule.runValueChange = True

	def script_up(self, gesture):
		gesture.send()
		if isStarting():
			sayMessage(announce[3])
			return
		if isRecording():
			return
		if checkSelection() or checkPart():
			self.appModule.runValueChange = False
			api.processPendingEvents()
			if not isReading():
				if checkSelection():
					actual = actualDuration()
					if not actual:
						actual = announce[1]
					if actual == totalTime():
						actual = '{0} {1}'.format(actual, announce[2])
					sayMessage(announce[5] + ' : ' + actual + ' ' + actualDurationPercentage())
				else:
					actual = actualDuration()
					if not actual:
						sayMessage('{0}, {1}'.format(announce[0], announce[1]))
						return
					if actual == totalTime():
						actual = '{0} {1}'.format(actual, announce[2])
					# Translators: Message  to indicate the elapsed time.
					sayMessage('{0}, {1} {2} {3}'.format(
						announce[0], _('Elapsed time: '), actual, actualDurationPercentage()))
		self.appModule.runValueChange = True

	def script_down(self, gesture):
		gesture.send()
		if isStarting():
			sayMessage(announce[3])
			return
		if isRecording():
			return
		if checkSelection() or checkPart():
			self.appModule.runValueChange = False
			api.processPendingEvents()
			if not isReading():
				if checkSelection():
					actual = actualDuration()
					if not actual:
						actual = announce[1]
					if actual == totalTime():
						actual = '{0} {1}'.format(actual, announce[2])
					sayMessage(announce[6] + ' : ' + actual + ' ' + actualDurationPercentage())
				else:
					actual = actualDuration()
					if not actual:
						sayMessage('{0}, {1}'.format(announce[0], announce[1]))
						return
					if actual == totalTime():
						actual = '{0} {1}'.format(actual, announce[2])
					# Translators: Message  to indicate the elapsed time.
					sayMessage('{0}, {1} {2} {3}'.format(
						announce[0], _('Elapsed time: '), actual, actualDurationPercentage()))
		self.appModule.runValueChange = True

	def script_elapsedTime(self, gesture):
		if isStarting():
			sayMessage(announce[3])
			return
		if isRecording():
			message(announce[4])
			return
		if checkSelection() or checkPart():
			if not actualDuration():
				text = announce[1]
			elif actualDuration() == totalTime():
				text = '{0} {1} {2} {3}'.format(
					_('Elapsed time: '), actualDuration(), announce[2], actualDurationPercentage())
			else:
				# Translators: Message to indicate the elapsed time.
				text = '{0} {1} {2}'.format(_('Elapsed time: '), actualDuration(), actualDurationPercentage())
			repeat = getLastScriptRepeatCount()
			if repeat == 0:
				message(text)
			elif repeat == 1:
				message('{0} {1}'.format(announce[8], totalTime()))

	# Translators: message presented in input mode.
	script_elapsedTime.__doc__ = _(
		'Gives the duration from the beginning of the file to the current position of the playback cursor.\
			If pressed twice, gives the total duration.'
	)

	def script_timeRemaining(self, gesture):
		if isStarting():
			sayMessage(announce[3])
			return
		if isRecording():
			message(announce[4])
			return
		if checkSelection() or checkPart():
			# Translators: Message to indicate the remaining time.
			message('{0} {1}'.format(_('Remaining time: '), timeRemaining()))

	# Translators: message presented in input mode.
	script_timeRemaining.__doc__ = _(
		'Gives the time remaining from the current position of the playback cursor to the end of the file.'
	)

	def script_vuMeter(self, gesture):
		gesture.send()
		if isStarting():
			sayMessage(announce[3])
			return
		hwnd = vuMeterHandle()
		repeat = getLastScriptRepeatCount()
		level = getTextFromWindow(hwnd)
		if level:
			if repeat == 0:
				sayMessage(announce[7] + ' : ' + level)
			elif repeat == 1:
				setFocus(hwnd)
				mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, None, None)
				mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, None, None)
				sayMessage(announce[19])
		else:
			sayMessage(announce[18])

	# Translators: message presented in input mode.
	script_vuMeter.__doc__ = _(
		'Used to determine the current level of the vu-meter, during recording, double pressure reset it.'
	)

	def script_bPosition(self, gesture):
		gesture.send()
		if isStarting():
			sayMessage(announce[3])
			return
		if not isReading():
			sayMessage(announce[20], marker=True)

	def script_nPosition(self, gesture):
		gesture.send()
		if isStarting():
			sayMessage(announce[3])
			return
		if not isReading():
			sayMessage(announce[21], marker=True)

	def script_beginningOfSelection(self, gesture):
		if isStarting():
			sayMessage(announce[3])
			return
		repeat = getLastScriptRepeatCount()
		if checkSelection():
			bSelection = beginSelection()
			if repeat == 0:
				sayMessage(announce[5] + ' : ' + bSelection)
			elif repeat == 1:
				sayMessage(announce[9] + ' : ' + selectionDuration())
		else:
			sayMessage(announce[11])

	# Translators: message presented in input mode.
	script_beginningOfSelection.__doc__ = _(
		'Used to indicate the position of the marker of the beginning of selection B.\
			Double pressure lets give you the duration of the selection.'
	)

	def script_endOfSelection(self, gesture):
		if isStarting():
			sayMessage(announce[3])
			return
		repeat = getLastScriptRepeatCount()
		if checkSelection():
			bSelection = beginSelection()
			eSelection = endSelection()
			if repeat == 0:
				sayMessage(announce[6] + ' : ' + eSelection)
			elif repeat == 1:
				sayMessage(announce[5] + ' : ' + bSelection)
				sayMessage(announce[6] + ' : ' + eSelection)
				sayMessage(announce[9] + ' : ' + selectionDuration())
		else:
			sayMessage(announce[11])

	# Translators: message presented in input mode.
	script_endOfSelection.__doc__ = _(
		'Used to indicate the position of the marker of the end of selection N.\
			Double pressure gives recapitulatif positions B and N, and the duration of the selection.'
	)

	def script_actualPart(self, gesture):
		if isStarting():
			sayMessage(announce[3])
			return
		if checkPart():
			message(part())
		elif isRecording():
			message(announce[12] + ' ' + announce[14])
		elif checkSelection():
			message(announce[12] + ' ' + announce[13])
		else:
			message(announce[12])

	# Translators: message presented in input mode.
	script_actualPart.__doc__ = _(
		'Give the reference of the actual part and the total number of parts in the current file.'
	)

	__gestures = {
		'kb:r': 'checkRecording',
		'kb:control+shift+d': 'elapsedTime',
		'kb:control+shift+r': 'timeRemaining',
		'kb:control+r': 'cancelSelection',
		'kb:space': 'space',
		'kb:control+leftArrow': 'previousSplittingPoint',
		'kb:control+rightArrow': 'nextSplittingPoint',
		'kb:upArrow': 'up',
		'kb:downArrow': 'down',
		'kb:control+shift+space': 'vuMeter',
		'kb:b': 'bPosition',
		'kb:n': 'nPosition',
		'kb:control+shift+b': 'beginningOfSelection',
		'kb:control+shift+e': 'endOfSelection',
		'kb:control+shift+p': 'actualPart'
	}


class AppModule   (appModuleHandler.AppModule):

	scriptCategory = ADDON_SUMMARY
	runValueChange = True

	def event_valueChange(self, obj, nextHandler):
		if not self.runValueChange:
			return
		if obj.role == ROLE_EDITABLETEXT and obj.value and all(x in obj.value for x in ['   ', ':']):
			if checkSelection() or checkPart():
				actual = actualDuration()
				if actual == totalTime():
					actual = announce[2] + ' ' + actual
				elif not actual:
					actual = announce[1]
				else:
					actual = actual + ' ' + actualDurationPercentage()
				if not isReading():
					sayMessage(actual)
					return
		nextHandler()

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.role == ROLE_PANE and obj.name and any(x in obj.name for x in ['mp3DirectCut', '.mp3']):
			clsList.insert(0, SoundManager)

	def script_openHelp(self, gesture):
		os.startfile(addonHandler.getCodeAddon().getDocFilePath())

	# Translators: message presented in input mode.
	script_openHelp.__doc__ = _('Lets open the help of the current add-on.')

	__gestures = {
		'kb:nvda+h': 'openHelp',
	}
