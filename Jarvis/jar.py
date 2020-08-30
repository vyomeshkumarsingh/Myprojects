import pyttsx3
import speech_recognition as sr
import wikipedia
import datetime
import webbrowser
import os
# import smtplib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hi!,I am Jarvis , how may i help you")

def TakeCommand():
    # it takes microphone input from the user and return a string

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"Used said:{query}\n")

    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query

# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('youremail@gmail.com', 'your-password')
#     server.sendmail('youremail@gmail.com', to, content)
#     server.close()

if __name__ == "__main__":
    # speak("vyomesh is very dedicated")
    wishMe()
    while True:
        query = TakeCommand().lower()

        # logic to perform tasks based on query
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences =2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open whatsapp web" in query:
            webbrowser.open("whatsapp web.com")
        elif "play music" in query:
            music_dir = "C:\\Users\\VYOMESH\\OneDrive\\Pictures\\Gallary\\audio"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Hi! G, the time is {strTime}")

        elif "open java ide" in query:
            javapath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\IntelliJ IDEA Community Edition 2019.2.3.lnk"
            os.startfile(javapath)

        # elif 'email to harry' in query:
        #     try:
        #         speak("What should I say?")
        #         content = TakeCommand()
        #         to = "harryyourEmail@gmail.com"    
        #         sendEmail(to, content)
        #         speak("Email has been sent!")
        #     except Exception as e:
        #         print(e)
        #         speak("Sorry my friend harry bhai. I am not able to send this email")    
        elif "quit" in query:
            exit()