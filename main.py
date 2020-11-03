# VIRTUAL ASSISTANT
# Diego Dos Santos <diegodossantos.es@gmail.com>

import speech_recognition as sr #recognition of what we are speaking
import pyaudio #part of the listen recognition
import time #exactly time 
from time import ctime #exactly time
import webbrowser #open new windows with a command 
import pygame #execute the sound 
import random #give a random register number of the file 
import os #use to remove the register number
from gtts import gTTS #transform the text speak in an audio file clear

r = sr.Recognizer()

# RECORD, MICROOFONE, ERRORS and PART OF THE LISTEN AUDIO CONFIGURATION

def record_audio(ask = False):  
    with sr.Microphone() as source:
        if ask:
            viky_speak(ask)
        audio = r.listen(source)
        voice_data: ''
    try:
        voice_data = r.recognize_google(audio)

    except sr.UnknownValueError:
        viky_speak ("Sorry! I don't know what do you want")
    except sr.RequestError:
        viky_speak ('Oh gooood, conection failed')
    return voice_data

# VOICE and TRANFORM TEXT IN A AUDIO FILE 

def viky_speak(audio_string):
    tts = gTTS(text=audio_string, lang="en")
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue
    print(audio_string)
    os.remove(audio_file)

# COMMON QUESTIONS and COMMANDS

def respond(voice_data):
    if "what's your name" in voice_data:
        viky_speak ('My name is Viky')

    if 'what time is it' in voice_data:
        viky_speak (ctime())

    if 'search' in voice_data:
        busqueda = record_audio('what do you want to search for?')
        url = 'https://google.com/search?q=' + busqueda
        webbrowser.get().open(url)
        viky_speak ('Here is what I found for' + busqueda)

    if 'find location' in voice_data:
        location = record_audio('Where?')
        url = 'https://google.com/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        viky_speak ('here is the location' + location)

    if 'exit' in voice_data:
        exit()

# BUCLE TO HOLD and WAIT THE COMMANDS 

time.sleep(1)
viky_speak ('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)