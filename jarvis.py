import sys
import pyttsx3 # python text to speech module (pip install)
import datetime #date time module import (built in)
import speech_recognition as sr #(pip install)
import wikipedia # (pip install)
import webbrowser #(built in)
import os #opens windows directories (built in)
import random #(built in)
import smtplib #(built in)
import sys
import pyjokes #(pip install)

mail_list = {"recipent1":"recipent1's email", "recipent2":"recipent2's email"}

engine = pyttsx3.init("sapi5") #sapi5 is like an API... windows' voice
voices = engine.getProperty("voices") #List of pyttsx.voice.Voice descriptor objects
#print(voices[0].id)
engine.setProperty('voice',voices[0].id) #0 is male and 1 is female



def speak(audio):
    engine.say(audio) 
    engine.runAndWait() 

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir!")
    
    speak("Jarvis at your service. How may I help you?")

def TakeCommand():    
    #it takes input from mic and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.energy_threshold=1000
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= "en-in")
        print (f"User said: {query}\n")
    except Exception as e:
        #print(e) #comment out if u don't want to see the error
        print("say that again pls")
        return "None"
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com",587) #587 is the modern port for secure SMTP
    server.ehlo()
    server.starttls()
    server.login("YOUR-EMAIL-ID","YOUR-EMAIL-PASSWORD")
    server.sendmail("YOUR-EMAIL-ID",to,content)
    server.close()

 
if __name__=="__main__": #this will run only when this file is running.
    wishMe()
    while True:
        query = TakeCommand().lower()
        #logic for executing tasks
        if "wikipedia" in query:
            speak("Searching wikipedia, sir")
            query = query.replace("wikipedia","")
            #print(query)
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        
        elif "open youtube" in query:
            speak("Opening youtube, sir.")
            webbrowser.open("https://www.youtube.com",new=2)
        
        elif "open google" in query:
            speak("Opening google, sir.")
            webbrowser.open_new_tab("https://www.google.co.in")
        
        elif "open amazon" in query:
            speak("Sure! Happy Shopping!")
            webbrowser.open_new_tab("https://www.amazon.in")

        elif "photos" in query:
            pic_dir = r"\gallery" #give the path to the picture folder
            pictures = os.listdir(pic_dir)
            speak("Showing photos, sir.")
            os.startfile(os.path.join(pic_dir,pictures[random.randint(1,25)])) #the randint parameters depend on the number of photos in directory
        
        elif "the time" in query:
            t = datetime.datetime.now().strftime("%H:%M:%S")
            print(t)
            speak (f"Sir, the time right now is {t}.")
        
        elif "visual studio" in query:
            codepath="C:\\Microsoft VS Code\\Code.exe"
            speak("Good luck with coding sir!")
            os.startfile(codepath)

        elif "music" in query:
            speak("enjoy sir!")
            webbrowser.open_new_tab("https://open.spotify.com")
        
        elif "zoom" in query or "meeting" in query or "video call" in query:
            zoompath="C:\\Users\\Zoom\\bin\\Zoom.exe"
            speak("Starting zoom meetings")
            os.startfile(zoompath)
        
        elif "joke" in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif "remind me" in query:      
            query=query.replace("remind me to","")
            print("writing sir")
            speak("writing sir")
            
            with open("C:\\Desktop\\Reminder.txt","w") as f:
                f.write(query)
                f.write("\n")
            

        elif "send mail" in query:
            pass
            #WRITE THE CODE FOR SENDING AN EMAIL TO THE ADDRESSES GIVEN IN MAIL_LIST DICTIONARY

        elif "quit" in query or "exit" in query or "stop" in query or "shut up" in query or "goodbye" in query:
            speak("Goodbye sir! See you soon.")
            sys.exit()
        
        else:
            speak("Sorry. I don't know that command. Please tell the developer to add this command.")


            
