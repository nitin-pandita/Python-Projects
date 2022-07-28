#text to speech converter program
from gtts import gTTS
import os
text = "Hello guys, Welcome to my youtube channel, Today we are going to learn , how to create audio from text file"

language = 'en' # en is for english language

obj = gTTS(text=text,lang=language,slow=False)

#we have used slow = False because our conveted video will have a high speed

obj.save("Sample.mp3")


os.system("Sample.mp3") #to open the file automatically we use 'OS'

