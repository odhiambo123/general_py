import os

import requests
from bs4 import BeautifulSoup
import sys

from gtts import gTTS


def readTextFromWeb(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        return text
    except:
        print("Error reading text from web")
        sys.exit(1)

def main():
    url = input("Enter the URL of the webpage to read text from: ")
    text = readTextFromWeb(url)

#convert to speech
    language = 'en'
    speech = gTTS(text=str(text), lang=language, slow=False)
    speech.save("webpage.mp3")
    os.system("open webpage.mp3")

    print("Text from the webpage has been read and saved as a mp3 file")



if __name__ == '__main__':
    main()
