import datetime
import json
from time import sleep

import speech_recognition.exceptions
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import pyttsx3
import pywhatkit
import speech_recognition as sr

from Plugins import chatGPT

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\jonet\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_response():
    try:
        with sr.Microphone() as source:
            print("Listening to your Response")
            voice = listener.listen(source)
            feed = listener.recognize_google(voice)
            feed = feed.lower()
            print(feed)
    except NameError:
        print("An exception occurred")
    return feed


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            if "test" in cmd:
                cmd = cmd.replace("test", '')
                print(cmd)
    except NameError:
        print("An exception occurred")
    return cmd


def run_alexa():
    global message
    command = take_command()
    try:
        # Said Only Wake word
        if command == "test":
            talk("Sorry, I didn't get that")

        # Will open YouTube with a random video from the channel
        elif 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)

        # Will ask ChatGPT for information on thing
        elif 'what is' in command:
            talk(chatGPT.new_chat(command))

        # Will return time
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)

        # Will message someone (Person will need to be in contact.json file to message)
        elif 'message' in command:
            cmd = command.replace('message', '')
            cmd = cmd.strip()
            talk("Messaging " + cmd)
            with open('contact.json') as f:
                data = json.load(f)
            try:
                link = data['Contacts'][cmd]['link']
                sleep(2)
                if link:
                    driver = uc.Chrome(options=options)
                    driver.get(link)
                    pyautogui.press('enter')
                    sleep(5)
                    driver.find_element(By.XPATH, data["inputXPath"]).click()
                    talk("What would you like to say?")
                    message = get_response()
                    talk("You would like me to send " + message)
                    pyautogui.write(message)
                    pyautogui.press('enter')
                else:
                    talk("An Error Occurred.")

            except KeyError:
                talk("An Error Occurred.")
                return
        # Will tell a joke
        elif 'joke' in command:
            chatGPT.getJoke(command)

        # Will write a paper based on your parameters and store/open the file when done
        elif 'write a paper' in command:
            chatGPT.write_paper(command)

        # Did not understand
        else:
            talk("Sorry I did not understand that.")
            return
    except speech_recognition.UnknownValueError:
        talk("Can you repeat that please?")


while True:
    run_alexa()
