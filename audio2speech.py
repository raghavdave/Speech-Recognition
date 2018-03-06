# -*- coding: utf-8 -*-
"""
Created on Fri Sep 08 14:14:18 2017

@author: raghavdave
"""
import os
from converter import Converter
import speech_recognition as sr

os.chdir('dir')

r.pause_threshold = 2

def audio_rec():
    r=sr.Recognizer()
    r.dynamic_energy_threshold = True
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        return audio
        
def audio2speech(input):
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        # print("You said: " + r.recognize_google(input)) 
        test = r.recognize_google(input,show_all=True)    
        unlist = test.values()[0]
        undict = list()
        undict1 = list()
        for i in range(len(unlist)):
            undict1 = unlist[i].values()
            undict.append(undict1)
        undict.sort
        main = undict[len(unlist)-1][1]
        print("You said: " + main)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


sentence = audio_rec()
audio2speech(sentence)

test = r.recognize_google(audio,show_all=True)    
unlist = test.values()[0]
undict = list()
undict1 = list()
for i in range(len(unlist)):
    undict1 = unlist[i].values()
    undict.append(undict1)

undict.sort
main = undict[len(unlist)-1][1]

r = sr.Recognizer()
r.pause_threshold = 0.8

with sr.WavFile("test1.wav") as source:              # use "test.wav" as the audio source
    audio = r.record(source)    
    
reduce()
for key in (list.keys()).keys:
  print(key)

list.keys()
   for prediction in list:
       print(prediction['alternative'])
        print(" " + prediction["transcript"] + " (" + str(prediction["confidence"]*100) + "%)")
