import pyttsx3
from tkinter_form import *

class Speach:

    def __init__(self, text, gender):
        self.text = text
        self.gender = gender
        self.engine = pyttsx3.init()
        self.engine.setProperty('volume', 1)
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[self.gender].id)  # Ovozni jinsiga qarab belgilash
        self.engine.setProperty('rate', 120)

    def speak(self):
        self.engine.say(self.text)  # Matn ovozga aylantiriladi
        self.engine.runAndWait()  # Ovozni ijro etish
        self.engine.stop()


if __name__ == "__main__":
    TTS_GUI()
