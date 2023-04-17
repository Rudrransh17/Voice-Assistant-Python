# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()
voice_id = 1     # 0 - Male		1 - Female

# Function to convert text to
# speech
def Speak(command):
    
    # Initialize the engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)
    engine.say("Did you say" + command)
    engine.runAndWait()
    
    

def Listen():
     
    # Making the use of Recognizer and Microphone
    # Method from Speech Recognition for taking
    # commands
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
        print('Listening')
         
        # seconds of non-speaking audio before
        # a phrase is considered complete
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing")
             
            # for listening the command in indian english
            command = r.recognize_google(audio, language='en-in')
             
            # for printing the query or the command that we give
            print("the query is printed= '", command, "'")
        except Exception as e:
             
            # this method is for handling the exception
            # and so that assistant can ask for telling
            # again the command
            print(e) 
            Speak("Say that again sir")
            Listen()
         
    return command


# command = Listen()
# Speak(command)


## Below is loop to keep listening continously--> 

while(1):
    print('loop')
    
    # Exception handling to handle
    # exceptions at the runtime
    try:
        
        # use the microphone as source for input.
        with sr.Microphone() as source2:
            
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
            
            #listens for the user's input
            audio2 = r.listen(source2)
            
            # Using google to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            print("Did you say ",MyText)
            Speak(MyText)
            
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        
    except sr.UnknownValueError:
        print("unknown error occurred")
    continue
