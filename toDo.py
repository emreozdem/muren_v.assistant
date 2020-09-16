import speech_recognition as sr
import urllib.request
import json
from gtts import gTTS
from playsound import playsound
import os
import sys
from random import choice
import requests
from lxml import html
import time
from datetime import datetime

import webbrowser
r=sr.Recognizer()

s_selamlama=["Merhaba","Ne haber","Selam patron","Ooo kimleri görüyorum, bu ne hoş sürpriz","Selam","Merhabalar efendim"]


def response(voice):
   
   if voice in s_selamlama:
      selamlama()
   if "saat kaç" in voice:
      seslendirme(datetime.now().strftime('%H:%M'))  
   if "ara" in voice or "bul" in voice or ("arama" in voice and "yap" in voice):
      webarama()
   if voice in ["izle","video","YouTube"]:
      ytarama()
   if "tamam" in voice or "kapat" in voice or ("güle" in voice and "güle" in voice):
      seslendirme("Hoşçakal")
      exit()

def record():
    with sr.Microphone() as source:
        audio=r.listen(source)
        voice=''
        try:
            voice=r.recognize_google(audio,language='tr-TR')
        except sr.UnknownValueError:
            seslendirme("Anlayamadım,lütfen tekrar edermisiniz")
        except sr.RequestError:
            seslendirme("Şu anda isteğinizi yerine getiremiyoruz")
        return voice


def seslendirme(yazi):
   tts=gTTS(text=yazi,lang='tr')
   tts.save("ses.mp3")
   print(yazi)
   playsound("ses.mp3")
   os.remove("ses.mp3")
   
def selamlama():
   secim=choice(s_selamlama)
   seslendirme(secim)
   secim=None

def webarama():
   seslendirme("Ne aratmak istersiniz?")
   key=record()
   print(key)
   url= 'https://www.google.com/search?q='+key
   webbrowser.get().open(url)

def ytarama():
   seslendirme("Ne aratmak istersiniz?")
   key=record()
   print(key)
   url= 'https://www.youtube.com/results?search_query='+key
   webbrowser.get().open(url)

def calistir():
   os.system("start steam://rungameid/365670")

