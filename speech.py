import pyttsx3
import time
engine=pyttsx3.init()

engine.say("sajan sah is the new iron man")
engine.runAndWait()
time.stop(2)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
