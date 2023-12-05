import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak: ")
    r.adjust_for_ambient_noise(source, duration=1) # Ajuster le niveau du bruit ambiant
    audio = r.listen(source, timeout= 5) # Enregistrez l'audio jusqu'à 5 secondes ou jusqu'à ce qu'il y ait un silence

    try:
        text = r.recognize_google(audio)
        print("You said this : {}".format(text))
    except:
        print("Sorry could not recognize your voice try again")