import datetime
import json
import webbrowser
from time import sleep
import pyautogui
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import chatGPT
from Apps import codeCompletion

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

wake_word = "test"


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
                cmd = cmd.replace(wake_word, '')
                print(cmd)
    except NameError:
        print("An exception occurred")
    return cmd


def run_alexa():
    command = take_command()
    try:
        # Said Only Wake word
        if command == wake_word:
            talk("Sorry, I didn't get that")

        # Will open YouTube with a random video from the channel
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'code' in command:
            talk("What type of code is it?")
            extension = get_response()
            talk("What would you like programmed?")
            prompt = get_response()
            codeCompletion.new_file(extension, prompt)
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
            with open('contact.json') as f:
                data = json.load(f)
            try:
                webbrowser.open(data['Contacts'][cmd]['link'])
            except NameError:
                talk("An Error Occurred.")
                return
            sleep(4)
            pyautogui.click(590, 1000)
            talk("What would you like to say?")
            try:
                response = get_response()
                pyautogui.write(response)
            except sr.UnknownValueError:
                talk("An error occurred. ")
                return

            sleep(1)
            pyautogui.press('enter')

        # Will tell a joke
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            talk(joke)
            talk("Did you enjoy the joke?")

        # Will write a paper based on your parameters and store/open the file when done
        elif 'write a paper' in command:
            chatGPT.write_paper(command)

        # Did not understand
        else:
            talk("Sorry I did not understand that.")
            return
    except NameError:
        talk("Can you repeat that please?")


while True:
    run_alexa()
