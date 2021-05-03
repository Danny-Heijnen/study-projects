import pyttsx3


engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', 'english-us')

engine.say("Take a deep breath in.")
engine.say("Feel your breath.")


engine.runAndWait()
