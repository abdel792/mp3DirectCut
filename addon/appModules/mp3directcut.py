# -*- coding: utf-8 -*-

#mp3directcut.py

# Copyright 2017-2018 Abdelkrim Bensaïd and other contributors, released under gPL.
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.

import addonHandler
addonHandler.initTranslation()

import appModuleHandler
import windowUtils
from oleacc import STATE_SYSTEM_INDETERMINATE, STATE_SYSTEM_MIXED
from controlTypes import ROLE_PANE, ROLE_EDITABLETEXT
from datetime import datetime
import os
import api
from scriptHandler import getLastScriptRepeatCount
from winUser import CHILDID_SELF, OBJID_CLIENT, setFocus, mouse_event, MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP
from ui import message
import speech
from NVDAObjects.IAccessible import IAccessible, getNVDAObjectFromEvent

oldSpeechMode = speech.speechMode
hr, min, sec, hun, th = _('hours'), _('minutes'), _('seconds'), _('hundredths'), _('thousandths')
programName = 'mp3DirectCut'
_addonDir = os.path.join(os.path.dirname(__file__), '..').decode('mbcs')
_curAddon = addonHandler.Addon(_addonDir)
_addonSummary = _curAddon.manifest['summary']

announce = (
	# Translators: Message to inform that no selection has been realized.
	_('No selection'),
	# Translators: Message to inform the user that the playback cursor is at the top of the file.
	_('Beginning of the file.'),
	# Translators: Message to inform the user that the playback cursor is at the end of the file.
	_('End of the file.'),
	# Translators: Message to inform the user that not file is loaded.
	_('Not file is loaded. Please check that you are in a file, open one with Control O, or R to start recording.'),
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
	_('The recording is ready ! It remains only to press spacebar for begin the recording. This same spacebar  will stop the recording !'),
	# Translators: Message to inform the user that a recording is in progress.
	_('A recording is in progress, please press spacebar for stop it and start a new one.'),
	# Translators: Message to inform the user that the recording is not ready.
	_('The recording is not ready !'),
	# Translators: Message to indicate that the vu-meter is not available.
	_('The vu-meter is not available. Please verify if a recording is in progress, and that the checkbox enable the margin button is checked in the options of %s.') % programName,
	# Translators: Message to confirm that the level of the vu-meter has been reset.
	_('The level of the vu-meter has been reset !'),
	# Translators: Message to confirm the placement of the selection start marker.
	_("Start selection marker set."),
	# Translators: Message to confirm the placement of the selection end marker.
	_("End selection marker set."),
	# Translators: Message to confirm that the selection has been canceled.
	_('Selection canceled.')
)

def timeSplitter(sTime):
	hours = minutes = seconds = hundredths = thousandths = ''
	if ':' in sTime:
		hrs = sTime.split(':')
		if hrs[0] != '00' and hrs[0] != '0':
			hours = '%s %s, ' % (hrs[0], hr)
		if hrs[1].split("'")[0] != '00':
			minutes = hrs[1].split("'")[0]
	else:
		mnts = sTime.split("'")
		if mnts[0] != '00' and mnts[0] != '0':
			minutes = mnts[0]
	if minutes:
		if len(minutes) > 1:
			if minutes[0] == '0':
				minutes = minutes[1]
		minutes = '%s %s, ' % (minutes, min)
	scnds = sTime.split("'")[1].split('.')[0]
	if scnds != '00' and scnds != '0':
		seconds = scnds
	if seconds:
		if len(seconds) > 1:
			if seconds[0] == '0':
				seconds = seconds[1]
		seconds = '%s %s, ' % (seconds, sec)
	hd=sTime.split('.')[1].split()[0]
	if hd != '00' and hd != '000':
		if len(hd) == 3:
			thousandths = '%s %s.' % (hd, th)
		else:
			hundredths = '%s %s.' % (hd, hun)
	timeSplitter = hours + minutes + seconds + hundredths if not thousandths else hours + minutes + seconds + thousandths
	return timeSplitter

def isRecordingReady():
	fg = api.getForegroundObject ()
	hTime = readOrRecord ()
	hRecord = windowUtils.findDescendantWindow(fg.windowHandle, controlID=160)
	text = getNVDAObjectFromEvent(hTime, OBJID_CLIENT, CHILDID_SELF).value
	text1 = getNVDAObjectFromEvent(hRecord, OBJID_CLIENT, CHILDID_SELF).value
	if not text1 and (text and not text.isspace()):
		return True
	return False

def sayMessage(msg, space = None, marker = None):
	import config
	if space:
		if config.conf['mp3DCReport']['space']:
			message (msg)
	elif marker:
		if config.conf['mp3DCReport']['marker']:
			message (msg)
	else:
		if config.conf['mp3DCReport']['other']:
			message(msg)

def isReading():
	fg = api.getForegroundObject ()
	o = fg.firstChild.firstChild.lastChild.firstChild
	hwnd = o.windowHandle
	childID = o.childCount - 1
	readingBtn = getNVDAObjectFromEvent (hwnd, OBJID_CLIENT, childID)
	if all(x in readingBtn.states for x in [STATE_SYSTEM_INDETERMINATE, STATE_SYSTEM_MIXED]):
		return True
	return False

def readOrRecord():
	fg = api.getForegroundObject ()
	hwnd = windowUtils.findDescendantWindow(fg.windowHandle, controlID=161)
	return hwnd

def isStarting():
	focus = api.getFocusObject ()
	if focus.role == ROLE_PANE and focus.name == u'mp3DirectCut':
		hwnd = readOrRecord()
		o = getNVDAObjectFromEvent(hwnd, OBJID_CLIENT, CHILDID_SELF)
		sStarting = o.value
		if not sStarting:
			return True
	return False

def vuMeterHandle():
	fg = api.getForegroundObject ()
	hwnd = windowUtils.findDescendantWindow(fg.windowHandle, controlID=138)
	return hwnd

def isRecording ():
	fg = api.getForegroundObject ()
	hwnd = windowUtils.findDescendantWindow(fg.windowHandle, controlID=160)
	o = getNVDAObjectFromEvent(hwnd, OBJID_CLIENT, CHILDID_SELF)
	text = o.value
	if text and not text.isspace():
		text=text.split()
		if text[1].startswith ("'"):
			return True
	return False

def checkPart():
	fg = api.getForegroundObject ()
	hwnd = windowUtils.findDescendantWindow(fg.windowHandle, controlID=160)
	o = getNVDAObjectFromEvent(hwnd, OBJID_CLIENT, CHILDID_SELF)
	text = o.value
	if text and not text.isspace():
		text=text.split()
		if text[1].startswith ('('):
			return True
	return False

def checkSelection ():
	fg = api.getForegroundObject ()
	hwnd = windowUtils.findDescendantWindow(fg.windowHandle, controlID=160)
	o = getNVDAObjectFromEvent(hwnd, OBJID_CLIENT, CHILDID_SELF)
	text = o.value
	if text and not text.isspace():
		text=text.split()
		if text[0].endswith(':'):
			return True
	return False

def part(flag=None):
	if checkPart ():
		fg = api.getForegroundObject ()
		hwnd = windowUtils.findDescendantWindow(fg.windowHandle, controlID=160)
		o = getNVDAObjectFromEvent(hwnd, OBJID_CLIENT, CHILDID_SELF)
		text = o.value
		text = text.split('(')
		text = text[1]
		text = text.split(')')
		text = text[0]
		text = text.replace('/', ' %s ' % _('of'))
		return '%s %s' % (announce[10], text) if not flag else '%s %s' % (_('Part'), text)

def selectionDuration():
	if checkSelection ():
		fg = api.getForegroundObject ()
		hwnd = windowUtils.findDescendantWindow(fg.windowHandle, controlID=160)
		o = getNVDAObjectFromEvent(hwnd, OBJID_CLIENT, CHILDID_SELF)
		text = o.value
		selectionDuration = text.split('(')
		selectionDuration = selectionDuration[1]
		selectionDuration = selectionDuration[:-1]
		return timeSplitter(selectionDuration)

def beginSelection():
	if checkSelection():
		fg = api.getForegroundObject ()
		hwnd = windowUtils.findDescendantWindow(fg.windowHandle, controlID=160)
		o = getNVDAObjectFromEvent(hwnd, OBJID_CLIENT, CHILDID_SELF)
		text = o.value
		beginSelection = text.split(' - ')
		beginSelection = beginSelection[0]
		beginSelection = beginSelection.split()[1]
		return timeSplitter(beginSelection)

def endSelection():
	if checkSelection ():
		fg = api.getForegroundObject ()
		hwnd = windowUtils.findDescendantWindow(fg.windowHandle, controlID=160)
		o = getNVDAObjectFromEvent(hwnd, OBJID_CLIENT, CHILDID_SELF)
		text = o.value
		endSelection = text.split(' - ')
		endSelection = endSelection[1]
		endSelection = endSelection.split(' ')
		endSelection = endSelection[0]
		return timeSplitter(endSelection)

def actualDuration():
	hwnd = readOrRecord()
	o = getNVDAObjectFromEvent(hwnd, OBJID_CLIENT, CHILDID_SELF)
	sActual = o.value
	if sActual and not sActual.isspace() and '   ' in sActual:
		sActual = sActual.split(': ')
		sActual = sActual[2].split()
		sActual=sActual[0]
		sActual = timeSplitter(sActual)
	return sActual

def actualDurationPercentage():
	hwnd = readOrRecord()
	o = getNVDAObjectFromEvent(hwnd, OBJID_CLIENT, CHILDID_SELF)
	sActual = o.value
	if '(' in sActual:
		sActual = sActual.split('(')
		sActual = sActual[1]
		sActual = sActual[:-1]
	return sActual

def totalTime():
	if checkPart () or checkSelection ():
		hwnd = readOrRecord()
		o = getNVDAObjectFromEvent(hwnd, OBJID_CLIENT, CHILDID_SELF)
		sTime = o.value
		sTime = sTime.split(': ')
		sTime = sTime[1].split('   ')[0]
		sTotal = timeSplitter(sTime)
		return sTotal

def timeRemaining():
	hwnd = readOrRecord()
	o = getNVDAObjectFromEvent(hwnd, OBJID_CLIENT, CHILDID_SELF)
	sActual = o.value
	if sActual != '' and not sActual.isspace() and '   ' in sActual:
		sActual = sActual.split(': ')
		sActual = sActual[2].split()
		sActual=sActual[0]
	sTotal = o.value
	sTotal = sTotal.split(': ')
	sTotal = sTotal[1]
	sTotal = sTotal.split('   ')[0]
	if sTotal == sActual:
		# Translators: Message to inform the user that there is no remaining time.
		return _('No time remaining !')
	hORm = len(sTotal.split('.')[1])
	fmt = "%H:%M'%S.%f"
	if not ':' in sActual:
		sActual = '0:%s' % sActual
	if not ':' in sTotal:
		sTotal = '0:%s' % sTotal
	result = datetime.strptime(sTotal, fmt) - datetime.strptime(sActual, fmt)
	result = str(result).decode('utf-8')
	result = result.replace(':', "'")
	result = result.replace("'", ':', 1)
	result = result[:-4] if hORm == 2 else result[:-3]
	return timeSplitter(result)

class SoundManager (IAccessible):

	scriptCategory = _addonSummary

	def script_checkRecording(self, gesture):
		gesture.send()
		if isRecordingReady ():
			sayMessage (announce[15])
		elif isRecording ():
			sayMessage (announce[16])
		else:
			sayMessage (announce[17])

	def script_cancelSelection(self, gesture):
		selection = checkSelection ()
		gesture.send ()
		if isStarting ():
			sayMessage (announce[3])
			return
		text = announce[22] if selection else announce[0]
		message(text)

	def script_space(self, gesture):
		gesture.send()
		if isReading():
			return
		if isStarting():
			sayMessage (announce[3])
			return
		sActual = actualDuration()
		speech.speechMode = speech.speechMode_off
		api.processPendingEvents()
		speech.speechMode = oldSpeechMode
		if not sActual:
			sayMessage(announce[1], space = True)
			return
		sActual = sActual + ' ' + actualDurationPercentage() if not sActual == totalTime() else announce[2] + ' ' + sActual + ' ' + actualDurationPercentage ()
		sayMessage(sActual, space = True)

	def script_nextSplittingPoint(self, gesture):
		gesture.send()
		if isStarting():
			sayMessage (announce[3])
			return
		if checkPart () or checkSelection ():
			sActual = actualDuration()
			if sActual == totalTime():
				sActual = announce[2] + ' ' + actualDuration () + ' ' + actualDurationPercentage() if checkSelection () else announce[2] + ' ' + actualDuration () + ' ' + part(flag=True)
			else:
				sActual = sActual + ' ' + actualDurationPercentage() if checkSelection () else sActual + ' ' + part(flag=True)
			speech.speechMode = speech.speechMode_off
			api.processPendingEvents()
			speech.speechMode = oldSpeechMode
			if not isReading():
				sayMessage(sActual)

	def script_previousSplittingPoint(self, gesture):
		gesture.send()
		if isStarting():
			sayMessage (announce[3])
			return
		if checkSelection () or checkPart ():
			sActual = actualDuration()
			if not sActual:
				sActual = announce[1] + ' ' + actualDurationPercentage() if checkSelection () else announce[1] + ' ' + part(flag=True)
			else:
				sActual = sActual + ' ' + actualDurationPercentage() if checkSelection () else sActual + ' ' + part(flag=True)
			speech.speechMode = speech.speechMode_off
			api.processPendingEvents()
			speech.speechMode = oldSpeechMode
			if not isReading():
				sayMessage(sActual)

	def script_up(self, gesture):
		gesture.send()
		if isStarting():
			sayMessage (announce[3])
			return
		if isRecording():
			return
		if checkSelection () or checkPart ():
			speech.speechMode = speech.speechMode_off
			api.processPendingEvents()
			speech.speechMode = oldSpeechMode
			if checkSelection ():
				if not isReading():
					sActual = actualDuration()
					if not sActual:
						sActual = announce[1]
					if sActual == totalTime():
						sActual = '%s %s' % (sActual, announce[2])
					sayMessage (announce[5] + ' : ' + sActual + ' ' + actualDurationPercentage())
			else:
				if not isReading():
					sActual = actualDuration()
					if not sActual:
						sayMessage('%s, %s' % (announce[0], announce[1]))
						return
					if sActual == totalTime():
						sActual = '%s %s' % (sActual, announce[2])
					# Translators: Message  to indicate the elapsed time.
					sayMessage ('%s, %s %s %s' % (announce[0], _('Elapsed time: '), sActual, actualDurationPercentage()))

	def script_down(self, gesture):
		gesture.send()
		if isStarting():
			sayMessage (announce[3])
			return
		if isRecording():
			return
		if checkSelection () or checkPart ():
			speech.speechMode = speech.speechMode_off
			api.processPendingEvents()
			speech.speechMode = oldSpeechMode
			if checkSelection ():
				if not isReading():
					sActual = actualDuration()
					if not sActual:
						sActual = announce[1]
					if sActual == totalTime():
						sActual = '%s %s' % (sActual, announce[2])
					sayMessage (announce[6] + ' : ' + sActual + ' ' + actualDurationPercentage())
			else:
				if not isReading():
					sActual = actualDuration()
					if not sActual:
						sayMessage('%s, %s' % (announce[0], announce[1]))
						return
					if sActual == totalTime():
						sActual = '%s %s' % (sActual, announce[2])
					# Translators: Message  to indicate the elapsed time.
					sayMessage ('%s, %s %s %s' % (announce[0], _('Elapsed time: '), sActual, actualDurationPercentage()))

	def script_elapsedTime(self, gesture):
		if isStarting():
			sayMessage (announce[3])
			return
		if isRecording():
			message(announce[4])
			return
		if checkSelection () or checkPart ():
			if not actualDuration():
				text = announce[1]
			elif actualDuration() == totalTime():
				text = '%s %s %s %s' % (_('Elapsed time: '), actualDuration(), announce[2], actualDurationPercentage())
			else:
				# Translators: Message to indicate the elapsed time.
				text = '%s %s %s' % (_('Elapsed time: '), actualDuration(), actualDurationPercentage())
			repeat = getLastScriptRepeatCount()
			if repeat == 0:
				message(text)
			elif repeat == 1:
				message('%s %s' % (announce[8], totalTime()))

	# Translators: message presented in input mode.
	script_elapsedTime.__doc__ = _('Gives the duration from the beginning of the file to the current position of the playback cursor. If pressed twice, gives the total duration.')

	def script_timeRemaining(self, gesture):
		if isStarting():
			sayMessage (announce[3])
			return
		if isRecording():
			message(announce[4])
			return
		if checkSelection () or checkPart ():
			# Translators: Message to indicate the remaining time.
			message('%s %s' % (_('Remaining time: '), timeRemaining()))

	# Translators: message presented in input mode.
	script_timeRemaining.__doc__ = _('Gives the time remaining from the current position of the playback cursor to the end of the file.')

	def script_vuMeter(self, gesture):
		gesture.send()
		if isStarting():
			sayMessage (announce[3])
			return
		h=self.windowHandle
		hwnd = vuMeterHandle()
		repeat = getLastScriptRepeatCount()
		o = getNVDAObjectFromEvent(hwnd, OBJID_CLIENT, CHILDID_SELF)
		sLevel = o.value
		if sLevel:
			if repeat == 0:
				sayMessage(announce[7] + ' : ' + sLevel)
			elif repeat == 1:
				setFocus(hwnd)
				mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, None, None)
				mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, None, None)
				sayMessage (announce[19])
				setFocus(h)
		else:
			sayMessage(announce[18])

	# Translators: message presented in input mode.
	script_vuMeter.__doc__ = _('Used to determine the current level of the vu-meter, during recording, double pressure reset it.')

	def script_bPosition(self, gesture):
		gesture.send()
		if isStarting():
			sayMessage (announce[3])
			return
		if not isReading():
			sayMessage (announce[20], marker = True)

	def script_nPosition(self, gesture):
		gesture.send()
		if isStarting():
			sayMessage (announce[3])
			return
		if not isReading():
			sayMessage (announce[21], marker = True)

	def script_beginningOfSelection(self, gesture):
		if isStarting():
			sayMessage (announce[3])
			return
		repeat = getLastScriptRepeatCount()
		bSelection = beginSelection()
		if not bSelection:
			bSelection = announce[1]
		if checkSelection ():
			if repeat == 0:
				sayMessage(announce[5] + ' : ' + bSelection)
			elif repeat == 1:
				sayMessage(announce[9] + ' : ' + selectionDuration())
		else:
			sayMessage(announce[11])

	# Translators: message presented in input mode.
	script_beginningOfSelection.__doc__ = _('Used to indicate the position of the marker of the beginning of selection B. Double pressure lets give you the duration of the selection.')

	def script_endOfSelection(self, gesture):
		if isStarting():
			sayMessage (announce[3])
			return
		repeat = getLastScriptRepeatCount()
		bSelection = beginSelection()
		eSelection = endSelection()
		if not bSelection:
			bSelection = announce[1]
		if not eSelection:
			eSelection = announce[1]
		if checkSelection ():
			if repeat == 0:
				sayMessage(announce[6] + ' : ' + eSelection)
			elif repeat == 1:
				sayMessage(announce[5] + ' : ' + bSelection)
				sayMessage(announce[6] + ' : ' + eSelection)
				sayMessage(announce[9] + ' : ' + selectionDuration())
		else:
			sayMessage(announce[11])

	# Translators: message presented in input mode.
	script_endOfSelection.__doc__ = _('Used to indicate the position of the marker of the end of selection N. Double pressure gives recapitulatif positions B and N, and the duration of the selection.')

	def script_actualPart(self, gesture):
		if isStarting():
			sayMessage (announce[3])
			return
		elif checkPart ():
			message(part())
		elif isRecording():
			message(announce[12] + ' ' + announce[14])
		elif checkSelection ():
			message(announce[12] + ' ' + announce[13])
		else:
			message(announce[12])

	# Translators: message presented in input mode.
	script_actualPart.__doc__ = _('Give the reference of the actual part and the total number of parts in the current file.')

	__gestures = {
		'kb:r':'checkRecording',
		'kb:control+shift+d': 'elapsedTime',
		'kb:control+shift+r': 'timeRemaining',
		'kb:control+r':'cancelSelection',
		'kb:space': 'space',
		'kb:control+leftArrow':'previousSplittingPoint',
		'kb:control+rightArrow':'nextSplittingPoint',
		'kb:upArrow': 'up',
		'kb:downArrow': 'down',
		'kb:control+shift+space': 'vuMeter',
		'kb:b': 'bPosition',
		'kb:n': 'nPosition',
		'kb:control+shift+b': 'beginningOfSelection',
		'kb:control+shift+e': 'endOfSelection',
		'kb:control+shift+p': 'actualPart'
	}

class AppModule (appModuleHandler.AppModule):

	scriptCategory = _addonSummary

	def event_valueChange (self, obj, nextHandler):
		if obj.role == ROLE_EDITABLETEXT and obj.value and all (x in obj.value for x in ['   ', ':']):
			if checkSelection () or checkPart ():
				sActual = actualDuration()
				if sActual == totalTime():
					sActual = announce[2] + ' ' + sActual
				elif not sActual:
					sActual = announce[1]
				else:
					sActual = sActual + ' ' + actualDurationPercentage()
				if not isReading():
					sayMessage(sActual)
					return
		nextHandler ()

	def chooseNVDAObjectOverlayClasses (self, obj, clsList):
		if obj.role == ROLE_PANE and obj.name and any (x in obj.name for x in [u'mp3DirectCut', '.mp3']):
			clsList.insert(0, SoundManager)

	def script_openHelp(self, gesture):
		os.startfile(addonHandler.getCodeAddon().getDocFilePath())

	# Translators: message presented in input mode.
	script_openHelp.__doc__=_('Lets open the help of the current add-on.')

	__gestures = {
		'kb:nvda+h':'openHelp'
	}