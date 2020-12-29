import speech_recognition as sr
#importando módulos que eu não consegui baixar no raspberry mas que podem ser substituídos
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os
import pyttsx3

import logging 
logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)

speaker = pyttsx3.init()
bot = ChatBot("Assistente", read_only=True)

trainer = ListTrainer(bot) #definir treinamento

#é bom colocar o treinador em um arquivo separado
"""for _file in os.listdir("chats"): #percorrer todos os arquivos em chats
    lines = open("chats/" + _file, "r").readlines()
    trainer.train(lines)"""

def speak(text):
    speaker.say(text)
    speaker.runAndWait()

r = sr.Recognizer()
with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)
    
    while True:
        try:
            audio = r.listen(s)
            speech = r.recognize_google(audio, language='pt')
            print(f"Você disse: {speech}")
            response = bot.get_response(speech)
            print(f"Bot: {response}")
            speak(response)
        except Exception: #contornando bug de quando ficava silêncio
            continue
