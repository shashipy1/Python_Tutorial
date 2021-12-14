import requests
import json
def speak(str):
    from win32com.client import  Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.speak(str)

if __name__ == '__main__':
    speak("News for today")
    url = "https://newsapi.org/v2/everything?q=tesla&from=2021-08-27&sortBy=publishedAt&apiKey=7fccebec63934933b08d865fb04d8b74"
    news = requests.get(url).text
    news = json.loads(news)
    print(news["status"])