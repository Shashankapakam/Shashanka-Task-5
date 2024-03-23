import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

def init_engine():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice
    return engine

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:", query)
        return query.lower()
    except Exception as e:
        print(e)
        speak("Sorry, I didn't catch that.")
        return None

def process_command(query):
    if 'wikipedia' in query:
        speak("Searching Wikipedia ...")
        query = query.replace("wikipedia", '')
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)
    elif 'are you' in query:
        speak("I am amigo developed by Jaspreet Singh")
    elif any(keyword in query for keyword in ['open youtube', 'open google', 'open github', 'open stackoverflow', 'open spotify', 'open whatsapp']):
        if 'youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")
        elif 'google' in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")
        elif 'github' in query:
            speak("Opening GitHub")
            webbrowser.open("https://github.com")
        elif 'stackoverflow' in query:
            speak("Opening Stack Overflow")
            webbrowser.open("https://stackoverflow.com")
        elif 'spotify' in query:
            speak("Opening Spotify")
            webbrowser.open("https://www.spotify.com")
        elif 'whatsapp' in query:
            speak("Opening WhatsApp")
            whatsapp_path = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(whatsapp_path)
    elif 'play music' in query:
        speak("Playing music on Spotify")
        webbrowser.open("https://www.spotify.com")
    elif any(keyword in query for keyword in ['local disk c', 'local disk d', 'local disk e']):
        disk = query.split()[-1].upper() + ":\\"
        speak(f"Opening local disk {disk}")
        os.startfile(disk)
    elif 'sleep' in query:
        speak("Going to sleep. Goodbye!")
        exit()
    else:
        speak("I'm sorry, I couldn't understand that.")

if __name__ == '__main__':
    engine = init_engine()
    speak("Amigo assistance activated. How can I help you?")
    
    while True:
        query = listen_command()
        if query:
            process_command(query)
