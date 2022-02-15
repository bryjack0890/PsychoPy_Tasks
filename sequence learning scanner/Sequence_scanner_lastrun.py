#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.2),
    on Mon Jul  8 12:26:14 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division

import psychopy
psychopy.useVersion('3.1.2')

from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.2'
expName = 'Sequence'  # from the Builder filename that created this script
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
    originPath='/Users/Teddy/Desktop/Psychopy task/sequence learning scanner/Sequence_scanner_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruction"
instructionClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='In this task your goal is to learn a sequence. You will see four rectangles in the center of the screen that represent your left middle, left index, right index, and right middle fingers. \n\nPlease place your fingers over the response box, as instructed previously, when performing this task.',
    font='Arial',
    pos=(0, 0), height=.1, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
subNum = expInfo['participant']
sessionNum = expInfo['session']
outfile= open("./data/sequence.txt","a+")
outfile.write("subject")
outfile.write("\t")
outfile.write("stim")
outfile.write("\t")
outfile.write("sequence")
outfile.write("\t")
outfile.write("trial")
outfile.write("\t")
outfile.write("cue")
outfile.write("\t")
outfile.write("response")
outfile.write("\t")
outfile.write("accuracy")
outfile.write("\t")
outfile.write("rt")
outfile.write("\t")
outfile.write("trial.onset")
outfile.write("\t")
outfile.write("trial.duration")
outfile.write("\n")



outfile2= open("./data/" + subNum + "_" + sessionNum + "_sequence.txt", "a+")
outfile2.write("timestamp: ")
outfile2.write(expInfo['date'])
outfile2.write("\n")
outfile2.write("subject")
outfile2.write("\t")
outfile2.write("stim")
outfile2.write("\t")
outfile2.write("sequence")
outfile2.write("\t")
outfile2.write("trial")
outfile2.write("\t")
outfile2.write("cue")
outfile2.write("\t")
outfile2.write("response")
outfile2.write("\t")
outfile2.write("accuracy")
outfile2.write("\t")
outfile2.write("rt")
outfile2.write("\t")
outfile2.write("trial.onset")
outfile2.write("\t")
outfile2.write("trial.duration")
outfile2.write("\t")
outfile2.write("block.duration")
outfile2.write("\n")

# Initialize components for Routine "instruction2"
instruction2Clock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Your goal is to press the corresponding button as quickly as possible when a rectangle on the screen is shaded black. Press the button that corresponds to that rectangle location from left to right.\n\nPlease respond as quickly as possible, but it is important that you wait until the rectangle is shaded. Please do not respond until the rectangle changes color!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instruction3"
instruction3Clock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Finally, sometimes you will be pressing buttons in a random order. Again, please press them as quickly as possible.\n\nWhen you see the letter “R” that means the upcoming button presses will be random. When you see the letter “S” that means the upcoming button presses are part of the sequence you are to learn. The beginning of the sequence is denoted by a red box.',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "instruction4"
instruction4Clock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='You will complete three runs of this task. Within each run, you will complete 5 blocks.\n\nEach run will last about 5 minutes.\n\nQuestions?',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=1.75, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PleaseWait"
PleaseWaitClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='Please Wait',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trigger"
triggerClock = core.Clock()
text_trigger = visual.TextStim(win=win, name='text_trigger',
    text=' ',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "SequenceRS"
SequenceRSClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='Black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "sequenceselect"
sequenceselectClock = core.Clock()
responseR = 0
responseS = 0

counterR = 0
counterS = 0

# Initialize components for Routine "SequenceR"
SequenceRClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2, 2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "SequenceS"
SequenceSClock = core.Clock()
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(2,2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "blockduration"
blockdurationClock = core.Clock()

# Initialize components for Routine "fixcross"
fixcrossClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "EndInstructions"
EndInstructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='You have completed the experiment!',
    font='Arial',
    pos=(0, 0), height=0.075, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instruction"-------
t = 0
instructionClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp = keyboard.Keyboard()
# keep track of which components have finished
instructionComponents = [text, key_resp]
for thisComponent in instructionComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruction"-------
while continueRoutine:
    # get current time
    t = instructionClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # not accounting for scr refresh
        text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    if t >= 0.0 and key_resp.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp.tStart = t  # not accounting for scr refresh
        key_resp.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        key_resp.clearEvents(eventType='keyboard')
    if key_resp.status == STARTED:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp.keys = theseKeys.name  # just the last key pressed
            key_resp.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructionComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction"-------
for thisComponent in instructionComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction2"-------
t = 0
instruction2Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_2 = keyboard.Keyboard()
# keep track of which components have finished
instruction2Components = [text_2, key_resp_2]
for thisComponent in instruction2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruction2"-------
while continueRoutine:
    # get current time
    t = instruction2Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if t >= 0.0 and text_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_2.tStart = t  # not accounting for scr refresh
        text_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # not accounting for scr refresh
        key_resp_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        key_resp_2.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_2.keys = theseKeys.name  # just the last key pressed
            key_resp_2.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction2"-------
for thisComponent in instruction2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction3"-------
t = 0
instruction3Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_3 = keyboard.Keyboard()
# keep track of which components have finished
instruction3Components = [text_3, key_resp_3]
for thisComponent in instruction3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruction3"-------
while continueRoutine:
    # get current time
    t = instruction3Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_3* updates
    if t >= 0.0 and text_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_3.tStart = t  # not accounting for scr refresh
        text_3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_3* updates
    if t >= 0.0 and key_resp_3.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_3.tStart = t  # not accounting for scr refresh
        key_resp_3.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        key_resp_3.clearEvents(eventType='keyboard')
    if key_resp_3.status == STARTED:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_3.keys = theseKeys.name  # just the last key pressed
            key_resp_3.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction3"-------
for thisComponent in instruction3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "instruction4"-------
t = 0
instruction4Clock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_9 = keyboard.Keyboard()
# keep track of which components have finished
instruction4Components = [text_8, key_resp_9]
for thisComponent in instruction4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruction4"-------
while continueRoutine:
    # get current time
    t = instruction4Clock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_8* updates
    if t >= 0.0 and text_8.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_8.tStart = t  # not accounting for scr refresh
        text_8.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # *key_resp_9* updates
    if t >= 0.0 and key_resp_9.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_9.tStart = t  # not accounting for scr refresh
        key_resp_9.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        key_resp_9.clearEvents(eventType='keyboard')
    if key_resp_9.status == STARTED:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_9.keys = theseKeys.name  # just the last key pressed
            key_resp_9.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instruction4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruction4"-------
for thisComponent in instruction4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruction4" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=3, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "PleaseWait"-------
    t = 0
    PleaseWaitClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4 = keyboard.Keyboard()
    # keep track of which components have finished
    PleaseWaitComponents = [text_4, key_resp_4]
    for thisComponent in PleaseWaitComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "PleaseWait"-------
    while continueRoutine:
        # get current time
        t = PleaseWaitClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t  # not accounting for scr refresh
            text_4.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        
        # *key_resp_4* updates
        if t >= 2 and key_resp_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_4.tStart = t  # not accounting for scr refresh
            key_resp_4.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            key_resp_4.clearEvents(eventType='keyboard')
        if key_resp_4.status == STARTED:
            theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_4.keys = theseKeys.name  # just the last key pressed
                key_resp_4.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PleaseWaitComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PleaseWait"-------
    for thisComponent in PleaseWaitComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    block.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        block.addData('key_resp_4.rt', key_resp_4.rt)
    block.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    block.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    import time
    
    start_time_block = time.perf_counter() 
    # the Routine "PleaseWait" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trigger"-------
    t = 0
    triggerClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_8 = keyboard.Keyboard()
    # keep track of which components have finished
    triggerComponents = [text_trigger, key_resp_8]
    for thisComponent in triggerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trigger"-------
    while continueRoutine:
        # get current time
        t = triggerClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_trigger* updates
        if t >= 0.0 and text_trigger.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_trigger.tStart = t  # not accounting for scr refresh
            text_trigger.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_trigger, 'tStartRefresh')  # time at next scr refresh
            text_trigger.setAutoDraw(True)
        
        # *key_resp_8* updates
        if t >= 0.0 and key_resp_8.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_8.tStart = t  # not accounting for scr refresh
            key_resp_8.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            key_resp_8.clearEvents(eventType='keyboard')
        if key_resp_8.status == STARTED:
            theseKeys = key_resp_8.getKeys(keyList=['T', 't'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                key_resp_8.keys = theseKeys.name  # just the last key pressed
                key_resp_8.rt = theseKeys.rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in triggerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trigger"-------
    for thisComponent in triggerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block.addData('text_trigger.started', text_trigger.tStartRefresh)
    block.addData('text_trigger.stopped', text_trigger.tStopRefresh)
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys = None
    block.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        block.addData('key_resp_8.rt', key_resp_8.rt)
    block.addData('key_resp_8.started', key_resp_8.tStartRefresh)
    block.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
    # the Routine "trigger" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials_3 = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('sequence.xlsx'),
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
        
        # ------Prepare to start Routine "SequenceRS"-------
        t = 0
        SequenceRSClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(20.000000)
        # update component parameters for each repeat
        text_5.setText(sequence)
        # keep track of which components have finished
        SequenceRSComponents = [text_5]
        for thisComponent in SequenceRSComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "SequenceRS"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = SequenceRSClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text_5* updates
            if t >= 0.0 and text_5.status == NOT_STARTED:
                # keep track of start time/frame for later
                text_5.tStart = t  # not accounting for scr refresh
                text_5.frameNStart = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            frameRemains = 0.0 + 20- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text_5.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SequenceRSComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "SequenceRS"-------
        for thisComponent in SequenceRSComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        start_time = time.perf_counter() 
        
        # ------Prepare to start Routine "sequenceselect"-------
        t = 0
        sequenceselectClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        if sequence == 'R':
            responseR = 1
            responseS = 0
        else:
            responseR = 0
            responseS = 1
        
        
        
        counterR = 0
        counterS = 0
        # keep track of which components have finished
        sequenceselectComponents = []
        for thisComponent in sequenceselectComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "sequenceselect"-------
        while continueRoutine:
            # get current time
            t = sequenceselectClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in sequenceselectComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "sequenceselect"-------
        for thisComponent in sequenceselectComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "sequenceselect" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=responseR, method='random', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('image_name_random.xlsx'),
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
            
            # set up handler to look after randomisation of conditions etc
            trials_4 = data.TrialHandler(nReps=18, method='random', 
                extraInfo=expInfo, originPath=-1,
                trialList=[None],
                seed=None, name='trials_4')
            thisExp.addLoop(trials_4)  # add the loop to the experiment
            thisTrial_4 = trials_4.trialList[0]  # so we can initialise stimuli with some values
            # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
            if thisTrial_4 != None:
                for paramName in thisTrial_4:
                    exec('{} = thisTrial_4[paramName]'.format(paramName))
            
            for thisTrial_4 in trials_4:
                currentLoop = trials_4
                # abbreviate parameter names if possible (e.g. rgb = thisTrial_4.rgb)
                if thisTrial_4 != None:
                    for paramName in thisTrial_4:
                        exec('{} = thisTrial_4[paramName]'.format(paramName))
                
                # ------Prepare to start Routine "SequenceR"-------
                t = 0
                SequenceRClock.reset()  # clock
                frameN = -1
                continueRoutine = True
                routineTimer.add(1.002000)
                # update component parameters for each repeat
                image.setImage(image_name_random)
                image_3.setImage('InstructionCues/InstructionCue5.PNG')
                counterR = counterR + 1
                
                trial_onset_time = time.perf_counter() - start_time
                
                if counterR > 17:
                    trials.finished = 1
                
                
                
                key_resp_5 = keyboard.Keyboard()
                # keep track of which components have finished
                SequenceRComponents = [image, image_3, key_resp_5]
                for thisComponent in SequenceRComponents:
                    thisComponent.tStart = None
                    thisComponent.tStop = None
                    thisComponent.tStartRefresh = None
                    thisComponent.tStopRefresh = None
                    if hasattr(thisComponent, 'status'):
                        thisComponent.status = NOT_STARTED
                
                # -------Start Routine "SequenceR"-------
                while continueRoutine and routineTimer.getTime() > 0:
                    # get current time
                    t = SequenceRClock.getTime()
                    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                    # update/draw components on each frame
                    
                    # *image* updates
                    if t >= 0 and image.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        image.tStart = t  # not accounting for scr refresh
                        image.frameNStart = frameN  # exact frame index
                        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                        image.setAutoDraw(True)
                    frameRemains = 0 + .21- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if image.status == STARTED and t >= frameRemains:
                        # keep track of stop time/frame for later
                        image.tStop = t  # not accounting for scr refresh
                        image.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                        image.setAutoDraw(False)
                    
                    # *image_3* updates
                    if t >= 0.19 and image_3.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        image_3.tStart = t  # not accounting for scr refresh
                        image_3.frameNStart = frameN  # exact frame index
                        win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                        image_3.setAutoDraw(True)
                    frameRemains = 0.19 + .812- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if image_3.status == STARTED and t >= frameRemains:
                        # keep track of stop time/frame for later
                        image_3.tStop = t  # not accounting for scr refresh
                        image_3.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                        image_3.setAutoDraw(False)
                    
                    # *key_resp_5* updates
                    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
                        # keep track of start time/frame for later
                        key_resp_5.tStart = t  # not accounting for scr refresh
                        key_resp_5.frameNStart = frameN  # exact frame index
                        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                        key_resp_5.status = STARTED
                        # keyboard checking is just starting
                        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                        key_resp_5.clearEvents(eventType='keyboard')
                    frameRemains = 0.0 + 1.002- win.monitorFramePeriod * 0.75  # most of one frame period left
                    if key_resp_5.status == STARTED and t >= frameRemains:
                        # keep track of stop time/frame for later
                        key_resp_5.tStop = t  # not accounting for scr refresh
                        key_resp_5.frameNStop = frameN  # exact frame index
                        win.timeOnFlip(key_resp_5, 'tStopRefresh')  # time at next scr refresh
                        key_resp_5.status = FINISHED
                    if key_resp_5.status == STARTED:
                        theseKeys = key_resp_5.getKeys(keyList=['1', '2', '3', '4', 'a', 'b', 'c', 'd', 'A', 'B', 'C', 'D'], waitRelease=False)
                        if len(theseKeys):
                            theseKeys = theseKeys[0]  # at least one key was pressed
                            
                            # check for quit:
                            if "escape" == theseKeys:
                                endExpNow = True
                            if key_resp_5.keys == []:  # then this was the first keypress
                                key_resp_5.keys = theseKeys.name  # just the first key pressed
                                key_resp_5.rt = theseKeys.rt
                                # was this 'correct'?
                                if (key_resp_5.keys == str(responseR)) or (key_resp_5.keys == responseR):
                                    key_resp_5.corr = 1
                                else:
                                    key_resp_5.corr = 0
                    
                    # check for quit (typically the Esc key)
                    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                        core.quit()
                    
                    # check if all components have finished
                    if not continueRoutine:  # a component has requested a forced-end of Routine
                        break
                    continueRoutine = False  # will revert to True if at least one component still running
                    for thisComponent in SequenceRComponents:
                        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                            continueRoutine = True
                            break  # at least one component has not yet finished
                    
                    # refresh the screen
                    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                        win.flip()
                
                # -------Ending Routine "SequenceR"-------
                for thisComponent in SequenceRComponents:
                    if hasattr(thisComponent, "setAutoDraw"):
                        thisComponent.setAutoDraw(False)
                if key_resp_5.corr != 0 or counterR > 17: 
                    trials_4.finished = 1
                
                block_end_time = time.perf_counter() - start_time
                
                outfile.write(subNum)
                outfile.write("\t")
                outfile.write(sessionNum)
                outfile.write("\t")
                outfile.write(sequence)
                outfile.write("\t")
                outfile.write(str(counterR))
                outfile.write("\t")
                outfile.write(image_name_random)
                outfile.write("\t")
                #response
                if not key_resp_5.keys : #if no response
                    outfile.write("Miss")
                else:
                    outfile.write(str(key_resp_5.keys))
                outfile.write("\t")
                #accuracy
                if not key_resp_5.keys : #if no response
                    outfile.write("Miss")
                else:
                    outfile.write(str(key_resp_5.corr))
                outfile.write("\t")
                #rt
                if not key_resp_5.keys : #if no response
                    outfile.write("0")
                else:
                    outfile.write(str(key_resp_5.rt*1000))
                outfile.write("\t")
                outfile.write(str(trial_onset_time))
                outfile.write("\t")
                outfile.write(str(t))
                outfile.write("\n")
                
                
                outfile2.write(subNum)
                outfile2.write("\t")
                outfile2.write(sessionNum)
                outfile2.write("\t")
                outfile2.write(sequence)
                outfile2.write("\t")
                outfile2.write(str(counterR))
                outfile2.write("\t")
                outfile2.write(image_name_random)
                outfile2.write("\t")
                #response
                if not key_resp_5.keys : #if no response
                    outfile2.write("Miss")
                else:
                    outfile2.write(str(key_resp_5.keys))
                outfile2.write("\t")
                #accuracy
                if not key_resp_5.keys : #if no response
                    outfile2.write("Miss")
                else:
                    outfile2.write(str(key_resp_5.corr))
                outfile2.write("\t")
                #rt
                if not key_resp_5.keys : #if no response
                    outfile2.write("0")
                else:
                    outfile2.write(str(key_resp_5.rt*1000))
                outfile2.write("\t")
                outfile2.write(str(trial_onset_time))
                outfile2.write("\t")
                outfile2.write(str(t))
                outfile2.write("\t")
                outfile2.write(str(block_end_time))
                outfile2.write("\n")
                # check responses
                if key_resp_5.keys in ['', [], None]:  # No response was made
                    key_resp_5.keys = None
                    # was no response the correct answer?!
                    if str(responseR).lower() == 'none':
                       key_resp_5.corr = 1;  # correct non-response
                    else:
                       key_resp_5.corr = 0;  # failed to respond (incorrectly)
                # store data for trials_4 (TrialHandler)
                trials_4.addData('key_resp_5.keys',key_resp_5.keys)
                trials_4.addData('key_resp_5.corr', key_resp_5.corr)
                if key_resp_5.keys != None:  # we had a response
                    trials_4.addData('key_resp_5.rt', key_resp_5.rt)
                trials_4.addData('key_resp_5.started', key_resp_5.tStartRefresh)
                trials_4.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
                thisExp.nextEntry()
                
            # completed 18 repeats of 'trials_4'
            
            thisExp.nextEntry()
            
        # completed responseR repeats of 'trials'
        
        
        # set up handler to look after randomisation of conditions etc
        trials_2 = data.TrialHandler(nReps=responseS, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('image_name_sequnce.xlsx'),
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
            
            # ------Prepare to start Routine "SequenceS"-------
            t = 0
            SequenceSClock.reset()  # clock
            frameN = -1
            continueRoutine = True
            routineTimer.add(1.002000)
            # update component parameters for each repeat
            image_5.setImage(image_name_sequence)
            image_4.setImage('InstructionCues/InstructionCue5.PNG')
            counterS = counterS + 1
            
            trial_onset_time = time.perf_counter() - start_time
            
            if counterS > 35:
                trials.finished = 1
            
            
            key_resp_7 = keyboard.Keyboard()
            # keep track of which components have finished
            SequenceSComponents = [image_5, image_4, key_resp_7]
            for thisComponent in SequenceSComponents:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            
            # -------Start Routine "SequenceS"-------
            while continueRoutine and routineTimer.getTime() > 0:
                # get current time
                t = SequenceSClock.getTime()
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_5* updates
                if t >= 0 and image_5.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_5.tStart = t  # not accounting for scr refresh
                    image_5.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
                    image_5.setAutoDraw(True)
                frameRemains = 0 + .21- win.monitorFramePeriod * 0.75  # most of one frame period left
                if image_5.status == STARTED and t >= frameRemains:
                    # keep track of stop time/frame for later
                    image_5.tStop = t  # not accounting for scr refresh
                    image_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_5, 'tStopRefresh')  # time at next scr refresh
                    image_5.setAutoDraw(False)
                
                # *image_4* updates
                if t >= .19 and image_4.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    image_4.tStart = t  # not accounting for scr refresh
                    image_4.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                    image_4.setAutoDraw(True)
                frameRemains = .19 + .812- win.monitorFramePeriod * 0.75  # most of one frame period left
                if image_4.status == STARTED and t >= frameRemains:
                    # keep track of stop time/frame for later
                    image_4.tStop = t  # not accounting for scr refresh
                    image_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(image_4, 'tStopRefresh')  # time at next scr refresh
                    image_4.setAutoDraw(False)
                
                # *key_resp_7* updates
                if t >= 0.0 and key_resp_7.status == NOT_STARTED:
                    # keep track of start time/frame for later
                    key_resp_7.tStart = t  # not accounting for scr refresh
                    key_resp_7.frameNStart = frameN  # exact frame index
                    win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                    key_resp_7.status = STARTED
                    # keyboard checking is just starting
                    win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                    key_resp_7.clearEvents(eventType='keyboard')
                frameRemains = 0.0 + 1.002- win.monitorFramePeriod * 0.75  # most of one frame period left
                if key_resp_7.status == STARTED and t >= frameRemains:
                    # keep track of stop time/frame for later
                    key_resp_7.tStop = t  # not accounting for scr refresh
                    key_resp_7.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_7, 'tStopRefresh')  # time at next scr refresh
                    key_resp_7.status = FINISHED
                if key_resp_7.status == STARTED:
                    theseKeys = key_resp_7.getKeys(keyList=['1', '2', '3', '4', 'a', 'b', 'c', 'd', 'A', 'B', 'C', 'D'], waitRelease=False)
                    if len(theseKeys):
                        theseKeys = theseKeys[0]  # at least one key was pressed
                        
                        # check for quit:
                        if "escape" == theseKeys:
                            endExpNow = True
                        if key_resp_7.keys == []:  # then this was the first keypress
                            key_resp_7.keys = theseKeys.name  # just the first key pressed
                            key_resp_7.rt = theseKeys.rt
                            # was this 'correct'?
                            if (key_resp_7.keys == str(responseS)) or (key_resp_7.keys == responseS):
                                key_resp_7.corr = 1
                            else:
                                key_resp_7.corr = 0
                
                # check for quit (typically the Esc key)
                if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                    core.quit()
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in SequenceSComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # -------Ending Routine "SequenceS"-------
            for thisComponent in SequenceSComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            block_end_time = time.perf_counter() - start_time
            
            outfile.write(subNum)
            outfile.write("\t")
            outfile.write(sessionNum)
            outfile.write("\t")
            outfile.write(sequence)
            outfile.write("\t")
            outfile.write(str(counterS))
            outfile.write("\t")
            outfile.write(image_name_sequence)
            outfile.write("\t")
            #response
            if not key_resp_7.keys : #if no response
                outfile.write("Miss")
            else:
                outfile.write(str(key_resp_7.keys))
            outfile.write("\t")
            #accuracy
            if not key_resp_7.keys : #if no response
                outfile.write("Miss")
            else:
                outfile.write(str(key_resp_7.corr))
            outfile.write("\t")
            #rt
            if not key_resp_7.keys : #if no response
                outfile.write("0")
            else:
                outfile.write(str(key_resp_7.rt*1000))
            outfile.write("\t")
            outfile.write(str(trial_onset_time))
            outfile.write("\t")
            outfile.write(str(t))
            outfile.write("\n")
            
            
            outfile2.write(subNum)
            outfile2.write("\t")
            outfile2.write(sessionNum)
            outfile2.write("\t")
            outfile2.write(sequence)
            outfile2.write("\t")
            outfile2.write(str(counterS))
            outfile2.write("\t")
            outfile2.write(image_name_sequence)
            outfile2.write("\t")
            #response
            if not key_resp_7.keys : #if no response
                outfile2.write("Miss")
            else:
                outfile2.write(str(key_resp_7.keys))
            outfile2.write("\t")
            #accuracy
            if not key_resp_7.keys : #if no response
                outfile2.write("Miss")
            else:
                outfile2.write(str(key_resp_7.corr))
            outfile2.write("\t")
            #rt
            if not key_resp_7.keys : #if no response
                outfile2.write("0")
            else:
                outfile2.write(str(key_resp_7.rt*1000))
            outfile2.write("\t")
            outfile2.write(str(trial_onset_time))
            outfile2.write("\t")
            outfile2.write(str(t))
            outfile2.write("\t")
            outfile2.write(str(block_end_time))
            outfile2.write("\n")
            # check responses
            if key_resp_7.keys in ['', [], None]:  # No response was made
                key_resp_7.keys = None
                # was no response the correct answer?!
                if str(responseS).lower() == 'none':
                   key_resp_7.corr = 1;  # correct non-response
                else:
                   key_resp_7.corr = 0;  # failed to respond (incorrectly)
            # store data for trials_2 (TrialHandler)
            trials_2.addData('key_resp_7.keys',key_resp_7.keys)
            trials_2.addData('key_resp_7.corr', key_resp_7.corr)
            if key_resp_7.keys != None:  # we had a response
                trials_2.addData('key_resp_7.rt', key_resp_7.rt)
            trials_2.addData('key_resp_7.started', key_resp_7.tStartRefresh)
            trials_2.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
            thisExp.nextEntry()
            
        # completed responseS repeats of 'trials_2'
        
        
        # ------Prepare to start Routine "blockduration"-------
        t = 0
        blockdurationClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        block_end_time = time.perf_counter() - start_time
        
        task_time = time.perf_counter() - start_time_block
        
        # keep track of which components have finished
        blockdurationComponents = []
        for thisComponent in blockdurationComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "blockduration"-------
        while continueRoutine:
            # get current time
            t = blockdurationClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in blockdurationComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "blockduration"-------
        for thisComponent in blockdurationComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        outfile2.write("\t")
        outfile2.write("\t")
        outfile2.write("\t")
        outfile2.write("\t")
        outfile2.write("\t")
        outfile2.write("\t")
        outfile2.write("\t")
        outfile2.write("\t")
        outfile2.write("\t")
        outfile2.write("\t")
        outfile2.write(str(block_end_time))
        outfile2.write("\t")
        outfile2.write(str(task_time))
        outfile2.write("\n")
        
        
        # the Routine "blockduration" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1 repeats of 'trials_3'
    
    
    # ------Prepare to start Routine "fixcross"-------
    t = 0
    fixcrossClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixcrossComponents = [text_7]
    for thisComponent in fixcrossComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "fixcross"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixcrossClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if t >= 0.0 and text_7.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_7.tStart = t  # not accounting for scr refresh
            text_7.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        frameRemains = 0.0 + 20- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_7.status == STARTED and t >= frameRemains:
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
        for thisComponent in fixcrossComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fixcross"-------
    for thisComponent in fixcrossComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block.addData('text_7.started', text_7.tStartRefresh)
    block.addData('text_7.stopped', text_7.tStopRefresh)
# completed 3 repeats of 'block'


# ------Prepare to start Routine "EndInstructions"-------
t = 0
EndInstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_6 = keyboard.Keyboard()
outfile2.write("timestamp: ")
outfile2.write(expInfo['date'])
# keep track of which components have finished
EndInstructionsComponents = [text_6, key_resp_6]
for thisComponent in EndInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "EndInstructions"-------
while continueRoutine:
    # get current time
    t = EndInstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if t >= 0.0 and text_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_6.tStart = t  # not accounting for scr refresh
        text_6.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_6* updates
    if t >= 0.0 and key_resp_6.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_6.tStart = t  # not accounting for scr refresh
        key_resp_6.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        key_resp_6.clearEvents(eventType='keyboard')
    if key_resp_6.status == STARTED:
        theseKeys = key_resp_6.getKeys(keyList=['esc'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            key_resp_6.keys = theseKeys.name  # just the last key pressed
            key_resp_6.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndInstructions"-------
for thisComponent in EndInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "EndInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
