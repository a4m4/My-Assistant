import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib

    def my_function():
        print("Hello from a function")        

    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak Anything")
            audio = r.listen(source)
            print("Done")
            try: 
                text = r.recognize_google(audio)
                print('You Said : {}'.format(text))            
            except:
                print('Sorry, i didnot understand Boss!')
            return text
        
    
    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('anyemail@gmail.com', 'password?')
        server.sendmail('salimehdi144@gmail.com', to, content)
        server.close()
        

    
        query = takeCommand().lower()
        if 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(f"Sir, the time is {strTime}")
            
        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            
               
        elif 'email please' in query:
            try:
                print("What should I say?")
                content = takeCommand()
                to = "anyemail@gmail.com"    
                sendEmail(to, content)
                print("Email has been sent!")
            except Exception as e:
                print(e)
                print("Sorry Boss. I am not able to send this email") 

