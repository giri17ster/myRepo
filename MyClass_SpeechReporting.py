from gtts import gTTS
from pygame import mixer
import time

def speechReporting(text_value):
    text2speech = gTTS(text=text_value, lang='jp')
    text2speech.save("report.mp3")
    mixer.init()
    mixer.music.load("report.mp3")
    mixer.music.play()
    time.sleep(5)
    mixer.music.stop()
    mixer.quit()

speechReporting("Globant is an IT and Software Development company operating in Argentina, Colombia, Uruguay, the United Kingdom, Brazil, the United States, Peru, India, Mexico, Chile, Spain, Romania and Belarus. It was formed in 2003 by Martín Migoya, Guibert Englebienne, Martín Umaran and Néstor Nocetti.")