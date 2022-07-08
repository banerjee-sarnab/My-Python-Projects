import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
import subprocess as sp
import pywhatkit as kit
from email import message
# from decouple import config
# import requests

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# engine.setProperty('voices', voices[1].id)

# Set Rate
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 1.0)

# Set Voice (Female)
engine.setProperty('voices', voices[1].id)

def speak(audio) :
    engine.say(audio)
    engine.runAndWait()

def wish_me() :
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour < 12):
        speak("Good Morning Sir !")
    elif(hour >=12 and hour < 17) :
        speak("Good Afternoon Sir !")
    else :
        speak("Good Evening Sir !")
    speak("Iam Jarvis, your all time desktop Assistant ! Please tell me your concern.")

def take_command():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening.....")
        r.pause_threshold = 1
        # r.energy_threshold = 400
        audio = r.listen(source)

    try :
        print("Recognizing.....")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"User said : {query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please.....")
        return "None"
    
    return query

def send_email(to, content) :
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('my_mail@gmail.com','password')
    server.sendmail('my_mail@gmail.com',to,content)
    server.close()
# OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")
# def get_weather_report(city):
#     res = requests.get(
#         f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
#     weather = res["weather"][0]["main"]
#     temperature = res["main"]["temp"]
#     feels_like = res["main"]["feels_like"]
#     return weather, f"{temperature}℃", f"{feels_like}℃"
if __name__ == "__main__" :
    paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
    }
    # speak("Hello, Good Afternoon")
    
    wish_me()
    
    while True :
        query = take_command().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query :
            speak('Searching Wikipedia.....')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query :
            webbrowser.open('youtube.com')

        elif 'open google' in query :
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query :
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query :
            try :
                music_dir = 'D:\\My Music'
                songs = os.listdir(music_dir)
                random_song = random.randint(0, len(songs)-1)
                # print(songs)
                os.startfile(os.path.join(music_dir,songs[random_song]))
            except :
                speak("Sorry Sir! Can't play music.")

        elif 'the time' in query :
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query :
            code_path = "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(code_path)

        # elif 'open notepad' in query :
        #     os.startfile(paths['notepad'])

        elif 'send an email to' in query :
            try :
                speak('What Should I say')
                content = take_command()
                to = "sender@gmail.com"
                send_email(to,content)
                speak("Email has been sent")
            except Exception as e :
                # print(e)
                speak("Sorry sir! I am not able to send this email")

        elif 'open camera' in query :
            try :
                sp.run('start microsoft.windows.camera:', shell=True)
            except Exception as e :
                speak("Sorry Sir! Can't open Camera!!")

        elif 'open command prompt' in query :
            os.system('start cmd')

        elif 'google' in query :
            query = query.replace('google','')
            kit.search(query)
        
        elif 'youtube' in query :
            query = query.replace('google','')
            kit.playonyt(query)
        
        elif 'open calculator' in query :
            sp.Popen(paths['calculator'])

        elif 'whatsapp' in query :
            try :
                number = 'your number'
                speak('What should I Write')
                messages = take_command().lower()
                kit.sendwhatmsg_instantly(f"+91{number}", messages)
                speak('I have sent the message sir!!')
            except Exception as e :
                speak("Sorry Sir! Can't send message")

        elif 'quit' in query :
            speak('Thanks for your time Sir! Hope to meet you again!!')
            exit()