#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Mon Feb 14 14:44:15 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'letternumber'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/Teddy/OneDrive - Indiana State University/Documents/Research/PsychopyTask/letter-number/letternumber_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
subNum = expInfo['participant']
sessionNum = expInfo['session']

outfile= open("./data/letternumber.txt","a+")
outfile.write("subject")
outfile.write("\t")
outfile.write("stimuli")
outfile.write("\t")
outfile.write("trial type")
outfile.write("\t")
outfile.write("position")
outfile.write("\t")
outfile.write("response")
outfile.write("\t")
outfile.write("acc")
outfile.write("\t")
outfile.write("rt")
outfile.write("\n")
outfile.write("\n")

outfile2= open("./data/" + subNum + "_" + sessionNum + "_ln.txt", "w+")
outfile2.write("timestamp: ")
outfile2.write(expInfo['date'])
outfile2.write("\n")
outfile2.write("subject")
outfile2.write("\t")
outfile2.write("stimuli")
outfile2.write("\t")
outfile2.write("trial type")
outfile2.write("\t")
outfile2.write("position")
outfile2.write("\t")
outfile2.write("response")
outfile2.write("\t")
outfile2.write("acc")
outfile2.write("\t")
outfile2.write("rt")
outfile2.write("\n")
text_3 = visual.TextStim(win=win, name='text_3',
    text='You will see letter-number pairs (e.g. G9) in one of four quadrants displayed on the computer monitor. \n\nWhen the letter-number pair is in the top half of the screen, indicate whether the number is odd ("M") or even ("Z") using the keyboard. \n\nWhen the letter-number pair is in the bottom half of the screen, indicate whether the letter is a vowel ("M") or consonant ("Z") using the keyboard.\n\nRespond as quickly and accurately as possible.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.25, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "practice_instructions_numbers"
practice_instructions_numbersClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='You will now complete practice trials of this task.\n\nWhen the letter pair is presented in the top half of the screen:\n\nM=Odd\nZ=Even\n\nPress the Spacebar to begin the practice trials.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.25, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "fixation_cross"
fixation_crossClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "grid"
gridClock = core.Clock()
polygon_5 = visual.Line(
    win=win, name='polygon_5',
    start=(-(1.5, 1)[0]/2.0, 0), end=(+(1.5, 1)[0]/2.0, 0),
    ori=0, pos=(0, 0),
    lineWidth=10,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=0.0, interpolate=True)
polygon_6 = visual.Line(
    win=win, name='polygon_6',
    start=(-(.85, 1)[0]/2.0, 0), end=(+(.85, 1)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=10,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "pract_num"
pract_numClock = core.Clock()
polygon = visual.Line(
    win=win, name='polygon',
    start=(-(1.5, 1)[0]/2.0, 0), end=(+(1.5, 1)[0]/2.0, 0),
    ori=0, pos=(0, 0),
    lineWidth=10,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=0.0, interpolate=True)
polygon_2 = visual.Line(
    win=win, name='polygon_2',
    start=(-(.85, 1)[0]/2.0, 0), end=(+(.85, 1)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=10,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-1.0, interpolate=True)
import numpy

letter = numpy.array([["G", 0], ["K", 0], ["M", 0], ["R", 0], ["A", 1], ["E", 1], ["I", 1], ["U", 1]])
number = numpy.array([[2, 0], [4, 0], [6, 0], [8, 0], [3, 1], [5, 1], [7, 1], [9, 1]])


y =0
z = 0

sn = numpy.array([[-.4,.3],[.4,.3]])
sl = numpy.array([[.4,-.3],[-.4,-.3]])
s = numpy.array([[-.4,.3],[.4,.3],[.4,-.3],[-.4,-.3]])
k = 0

display = 'zzz'
text_5 = visual.TextStim(win=win, name='text_5',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "practice_instructions_letters"
practice_instructions_lettersClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='You will now complete practice trials of this task.\n\nWhen the letter pair is presented in the bottom half of the screen:\n\nM=Vowel\nZ=Consonant\n\nPress the Spacebar to begin the practice trials.',
    font='Arial',
    pos=(0, 0), height=.05, wrapWidth=1.25, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "grid"
gridClock = core.Clock()
polygon_5 = visual.Line(
    win=win, name='polygon_5',
    start=(-(1.5, 1)[0]/2.0, 0), end=(+(1.5, 1)[0]/2.0, 0),
    ori=0, pos=(0, 0),
    lineWidth=10,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=0.0, interpolate=True)
polygon_6 = visual.Line(
    win=win, name='polygon_6',
    start=(-(.85, 1)[0]/2.0, 0), end=(+(.85, 1)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=10,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "pract_let"
pract_letClock = core.Clock()
polygon_3 = visual.Line(
    win=win, name='polygon_3',
    start=(-(1.5, 1)[0]/2.0, 0), end=(+(1.5, 1)[0]/2.0, 0),
    ori=0, pos=(0, 0),
    lineWidth=10,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=0.0, interpolate=True)
polygon_4 = visual.Line(
    win=win, name='polygon_4',
    start=(-(.85, 1)[0]/2.0, 0), end=(+(.85, 1)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=10,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-1.0, interpolate=True)
import numpy

letter = numpy.array([["G", 0], ["K", 0], ["M", 0], ["R", 0], ["A", 1], ["E", 1], ["I", 1], ["U", 1]])
number = numpy.array([[2, 0], [4, 0], [6, 0], [8, 0], [3, 1], [5, 1], [7, 1], [9, 1]])


y = 0
z = 0

sn = numpy.array([[-.4,.3],[.4,.3]])
sl = numpy.array([[.4,-.3],[-.4,-.3]])
s = numpy.array([[-.4,.3],[.4,.3],[.4,-.3],[-.4,-.3]])
k = 0

display = 'zzz'
text_6 = visual.TextStim(win=win, name='text_6',
    text='',
    font='Arial',
    pos=[0,0], height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "prac_complete"
prac_completeClock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='You have complete the practice section of this task. \n\nYou will now move on to the experiment.\n\nPress the spacebar when you are ready to continue.',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=1.25, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "reminder"
reminderClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='As a reminder:\n\nWhen the letter pair is presented in the top half of the screen:\nM=Odd\nZ=Even\n\nWhen the letter pair is presented in the bottom half of the screen:\nM=Vowel\nZ=Consonant\n\nPress the Spacebar to begin the experiment.',
    font='Arial',
    pos=(0, 0), height=.05, wrapWidth=1.25, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()
import numpy

letter = numpy.array([["G", 0], ["K", 0], ["M", 0], ["R", 0], ["A", 1], ["E", 1], ["I", 1], ["U", 1]])
number = numpy.array([[2, 0], [4, 0], [6, 0], [8, 0], [3, 1], [5, 1], [7, 1], [9, 1]])


y =0
z = 0

sn = numpy.array([[-.4,.3],[.4,.3]])
sl = numpy.array([[.4,-.3],[-.4,-.3]])
s = numpy.array([[-.4,.3],[.4,.3],[.4,-.3],[-.4,-.3]])
k = 0

pos = 0
display = 'zzz'

# Initialize components for Routine "fixation_cross"
fixation_crossClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "grid"
gridClock = core.Clock()
polygon_5 = visual.Line(
    win=win, name='polygon_5',
    start=(-(1.5, 1)[0]/2.0, 0), end=(+(1.5, 1)[0]/2.0, 0),
    ori=0, pos=(0, 0),
    lineWidth=10,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=0.0, interpolate=True)
polygon_6 = visual.Line(
    win=win, name='polygon_6',
    start=(-(.85, 1)[0]/2.0, 0), end=(+(.85, 1)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=10,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "qtr"
qtrClock = core.Clock()
quadhor = visual.Line(
    win=win, name='quadhor',
    start=(-(1.5, 1)[0]/2.0, 0), end=(+(1.5, 1)[0]/2.0, 0),
    ori=0, pos=(0, 0),
    lineWidth=10,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=0.0, interpolate=True)
quadvert = visual.Line(
    win=win, name='quadvert',
    start=(-(.85, 1)[0]/2.0, 0), end=(+(.85, 1)[0]/2.0, 0),
    ori=90, pos=(0, 0),
    lineWidth=10,     colorSpace='rgb',  lineColor=[-1,-1,-1], fillColor=[-1,-1,-1],
    opacity=1, depth=-1.0, interpolate=True)
text = visual.TextStim(win=win, name='text',
    text='',
    font='Arial',
    pos=[0,0], height=.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "end_instructions"
end_instructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='You have completed the experiment!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
instructionsComponents = [text_3, key_resp_3]
for thisComponent in instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions"-------
while continueRoutine:
    # get current time
    t = instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions"-------
for thisComponent in instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "practice_instructions_numbers"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
practice_instructions_numbersComponents = [text_9, key_resp_8]
for thisComponent in practice_instructions_numbersComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_instructions_numbersClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_instructions_numbers"-------
while continueRoutine:
    # get current time
    t = practice_instructions_numbersClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_instructions_numbersClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_instructions_numbersComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_instructions_numbers"-------
for thisComponent in practice_instructions_numbersComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "practice_instructions_numbers" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fixation_cross"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation_crossComponents = [text_7]
for thisComponent in fixation_crossComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation_crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation_cross"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation_crossClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation_crossClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation_crossComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation_cross"-------
for thisComponent in fixation_crossComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# ------Prepare to start Routine "grid"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
gridComponents = [polygon_5, polygon_6]
for thisComponent in gridComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
gridClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "grid"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = gridClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=gridClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_5* updates
    if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_5.frameNStart = frameN  # exact frame index
        polygon_5.tStart = t  # local t and not account for scr refresh
        polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
        polygon_5.setAutoDraw(True)
    if polygon_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_5.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            polygon_5.tStop = t  # not accounting for scr refresh
            polygon_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_5, 'tStopRefresh')  # time at next scr refresh
            polygon_5.setAutoDraw(False)
    
    # *polygon_6* updates
    if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_6.frameNStart = frameN  # exact frame index
        polygon_6.tStart = t  # local t and not account for scr refresh
        polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
        polygon_6.setAutoDraw(True)
    if polygon_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_6.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            polygon_6.tStop = t  # not accounting for scr refresh
            polygon_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_6, 'tStopRefresh')  # time at next scr refresh
            polygon_6.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in gridComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "grid"-------
for thisComponent in gridComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_5.started', polygon_5.tStartRefresh)
thisExp.addData('polygon_5.stopped', polygon_5.tStopRefresh)
thisExp.addData('polygon_6.started', polygon_6.tStartRefresh)
thisExp.addData('polygon_6.stopped', polygon_6.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=20, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "pract_num"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    numpy.random.shuffle(letter)
    numpy.random.shuffle(number)
    
    n = number[0,0]
    l = letter[0,0]
    
    if n == y:
        n = number[1,0]
    
    if l == z:
        l = letter[1,0]
    
    d = (l+''+ str(n))
    
    
    display = str(d)
    
    y = n 
    z = l
    
    if k == 2:
        k = 0
    
    pos = sn[k]
    
    k = k + 1
    
    text_5.setPos(pos)
    text_5.setText(display)
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    pract_numComponents = [polygon, polygon_2, text_5, key_resp_5]
    for thisComponent in pract_numComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pract_numClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pract_num"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pract_numClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pract_numClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)
        
        # *polygon_2* updates
        if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_2.frameNStart = frameN  # exact frame index
            polygon_2.tStart = t  # local t and not account for scr refresh
            polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
            polygon_2.setAutoDraw(True)
        if polygon_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                polygon_2.tStop = t  # not accounting for scr refresh
                polygon_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_2, 'tStopRefresh')  # time at next scr refresh
                polygon_2.setAutoDraw(False)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_5.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_5.tStop = t  # not accounting for scr refresh
                key_resp_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_5, 'tStopRefresh')  # time at next scr refresh
                key_resp_5.status = FINISHED
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['z', 'm'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[0].name  # just the first key pressed
                key_resp_5.rt = _key_resp_5_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pract_numComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pract_num"-------
    for thisComponent in pract_numComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('polygon.started', polygon.tStartRefresh)
    trials_2.addData('polygon.stopped', polygon.tStopRefresh)
    trials_2.addData('polygon_2.started', polygon_2.tStartRefresh)
    trials_2.addData('polygon_2.stopped', polygon_2.tStopRefresh)
    outfile2.write(subNum)
    outfile2.write("\t")
    outfile2.write(display)
    outfile2.write("\t")
    
    if (pos[0] == -.4 and pos[1] == .3): outfile2.write( "repeat" )
    elif (pos[0] == .4 and pos[1] == .3): outfile2.write( "repeat" )
    else: outfile2.write( "repeat" )
    
    outfile2.write("\t")
    outfile2.write(str(pos[0]) + "," + str(pos[1]))
    outfile2.write("\t")
    outfile2.write(str(key_resp_5.keys))
    outfile2.write("\t")
    
    #response = key_resp_5.keys
    #if not response: outfile2.write("Miss")
    #elif (((pos[0] == -.4 and pos[1] == .3) or (pos[0] == .4 and pos[1] == .3)) and response is 'z' and number[0,1] == 0): outfile2.write( "Correct" )
    #elif (((pos[0] == -.4 and pos[1] == .3) or (pos[0] == .4 and pos[1] == .3)) and response is 'm' and number[0,1] == 1): outfile2.write( "Correct" )
    #elif (((pos[0] == -.4 and pos[1] == -.3) or (pos[0] == .4 and pos[1] == -.3)) and response is 'z' and letter[0,1] == 0): outfile2.write( "Correct" )
    #elif (((pos[0] == -.4 and pos[1] == -.3) or (pos[0] == .4 and pos[1] == -.3)) and response is 'm' and letter[0,1] == 1): outfile2.write( "Correct" )
    #else: outfile2.write( "Incorrect")
    
    response = key_resp_5.keys
    if not response: outfile2.write("Miss")
    elif (((pos[0] == -.4 and pos[1] == .3) or (pos[0] == .4 and pos[1] == .3)) and response is 'z' and number[0,1] == 0): outfile2.write( "Correct" )
    elif (((pos[0] == -.4 and pos[1] == .3) or (pos[0] == .4 and pos[1] == .3)) and response is 'm' and number[0,1] == 1): outfile2.write( "Correct" )
    elif (((pos[0] == -.4 and pos[1] == -.3) or (pos[0] == .4 and pos[1] == -.3)) and response is 'z' and letter[0,1] == 0): outfile2.write( "Correct" )
    elif (((pos[0] == -.4 and pos[1] == -.3) or (pos[0] == .4 and pos[1] == -.3)) and response is 'm' and letter[0,1] == 1): outfile2.write( "Correct" )
    else: outfile2.write( "Incorrect")
    
    outfile2.write("\t")
    outfile2.write( str(key_resp_5.rt*1000) )
    outfile2.write("\t")
    outfile2.write( 'practice numbers' )
    outfile2.write("\n")
    trials_2.addData('text_5.started', text_5.tStartRefresh)
    trials_2.addData('text_5.stopped', text_5.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    trials_2.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        trials_2.addData('key_resp_5.rt', key_resp_5.rt)
    trials_2.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    trials_2.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    thisExp.nextEntry()
    
# completed 20 repeats of 'trials_2'


# ------Prepare to start Routine "practice_instructions_letters"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
practice_instructions_lettersComponents = [text_10, key_resp_9]
for thisComponent in practice_instructions_lettersComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_instructions_lettersClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_instructions_letters"-------
while continueRoutine:
    # get current time
    t = practice_instructions_lettersClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_instructions_lettersClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_instructions_lettersComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_instructions_letters"-------
for thisComponent in practice_instructions_lettersComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "practice_instructions_letters" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "grid"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
gridComponents = [polygon_5, polygon_6]
for thisComponent in gridComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
gridClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "grid"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = gridClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=gridClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_5* updates
    if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_5.frameNStart = frameN  # exact frame index
        polygon_5.tStart = t  # local t and not account for scr refresh
        polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
        polygon_5.setAutoDraw(True)
    if polygon_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_5.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            polygon_5.tStop = t  # not accounting for scr refresh
            polygon_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_5, 'tStopRefresh')  # time at next scr refresh
            polygon_5.setAutoDraw(False)
    
    # *polygon_6* updates
    if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_6.frameNStart = frameN  # exact frame index
        polygon_6.tStart = t  # local t and not account for scr refresh
        polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
        polygon_6.setAutoDraw(True)
    if polygon_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_6.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            polygon_6.tStop = t  # not accounting for scr refresh
            polygon_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_6, 'tStopRefresh')  # time at next scr refresh
            polygon_6.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in gridComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "grid"-------
for thisComponent in gridComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_5.started', polygon_5.tStartRefresh)
thisExp.addData('polygon_5.stopped', polygon_5.tStopRefresh)
thisExp.addData('polygon_6.started', polygon_6.tStartRefresh)
thisExp.addData('polygon_6.stopped', polygon_6.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials_3 = data.TrialHandler(nReps=20, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials_3')
thisExp.addLoop(trials_3)  # add the loop to the experiment
thisTrial_3 = trials_3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
if thisTrial_3 != None:
    for paramName in thisTrial_3:
        exec('{} = thisTrial_3[paramName]'.format(paramName))

for thisTrial_3 in trials_3:
    currentLoop = trials_3
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_3.rgb)
    if thisTrial_3 != None:
        for paramName in thisTrial_3:
            exec('{} = thisTrial_3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "pract_let"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    numpy.random.shuffle(letter)
    numpy.random.shuffle(number)
    
    n = number[0,0]  ##diplay
    h = number[0,1]  ##logic
    
    l = letter[0,0]  ##display
    j = letter[0,1]  ##logic
    
    if n == y:
        n = number[1,0]
        h = number[1,1]
    
    if l == z:
        l = letter[1,0]
        j = letter[1,1]
    
    
    d = (l+''+ str(n))
    
    
    display = str(d)
    
    y = n 
    z = l
    
    if k == 2:
        k = 0
    
    pos = sl[k]
    
    k = k + 1
    
    text_6.setPos(pos)
    text_6.setText(display)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    pract_letComponents = [polygon_3, polygon_4, text_6, key_resp_6]
    for thisComponent in pract_letComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pract_letClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pract_let"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pract_letClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pract_letClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *polygon_3* updates
        if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_3.frameNStart = frameN  # exact frame index
            polygon_3.tStart = t  # local t and not account for scr refresh
            polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
            polygon_3.setAutoDraw(True)
        if polygon_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_3.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                polygon_3.tStop = t  # not accounting for scr refresh
                polygon_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_3, 'tStopRefresh')  # time at next scr refresh
                polygon_3.setAutoDraw(False)
        
        # *polygon_4* updates
        if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon_4.frameNStart = frameN  # exact frame index
            polygon_4.tStart = t  # local t and not account for scr refresh
            polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
            polygon_4.setAutoDraw(True)
        if polygon_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon_4.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                polygon_4.tStop = t  # not accounting for scr refresh
                polygon_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon_4, 'tStopRefresh')  # time at next scr refresh
                polygon_4.setAutoDraw(False)
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                text_6.setAutoDraw(False)
        
        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_6.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_6.tStop = t  # not accounting for scr refresh
                key_resp_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_6, 'tStopRefresh')  # time at next scr refresh
                key_resp_6.status = FINISHED
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['z', 'm'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[0].name  # just the first key pressed
                key_resp_6.rt = _key_resp_6_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pract_letComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pract_let"-------
    for thisComponent in pract_letComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_3.addData('polygon_3.started', polygon_3.tStartRefresh)
    trials_3.addData('polygon_3.stopped', polygon_3.tStopRefresh)
    trials_3.addData('polygon_4.started', polygon_4.tStartRefresh)
    trials_3.addData('polygon_4.stopped', polygon_4.tStopRefresh)
    outfile2.write(subNum)
    outfile2.write("\t")
    outfile2.write(display)
    outfile2.write("\t")
    
    if (pos[0] == -.4 and pos[1] == -.3): outfile2.write( "repeat" )
    elif (pos[0] == .4 and pos[1] == -.3): outfile2.write( "repeat" )
    else: outfile2.write( "repeat" )
    
    outfile2.write("\t")
    outfile2.write(str(pos[0]) + "," + str(pos[1]))
    outfile2.write("\t")
    outfile2.write(str(key_resp_6.keys))
    outfile2.write("\t")
    
    response = key_resp_6.keys
    if not response: outfile2.write("Miss")
    elif ((pos[1] == .3) and response is 'z' and h == 0): outfile2.write( "Correct" )
    elif ((pos[1] == .3) and response is 'm' and h == 1): outfile2.write( "Correct" )
    elif ((pos[1] == -.3) and response is 'z' and j == '0'): outfile2.write( "Correct" )
    elif ((pos[1] == -.3) and response is 'm' and j == '1'): outfile2.write( "Correct" )
    else: outfile2.write( "Incorrect")
    
    outfile2.write("\t")
    outfile2.write( str(key_resp_6.rt*1000) )
    outfile2.write("\t")
    outfile2.write( 'practice letters' )
    outfile2.write("\n")
    trials_3.addData('text_6.started', text_6.tStartRefresh)
    trials_3.addData('text_6.stopped', text_6.tStopRefresh)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    trials_3.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        trials_3.addData('key_resp_6.rt', key_resp_6.rt)
    trials_3.addData('key_resp_6.started', key_resp_6.tStartRefresh)
    trials_3.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
    thisExp.nextEntry()
    
# completed 20 repeats of 'trials_3'


# ------Prepare to start Routine "prac_complete"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
prac_completeComponents = [text_8, key_resp_7]
for thisComponent in prac_completeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
prac_completeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "prac_complete"-------
while continueRoutine:
    # get current time
    t = prac_completeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=prac_completeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prac_completeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "prac_complete"-------
for thisComponent in prac_completeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
#k=0
# the Routine "prac_complete" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "reminder"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_4.keys = []
key_resp_4.rt = []
_key_resp_4_allKeys = []
# keep track of which components have finished
reminderComponents = [text_4, key_resp_4]
for thisComponent in reminderComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
reminderClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "reminder"-------
while continueRoutine:
    # get current time
    t = reminderClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=reminderClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *key_resp_4* updates
    waitOnFlip = False
    if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.tStart = t  # local t and not account for scr refresh
        key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_4.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_4_allKeys.extend(theseKeys)
        if len(_key_resp_4_allKeys):
            key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
            key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in reminderComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "reminder"-------
for thisComponent in reminderComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
    key_resp_4.keys = None
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.addData('key_resp_4.started', key_resp_4.tStartRefresh)
thisExp.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
thisExp.nextEntry()
# the Routine "reminder" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fixation_cross"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
fixation_crossComponents = [text_7]
for thisComponent in fixation_crossComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
fixation_crossClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fixation_cross"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = fixation_crossClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=fixation_crossClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation_crossComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation_cross"-------
for thisComponent in fixation_crossComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# ------Prepare to start Routine "grid"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
gridComponents = [polygon_5, polygon_6]
for thisComponent in gridComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
gridClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "grid"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = gridClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=gridClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_5* updates
    if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_5.frameNStart = frameN  # exact frame index
        polygon_5.tStart = t  # local t and not account for scr refresh
        polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
        polygon_5.setAutoDraw(True)
    if polygon_5.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_5.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            polygon_5.tStop = t  # not accounting for scr refresh
            polygon_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_5, 'tStopRefresh')  # time at next scr refresh
            polygon_5.setAutoDraw(False)
    
    # *polygon_6* updates
    if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_6.frameNStart = frameN  # exact frame index
        polygon_6.tStart = t  # local t and not account for scr refresh
        polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
        polygon_6.setAutoDraw(True)
    if polygon_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > polygon_6.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            polygon_6.tStop = t  # not accounting for scr refresh
            polygon_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(polygon_6, 'tStopRefresh')  # time at next scr refresh
            polygon_6.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in gridComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "grid"-------
for thisComponent in gridComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_5.started', polygon_5.tStartRefresh)
thisExp.addData('polygon_5.stopped', polygon_5.tStopRefresh)
thisExp.addData('polygon_6.started', polygon_6.tStartRefresh)
thisExp.addData('polygon_6.stopped', polygon_6.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=152, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "qtr"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    numpy.random.shuffle(letter)
    numpy.random.shuffle(number)
    
    n = number[0,0]
    l = letter[0,0]
    
    if n == y:
        n = number[1,0]
    
    if l == z:
        l = letter[1,0]
    
    d = (l+''+ str(n))
    
    
    display = str(d)
    
    y = n 
    z = l
    
    if k == 4:
        k = 0
    
    pos = s[k]
    
    k = k + 1
    
    text.setPos(pos)
    text.setText(display)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    qtrComponents = [quadhor, quadvert, text, key_resp]
    for thisComponent in qtrComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    qtrClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "qtr"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = qtrClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=qtrClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *quadhor* updates
        if quadhor.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            quadhor.frameNStart = frameN  # exact frame index
            quadhor.tStart = t  # local t and not account for scr refresh
            quadhor.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(quadhor, 'tStartRefresh')  # time at next scr refresh
            quadhor.setAutoDraw(True)
        if quadhor.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > quadhor.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                quadhor.tStop = t  # not accounting for scr refresh
                quadhor.frameNStop = frameN  # exact frame index
                win.timeOnFlip(quadhor, 'tStopRefresh')  # time at next scr refresh
                quadhor.setAutoDraw(False)
        
        # *quadvert* updates
        if quadvert.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            quadvert.frameNStart = frameN  # exact frame index
            quadvert.tStart = t  # local t and not account for scr refresh
            quadvert.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(quadvert, 'tStartRefresh')  # time at next scr refresh
            quadvert.setAutoDraw(True)
        if quadvert.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > quadvert.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                quadvert.tStop = t  # not accounting for scr refresh
                quadvert.frameNStop = frameN  # exact frame index
                win.timeOnFlip(quadvert, 'tStopRefresh')  # time at next scr refresh
                quadvert.setAutoDraw(False)
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['z', 'm'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[0].name  # just the first key pressed
                key_resp.rt = _key_resp_allKeys[0].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in qtrComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "qtr"-------
    for thisComponent in qtrComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('quadhor.started', quadhor.tStartRefresh)
    trials.addData('quadhor.stopped', quadhor.tStopRefresh)
    trials.addData('quadvert.started', quadvert.tStartRefresh)
    trials.addData('quadvert.stopped', quadvert.tStopRefresh)
    outfile.write(subNum)
    outfile.write("\t")
    outfile.write(display)
    outfile.write("\t")
    
    if (pos[0] == -.4 and pos[1] == .3): outfile.write( "switch" )
    elif (pos[0] == .4 and pos[1] == -.3): outfile.write( "switch" )
    else: outfile.write( "repeat" )
    
    outfile.write("\t")
    outfile.write(str(pos[0]) + "," + str(pos[1]))
    outfile.write("\t")
    outfile.write(str(key_resp.keys))
    outfile.write("\t")
    
    response = key_resp.keys
    if not response: outfile.write("Miss")
    elif (((pos[0] == -.4 and pos[1] == .3) or (pos[0] == .4 and pos[1] == .3)) and response is 'z' and number[0,1] == 0): outfile.write( "Correct" )
    elif (((pos[0] == -.4 and pos[1] == .3) or (pos[0] == .4 and pos[1] == .3)) and response is 'm' and number[0,1] == 1): outfile.write( "Correct" )
    elif (((pos[0] == -.4 and pos[1] == -.3) or (pos[0] == .4 and pos[1] == -.3)) and response is 'z' and letter[0,1] == 0): outfile.write( "Correct" )
    elif (((pos[0] == -.4 and pos[1] == -.3) or (pos[0] == .4 and pos[1] == -.3)) and response is 'm' and letter[0,1] == 1): outfile.write( "Correct" )
    else: outfile.write( "Incorrect")
    
    outfile.write("\t")
    outfile.write( str(key_resp.rt*1000) )
    outfile.write("\n")
    
    
    outfile2.write(subNum)
    outfile2.write("\t")
    outfile2.write(display)
    outfile2.write("\t")
    
    if (pos[0] == -.4 and pos[1] == .3): outfile2.write( "switch" )
    elif (pos[0] == .4 and pos[1] == -.3): outfile2.write( "switch" )
    else: outfile2.write( "repeat" )
    
    outfile2.write("\t")
    outfile2.write(str(pos[0]) + "," + str(pos[1]))
    outfile2.write("\t")
    outfile2.write(str(key_resp.keys))
    outfile2.write("\t")
    
    response = key_resp.keys
    if not response: outfile2.write("Miss")
    elif (((pos[0] == -.4 and pos[1] == .3) or (pos[0] == .4 and pos[1] == .3)) and response is 'z' and number[0,1] == 0): outfile2.write( "Correct" )
    elif (((pos[0] == -.4 and pos[1] == .3) or (pos[0] == .4 and pos[1] == .3)) and response is 'm' and number[0,1] == 1): outfile2.write( "Correct" )
    elif (((pos[0] == -.4 and pos[1] == -.3) or (pos[0] == .4 and pos[1] == -.3)) and response is 'z' and letter[0,1] == 0): outfile2.write( "Correct" )
    elif (((pos[0] == -.4 and pos[1] == -.3) or (pos[0] == .4 and pos[1] == -.3)) and response is 'm' and letter[0,1] == 1): outfile2.write( "Correct" )
    else: outfile2.write( "Incorrect")
    
    outfile2.write("\t")
    outfile2.write( str(key_resp.rt*1000) )
    outfile2.write("\n")
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        trials.addData('key_resp.rt', key_resp.rt)
    trials.addData('key_resp.started', key_resp.tStartRefresh)
    trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    thisExp.nextEntry()
    
# completed 152 repeats of 'trials'


# ------Prepare to start Routine "end_instructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
end_instructionsComponents = [text_2, key_resp_2]
for thisComponent in end_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
end_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end_instructions"-------
while continueRoutine:
    # get current time
    t = end_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=end_instructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['esc'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in end_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end_instructions"-------
for thisComponent in end_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "end_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
