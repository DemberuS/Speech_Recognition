import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
with sr.Microphone() as source:
    audio = r.listen(source)
    order = r.recognize_google(audio, language='ru-ru')

print(order)

engine = pyttsx3.init()
engine.say(order)
engine.runAndWait()