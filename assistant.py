import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            cmd = listener.recognize_google(voice)
            cmd = cmd.lower()
            if 'bonzibuddy' in cmd:
                cmd = cmd.replace('bonzibuddy', '')
                print(cmd)
    except NameError:
        print("An exception occurred")
    return cmd


def run_alexa():
    command = take_command()
    try:
        if command == "bonzibuddy":
            talk("Sorry, I didn't get that")
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'loco' in command:
            talk('Fuck you too')
        #TODO: Check what is happening here...
        # elif 'who the heck is' in command:
        #     person = command.replace('who the heck is', '')
        #     info = wikipedia.summary(person, 1)
        #     talk(info)
        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'are you single' in command:
            talk("What do u want lol")
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
    except NameError:
        talk("Can you repeat that please?")

while True:      
    run_alexa()