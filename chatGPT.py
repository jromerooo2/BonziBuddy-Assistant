import random
import openai
import os

# OpenAI Initialization
openai.organization = "org-vxtFFnnBThf1eKODPmnmi6R3"
openai.api_key = "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"


def new_chat(prompt):
    chatResponse = openai.Completion.create(
        model="text-davinci-003",
        prompt="\nHuman: " + prompt + "\nAI:",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    return chatResponse['choices'][0]['text']


def write_paper(prompt):
    chatResponse = openai.Completion.create(
        model="text-davinci-003",
        prompt="\nHuman: " + prompt + "\nAI:",
        temperature=0.9,
        max_tokens=5000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    number = random.randrange(1, 100)
    file_name = "paper" + str(number)
    file_path = "./Papers/" + file_name + ".txt"
    f = open("./Papers/" + file_name + ".txt", "w+")
    f.write(chatResponse['choices'][0]['text'])
    f.close()
    osCommandString = "notepad.exe " + file_path + ""
    os.system(osCommandString)


def summarize(prompt):
    chatResponse = openai.Completion.create(
        model="text-davinci-003",
        prompt="Summarize this text:\n\n " + prompt,
        temperature=0.5,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
    )
    return chatResponse['choices'][0]['text']
