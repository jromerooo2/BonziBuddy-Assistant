import random
import openai
import os
import pyautogui
from time import sleep

# OpenAI Initialization
openai.organization = "org-vxtFFnnBThf1eKODPmnmi6R3"
openai.api_key = "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"

def summarize(prompt):
    chatResponse = openai.Completion.create(
        model="text-davinci-003",
        prompt="Summarize this text: " + prompt,
        temperature=0.5,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    return chatResponse['choices'][0]['text']
def new_file(extension, prompt):
    if extension == 'javascript':
        file_type = 'js'
    elif extension == 'python':
        file_type = 'py'
    else:
        return "No Type Selected"
    app_path = "Code.exe.lnk "

    osCommandString = "start " + app_path
    os.system(osCommandString)
    sleep(5)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'n')
    keywords = openai.Completion.create(
        model="text-davinci-003",
        prompt="Extract keywords from this text:\n\n " + prompt,
        temperature=0.5,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.8,
        presence_penalty=0.0
    )
    keyword_response = keywords['choices'][0]['text']
    file_name = keyword_response[0]
    sleep(10)
    chatResponse = openai.Completion.create(
        model="text-davinci-003",
        prompt=extension + ":  " + prompt,
        temperature=0.5,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    response = chatResponse['choices'][0]['text']
    sleep(7)
    pyautogui.write(response)
    pyautogui.hotkey('ctrl', 's')
    sleep(1)
    pyautogui.write(keywords[0])

