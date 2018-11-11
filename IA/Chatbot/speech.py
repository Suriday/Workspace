#pip install SpeechRecognition
#pip install pyaudio
import speech_recognition as sr
#Obtenemos el audio del microfono
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=0.3)
    print('Habla')
    audio = recognizer.listen(source)


print(recognizer.recognize_google(audio, language="es"))