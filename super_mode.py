##########################################################################################################################################################################
#created by    : Naveen
#last modified :31/12/19
##########################################################################################################################################################################

import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import smtplib
import requests
from pprint import pprint
from selenium import webdriver
import cv2
from win10toast import ToastNotifier
import chrome
import camera
import gui
import translate
import mouse
import img_to_text
import sys
import face_id
from SVR.Versions import svr  
#############################################################################################################################################################################
def sup():
    toaster = ToastNotifier()
    toaster.show_toast("Tina notification..",
    "Super mode Started!!!",
    icon_path=None,
    duration=5)

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()


    def wishMe():
        speak("Welcome back sir")
        hour = int(datetime.datetime.now().hour)

        #speak("tina at your Service. Please tell me how can I help You ")

    def takeCommand():

        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 0.5
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print("Naveen Said:{}\n".format(query))

        except Exception as e:
            print(e)
            print("Say that again Please...")
            speak("Say that again Please...")
            return "None"
        return query


    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('email_id', 'pass')
        server.sendmail('email_id', to, content)
        server.close()


        


                

    if __name__ == "__main__":
        
        wishMe()
        while True:
            query = takeCommand().lower()


            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'search in chrome' in query:
                speak("what should i search?")
                chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'#Add the Location of the chrome browser

                r = sr.Recognizer()

                with sr.Microphone() as source:
                    print('say something!')
                    audio = r.listen(source)
                    print("done")
                try:
                    text = r.recognize_google(audio)
                    print('google think you said:\n' +text +'.com')
                    wb.get(chrome_path).open(text+'.com')
                except Exception as e:
                    print(e)
            
            elif 'how is the weather' and 'weather' in query:

                url = 'https://api.openweathermap.org/'#Open api link here

                res = requests.get(url)

                data = res.json()

                weather = data['weather'] [0] ['main'] 
                temp = data['main']['temp']
                wind_speed = data['wind']['speed']

                latitude = data['coord']['lat']
                longitude = data['coord']['lon']

                description = data['weather'][0]['description']
                speak('Temperature : {} degree celcius'.format(temp))
                print('Wind Speed : {} m/s'.format(wind_speed))
                print('Latitude : {}'.format(latitude))
                print('Longitude : {}'.format(longitude))
                print('Description : {}'.format(description))
                print('weather is: {} '.format(weather))
                speak('weather is : {} '.format(weather))


            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%I:%M:%S")    
                speak("Sir, the time is {strTime}")
            
            elif 'the date' in query:
                year = int(datetime.datetime.now().year)
                month = int(datetime.datetime.now().month)
                date = int(datetime.datetime.now().day)
                speak("the current Date is")
                speak(date)
                speak(month)
                speak(year)


            elif 'email to ****' and 'send bug report' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "to_email_id"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend . I am not able to send this email")      

            elif 'open code' in query:
                codePath = "C:\\Users\\ELCOT\\Desktop\\ai.py"#ADD THE PATH OF THE PROGEM HERE
                os.startfile(codePath)


            elif 'open' in query:
                os.system('explorer C://{}'.format(query.replace('Open','')))

            
            elif 'image to text' in query:
                try:
                    exec(img_to_text.ta())
                    speak("ok sir opening scan the image")
                except:
                    a=bin(1)
                
            elif 'translate' in query:
                try:
                    speak("ok sir enter word")
                    ss=input("enter word")
                    xx=exec(translate.trans(ss))
                    print(xx)
                except:
                    a=bin(1)
                    
            elif 'mouce' in query:
                try:
                    exec(mouce.m())
                    speak("ok sir please be patient while controling")
                except:
                    a=bin(1)

            

            elif 'send file' in query:
                try:
                    exec(gui.g())
                    speak("please scan the qr code")
                except:
                    a=bin(1)
                

            elif 'shut up' in query:
                speak("ok sir closing..")
                exit()
            elif 'version' in query:
                a=1
            elif 'play game' in query:
                try:
                    exec(dino.ga())
                    speak("play a game")
                except:
                    a=bin(1)
            elif 'camera' and 'take a snap' in query:
                try:
                    exec(camera.cam())
                    speak("ok sir opening")
                except:
                    a=bin(1)
            elif 'tell about developer' in query:
               
                f=open(r"C:\Users\ELCOT\Desktop\New folder\team\developers.txt","r")
                speak(f.read())
                
