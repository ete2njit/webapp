from random import choice
import requests


class Chatbot:
    name = ""
    key = ""
    image = ""

    def __init__(
        self,
        name="Yoda-bot",
        key="botkey",
        image="https://images.immediate.co.uk/production/volatile/sites/3/2017/12/yoda-the-empire-strikes-back-28a7558.jpg?quality=90",
    ):
        self.name = name
        self.key = key
        self.image = image

    def about(self):
        return "Go no further, you must. Found Master Yoda, you have."

    def help(self):
        return (
            "Type '!! about' for info about me! Type '!! funtranslate <message>' and I will translate your message. "
            + "Type '!! randcase <message>' and I'll return your message with random capitalization. "
            + "Type '!! funtranslate <message>' and Master Yoda will have a look at your message and rephrase it for you. "
            + "Type '!! joke' and I will tell you a programming joke! We all love those! Right?"
        )

    def randcase(self, sentence):
        return "".join(choice((str.upper, str.lower))(c) for c in sentence)

    def joke(self):
        response = requests.get(
            "https://official-joke-api.appspot.com/jokes/programming/random"
        )
        joke_content = response.json()[0]

        if response:
            return joke_content["setup"] + " " + joke_content["punchline"]
        return "Run out of jokes, Yoda has."

    def translate(self, sentence):
        response = requests.get(
            "https://api.funtranslations.com/translate/yoda.json?text=" + sentence
        )
        translation = response.json()

        if response:
            return translation["contents"]["translated"]
        return "At a loss for words, Master Yoda is."

    def process(self, argument):
        line = argument.strip()[2:].strip()
        arg_list = line.split()
        command = arg_list[0]
        param = " ".join(arg_list[1:])

        if command.lower() == "about":
            return self.about()
        if command.lower() == "help":
            return self.help()
        if command.lower() == "randcase":
            return self.randcase(param)
        if command.lower() == "joke":
            return self.joke()
        if command.lower() == "funtranslate":
            return self.translate(param)

        return (
            "A recognized command, '"
            + command.lower()
            + "' is not. Type !! help for info about recognized commands"
        )

    def isCommand(self, argument):
        if argument.strip()[0] == "!" and argument.strip()[1] == "!":
            return True
        return False
