import speech_recognition as sr
#importando módulos que eu não consegui baixar no raspberry mas que podem ser substituídos
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot = ChatBot("Assistente", read_only=True)

"""bot.set_trainer(ListTrainer) #definir treinamento

for _file in os.listdir("chats"): #percorrer todos os arquivos em chats
    lines = open("chats/" + _file, "r").readlines()
    bot.train(lines)"""


r = sr.Recognizer()

with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)
    
    while True:
        try:
            audio = r.listen(s)
            speech = r.recognize_google(audio, language='pt')
            print(f"Você disse: {speech}")
            print(f"Bot: {bot.get_response(speech)}")
        except Exception: #contornando bug de quando ficava silêncio
            continue
