import speech_recognition as sr
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os

r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if(ask):
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            speak('Sizi anlayamadım.')
        except sr.RequestError:
            speak('Sistem çalışmıyor.')   
        return voice
    

def response(voice):
    if 'merhaba' in voice:
        speak('merhaba hos geldiniz!')
    if 'nasılsın' in voice:
        speak('iyiyim siz nasılsınız?')
    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))
    if 'arama yap' in voice:
        search = record('ne aramak istiyorsunuz?')
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        speak(search + ' için bulduklarım:')
    if 'tamamdır' in voice:
        speak('Görüşürüz.')
        exit()


def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

speak('Size nasıl yardımcı olabilirim?')
time.sleep(1)
while 1:
    voice = record()
    print(voice)
    response(voice)






