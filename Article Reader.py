from importlib.util import spec_from_file_location
import requests
import pyttsx3
from bs4 import BeautifulSoup

#example https://medium.com/pythoneers/python-script-that-reads-articles-on-your-behalf-70591fa9ed16
url = str(input('Paste article url \n'))

def content(url):
    res =requests.get(url)
    soup =BeautifulSoup(res.text , 'html.parser')
    articles = []

    for i in range(len(soup.select('.p'))):
        article = soup.select('.p')[i].getText().strip()
        articles.append(article)
        contents = " ".join(articles)

    return contents



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



contents = content(url)
print(contents)
speak(contents)