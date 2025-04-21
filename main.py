#hello this is my simple chatbot with voice record and response using python and geminai ai
# made by me aicha allagui
#
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
from pygame import mixer
from io import BytesIO
import os
import google.generativeai as genai

#lena bech na3mel el configuration ta3 openai bil key
API_KEY=""
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat_session = model.start_chat(history=[])

#la logique 
#awel haja bech  na3mel record lil sout
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:     #lena win bech nasma3 el question
        print("listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')# lena bech netaked eli najem y cpture el sout w ba3thou cbon 
        query = r.recognize_google(audio, language='en-in')
        print(f'user has said {query}')
        respond(query)
    except Exception as e:
        print('Say that again please...', e)

#theni step enou generiw el response
def respond(query): 
    print('Responding...')#len generation du reponse a l'aide du geminai
    response = chat_session.send_message(query)
    speak(response.text)


#speak the response
def speak(text):
    speech = gTTS(text=text, lang='en', slow=False)# lena specifina el langue de reponse w bech y9oulha  et la boucle continue 

    speech.save('captured_voice.mp3')
    playsound('captured_voice.mp3')
    
    os.remove('captured_voice.mp3')
    print(text)
    listen()


query = listen()
