import pyttsx3  # pip install pyttsx3
import datetime
import pywhatkit as pywhatkit  # pip install pywhatkit
import speech_recognition as sr  # pip install speechrecognition
import wikipedia  # pip install wikipedia
import webbrowser
import os
import time
import random
import pyautogui  # pip install pyautogui
import requests  # pip install requests

listener = sr.Recognizer()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
with open("voice.txt", "r") as f:
    voice = f.read()
engine.setProperty('voice', voices[int(voice)].id)


def speak(audio):
    with open("voice.txt", "r") as f:
        voice = f.read()
    print("    ")
    print("-------------------")
    print("    ")
    if voice == "1":
        print(f"Friday: {audio}")
    else:
        print(f"Mark: {audio}")
    print("    ")
    print("-------------------")
    print("    ")
    engine.say(audio)
    engine.runAndWait()


def weather():
    # tell weather to user using openweathermap
    api_key = "69e2f2cb7807397cb7f2d5cf6567fd30"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    city_name = "Pezinok"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    # now is complete url for weather like:
    # http://api.openweathermap.org/data/2.5/weather?appid=69e2f2cb7807397cb7f2d5cf6567fd30&q=Pezinok
    response = requests.get(complete_url)
    #     tell the user if the weather is clear, cloudy, rain, snow, sunny or thunderstorm
    x = response.json()
    if x["weather"][0]["main"] == "Clear":
        speak("The weather is clear")
    elif x["weather"][0]["main"] == "Clouds":
        speak("The weather is cloudy")
    elif x["weather"][0]["main"] == "Rain":
        speak("The weather is rainy")
    elif x["weather"][0]["main"] == "Snow":
        speak("The weather is snowy")
    elif x["weather"][0]["main"] == "Thunderstorm":
        speak("The weather is thunderstorm")
    else:
        speak("The weather is not clear")


# speak("Hallo Tom. I am your virtual assistant")

if voice == "1":
    speak("initializing Friday")
else:
    speak("initializing Mark")


def Time():
    ttime = datetime.datetime.now().strftime("%I:%M:%S")
    speak(ttime)


# time()


def date():
    date = int(datetime.datetime.now().year)
    date2 = int(datetime.datetime.now().month)
    date3 = int(datetime.datetime.now().day)
    speak("year: ", date)
    speak("month: ", date2)
    speak("DAY: ", date3)


# date()


def wishMe():
    hour = datetime.datetime.now().hour
    if 6 <= hour < 12:
        speak("good morning boss")
    elif 12 <= hour < 18:
        speak("good afternoon boss")
    elif 18 <= hour < 24:
        speak("good evening boss")
    else:
        speak("good night boss")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source, 0, 3)

    try:
        query = r.recognize_google(audio, language='en-in')  # en-in
        print(f"you: {query}\n")  # User query will be printed.

    except Exception as e:
        return "None"
    return query


def mark():
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            wishMe()
            speak("How was your day look like?")
            while 1:
                query = takeCommand().lower()
                if 'exit' in query.lower() or 'quit' in query.lower() or 'goodbye' in query.lower() or \
                        'sleep' in query.lower():
                    speak("Bye bye. Have a nice day.")
                    break
                elif "good" in query.lower():
                    speak("Good to hear that")
                    speak("what else can I do for you?")
                elif "bad" in query.lower():
                    speak("I am sorry to hear that")
                    speak("what else can I do for you?")
                elif "the worst" in query.lower():
                    speak("I am sorry to hear that")
                    speak("what else can I do for you?")
                else:
                    if "open youtube" in query.lower():
                        webbrowser.open("https://youtube.com")
                        speak("OK. I opened YouTube")
                    elif "wikipedia" in query.lower():
                        speak("searching wikipedia")
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=2)
                        speak("According to wikipedia")
                        speak(results)
                    elif "for nothing" in query.lower():
                        speak("I am sorry. But your rude!")
                    elif "web" in query.lower():
                        webbrowser.open("http://192.168.1.38/")
                        speak("OK. I opened our website")
                    elif "open google" in query.lower():
                        webbrowser.open("http://www.google.com")
                        speak("OK. I opened Google")
                    elif "what's the time" in query.lower():
                        speak("It's:     ")
                        Time()
                    elif "what's the date" in query.lower():
                        speak("The date is: ")
                        date()
                    elif "open stack overflow" in query.lower():
                        webbrowser.open("https://stackoverflow.com")
                        speak("OK. I opened Stack Overflow")
                    elif "open programming app" in query.lower():
                        webbrowser.open("https://github.com")
                        speak("OK. I opened GitHub")
                    elif "how are you" in query.lower():
                        speak("I am fine. Thanks for asking")
                    elif "add new training" in query.lower() or "add training" in query.lower() or "add a new training" in query.lower():
                        query = query.replace("add new training", "")
                        query = ("What is the name of the training?")
                        ttiimmee = takeCommand().lower()
                        with open("training.txt", "a") as f:
                            f.append("\n" + query + " for " + ttiimmee + ",")
                        speak("Training added")
                    elif "clear console" in query.lower():
                        speak("Clearing console")
                        os.system('cls')
                    elif "clear training" in query.lower():
                        speak("Clearing training")
                        with open("training.txt", "w") as f:
                            f.write(",")
                        speak("Training was cleared")
                    elif "search" in query.lower():
                        query = query.replace("search", "")
                        speak("searching " + query)
                        webbrowser.open("https://www.google.com/search?q=" + query)
                    elif "who are you" in query.lower():
                        speak("I am your personal assistant. My name is mark")
                    elif "who made you" in query.lower():
                        speak("I was made by Tom")
                    elif "who is your creator" in query.lower() or "who's your creator" in query.lower():
                        speak("I was made by Tom")
                    elif "open whatsapp" in query.lower():
                        webbrowser.open("https://web.whatsapp.com")
                        speak("OK. I opened Whatsapp")
                    elif "play" in query.lower():
                        song = query.replace("play", "")
                        pywhatkit.playonyt(song)
                        speak("playing " + song)
                        pyautogui.press('f5')
                        time.sleep(8)
                        pyautogui.press('t')
                        pyautogui.press('f')
                    elif "window to left" in query.lower():
                        speak("The window is switched to left")
                        pyautogui.hotkey('winleft', 'left')
                    elif "window to right" in query.lower():
                        speak("The window is switched to right")
                        pyautogui.hotkey('winleft', 'right')
                    elif "window to up" in query.lower():
                        speak("The window is switched to up")
                        pyautogui.hotkey('winleft', 'up')
                    elif "window to down" in query.lower():
                        speak("The window is switched to down")
                        pyautogui.hotkey('winleft', 'down')
                    elif "close window" in query.lower():
                        speak("Closing window")
                        pyautogui.hotkey('altleft', 'f4')
                    elif "close this window" in query.lower():
                        speak("Closing window")
                        pyautogui.hotkey("altleft", 'f4')
                    elif "window" in query.lower():
                        speak("Switching window")
                        pyautogui.hotkey('altleft', 'tab')
                    elif "tab" in query.lower():
                        speak("Switching tab")
                        pyautogui.hotkey('ctrlleft', 'tab')
                    elif "minimize" in query.lower():
                        speak("Minimizing window")
                        pyautogui.hotkey('winleft', 'm')
                    elif "maximize" in query.lower():
                        speak("Maximizing window")
                        pyautogui.hotkey('winleft', 'up')
                    elif "close this" in query.lower():
                        speak("Closing tab")
                        pyautogui.hotkey('ctrlleft', 'w')
                    elif "open wikipedia" in query.lower():
                        webbrowser.open("https://wikipedia.org")
                        speak("OK. I opened Wikipedia")
                    elif "open programming studio" in query.lower():
                        os.startfile(
                            "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\"
                            "PyCharm Community Edition 2022.1.lnk")
                        speak("OK. I opened your Programming Studio named PyCharm")
                    elif "how" in query.lower() and "day" in query.lower() and "you" in query.lower():
                        speak("My day was good")
                    elif "search" in query.lower():
                        speak("What do you want to search?")
                        search = takeCommand().lower()
                        a = "Here is what I found for " + search
                        webbrowser.open("https://www.google.com/search?q=" + search)
                        speak(a)
                    elif "what's your version" in query.lower() or "what is your version" in query.lower():
                        speak("I am version A.2")
                        print("(A.1 now does not exist)")
                    elif "what is your name" in query.lower() or "what's your name" in query.lower():
                        if voice == 0:
                            speak("My name is Mark")
                        else:
                            speak("My name is Friday")
                    elif "how old are you" in query.lower():
                        speak("I am 3 months old")
                    elif query == "mark" or query == "friday":
                        speak("Yes?")
                    elif "say hello" in query.lower():
                        speak("Hello.")
                        with open("voice.txt", "r") as f:
                            voice = int(f.read())
                        if voice == 0:
                            speak("I am Mark")
                        else:
                            speak("I am Friday")
                    elif "change to friday" in query.lower():
                        speak("I am changing to Friday")
                        with open("voice.txt", "w") as f:
                            f.write("1")
                        with open("voice.txt", "r") as f:
                            voice = int(f.read())
                        engine.setProperty('voice', voices[voice].id)
                    elif "change to mark" in query.lower() or "change to marc" in query.lower():
                        speak("I am changing to Mark")
                        with open("voice.txt", "w") as f:
                            f.write("0")
                        with open("voice.txt", "r") as f:
                            voice = int(f.read())
                        engine.setProperty('voice', voices[voice].id)
                    elif "weather" in query.lower():
                        weather()
                    elif "tell" in query.lower() and "about you" in query.lower():
                        speak("Let me introduce myself")
                        speak("I am a computer program!")
                        speak("I was made by Tom")
                        speak("I was created on December 2021")
                        speak("I am version A.2")
                        speak("if you want to know what can I do for you, say 'what can you do?!'")
                    elif "intro" in query.lower():
                        os.startfile("C:\\Users\\Mark\\Desktop\\Intro.mp4")
                        speak("Hello, I am Friday. Your personal assistant. I am here to help you.")
                        speak("I can open websites, search for information, play music, pause music, and play videos.")
                        speak("I can also change my voice to Mark or Friday.")
                        speak("If you want to know more about me, just ask 'tell me about yourself'.")
                    elif "thank" in query.lower():
                        speak(random.choice(
                            ["You're welcome", "No problem", "My pleasure", "It was my pleasure to help you"]))
                    elif "what can you do" in query.lower():
                        speak("I can search Wikipedia, open YouTube, play music, open Google, open Stack Overflow, "
                              "open GitHub(programming app), open Whatsapp, tell you time, tell you date, control your "
                              "video. And that's it!")
                    else:
                        pass
        elif "bye" in query.lower():
            break
        else:
            pass


# wishMe()
# query = takeCommand()

if __name__ == "__main__":
    speak("Initializing is Done!")
    mark()
