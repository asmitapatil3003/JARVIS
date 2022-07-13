import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
       engine.say(audio)
       engine.runAndWait()

def greeting():
       hour=int(datetime.datetime.now().hour)
       if hour>=0 and hour<12:
              speak("Good Morning!")
       elif hour>=12 and hour<18:
              speak("Good Afternoon!")
       else:
              speak("Good Evening!")

       speak("I am Jarvis Mam. Please tell me how may I help you")

def takeCommand():
         r=sr.Recognizer()
         with sr.Microphone() as source:
             print("Listening....")
             r.pause_threshold=1
             audio=r.listen(source)
         try:
             print("Recognizing...")
             query= r.recognize_google(audio,language='en-in')
             print(f"User Said: {query}\n")

         except Exception as e:
             print("say that again please..")
             return "None"
         return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('asmitap3003@gmail.com', '@Ap302002')
    server.sendmail('asmitap3003@gmail.com', to, content)
    server.close()

if __name__=="__main__" :
       greeting()

       while True:
              query=takeCommand().lower()

              if 'wikipedia' in query:
                  speak("searching Wikipedia")
                  query=query.replace("wikipedia","")
                  results=wikipedia.summary(query,sentences=2)
                  speak("According to wikipedia")
                  print(results)
                  speak(results)

              elif 'open youtube' in query:
                  webbrowser.open("youtube.com")

              elif 'open google' in query:
                  webbrowser.open("google.com")

              elif 'play music' in query:
                   music_dir='C:\\Users\\shree\\Music\\favorite song'
                   songs=os.listdir(music_dir)
                   print(songs)
                   os.startfile(os.path.join(music_dir,songs[0]))

              elif 'the time' in query:
                  strTime = datetime.datetime.now().strftime("%H:%M:%S")
                  print(f"Mam, the time is {strTime}")
                  speak(f"Mam, the time is {strTime}")


              elif 'open code' in query:
                  codePath = "C:\\Users\\shree\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"

                  os.startfile(codePath)

              elif 'email to asmita' in query:
                  try:
                      speak("What should I say?")
                      content = takeCommand()
                      to = "asmitap3003gmail.com"
                      sendEmail(to, content)
                      speak("Email has been sent!")

                  except Exception as e:
                      print(e)
                      speak("Sorry my friend asmita . I am not able to send this email")


       

