from gtts import gTTS
import os


file = open("notes.doc", "r").read().replace("\n", " ")

language = 'en'
speech = gTTS(text=str(file), lang=language, slow=False)

#save the converted audio in mp3 file

speech.save("notes.mp3")

os.system("start notes.mp3")

