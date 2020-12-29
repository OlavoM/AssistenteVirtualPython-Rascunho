import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as s:
    r.adjust_for_ambient_noise(s)
    
    while True:
        try:
            audio = r.listen(s)
            speech = r.recognize_google(audio, language='pt')
            print (f"Você disse: {speech}")
            if speech == "desligar":
                break
        except Exception: #contornando bug de quando ficava silêncio
            continue
