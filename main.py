import time  # For adding delay
# Speech recognition package from google api
import speech_recognition as sr
# Text to speech package
import pyttsx3
# Import Selenium webdriver
from selenium import webdriver
# Import by method to access elements
from selenium.webdriver.common.by import By
# Import os to open applications
import os
# Impport of wolfram package
import wolframalpha
# Import action chains in selenium to perform actions
from selenium.webdriver.common.action_chains import ActionChains
# Import keys for pressing keyboard keys using selenium
from selenium.webdriver.common.keys import Keys
# for async
import asyncio

# Initialise voice recogniser
r = sr.Recognizer()

# Select voice of assistant
voice_id = 1     # 0 - Male		1 - Female

# API id of wolfram
wolfram_id = '8JTTHT-6TQT8344LG'

# Function to convert text to speech
def Speak(command):
    print("Assistant: ", command)
    # Initialize the engine
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice_id].id)
    engine.say(command)
    engine.runAndWait()

# Function to convert speech to text
def Listen():

    # Making the use of Recognizer and Microphone
    # Method from Speech Recognition for taking
    # commands
    
    print("Say")
    with sr.Microphone() as source:

        # seconds of non-speaking audio before
        # a phrase is considered complete
        #r.pause_threshold = 0.7
        
        try:
            audio = r.listen(source)
            # for listening the command in indian english
            command = r.recognize_google(audio, language='en-in')

            # for printing the query or the command that we give
            print("You: ", command)
            return command
        except Exception as e:

            # this method is for handling the exception
            # and so that assistant can ask for telling
            # again the command
            print(e)
            return Listen()

# Function to search the input on google
def SearchGoogle(input):
    query = input.split(' ', 1)[1]
    browser = webdriver.Chrome()  # Opens chrome browser
    browser.maximize_window()
    # Goes to following URL
    browser.get('http://www.google.com/')
    # Create the search box object
    search_box = browser.find_element("name", "q")
    # Type what to search as key
    search_box.send_keys(query)
    # Submit the search
    search_box.submit()
    time.sleep(10)
    browser.quit()
    return

# Function to play the video on youtube
def PlayYoutube(input):
    query = input.split(' ', 1)[1]
    browser = webdriver.Chrome()  # Opens chrome browser
    #browser.maximize_window()
    # Goes to following URL
    browser.get('http://www.youtube.com/')
    # Create the search box object
    search_box = browser.find_element("name", "search_query")
    # Type what to search as key
    search_box.send_keys(query)
    # Submit the search
    search_box.submit()
    time.sleep(5)
    # Find song element
    xpath = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string"
    card = browser.find_element(By.XPATH, xpath)
    card.click()
    time.sleep(5)
    next_xpath = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[31]/div[2]/div[1]/a[2]"
    pause_xpath = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div[2]/div/div/ytd-player/div/div/div[35]/div[2]/div[1]/button/svg/path"
    actions = ActionChains(browser)
    while(1):
        actions.reset_actions()
        print("-----Inside youtube while loop-----")
        with sr.Microphone() as source:
            #r.pause_threshold = 0.7
            try:   
                try:
                    audio = r.listen(source)
                    stop = r.recognize_google(audio, language='en-in')
                except:
                    continue
                print("You: " + stop)
                if 'stop' in stop or 'exit' in stop:
                    browser.quit()
                    return
                elif 'next' in stop:
                    # browser.find_element(By.XPATH,next_xpath).click()
                    actions.key_down(Keys.SHIFT).send_keys('n').key_up(Keys.SHIFT)
                    actions.perform()
                elif 'play' in stop or 'pause' in stop:
                    # browser.find_element(By.XPATH, pause_xpath).click()
                    actions.send_keys(Keys.SPACE)
                    actions.perform()
                elif 'low' in stop or 'decrease' in stop:
                    actions.send_keys(Keys.ARROW_DOWN)
                    actions.send_keys(Keys.ARROW_DOWN)
                    actions.send_keys(Keys.ARROW_DOWN)
                    actions.send_keys(Keys.ARROW_DOWN)
                    actions.perform()
                elif 'high' in stop or 'increase' in stop:
                    actions.send_keys(Keys.ARROW_UP)
                    actions.send_keys(Keys.ARROW_UP)
                    actions.send_keys(Keys.ARROW_UP)
                    actions.send_keys(Keys.ARROW_UP)
                    actions.perform()
                elif 'full' in stop:
                    actions.send_keys('f')
                    actions.perform()
                else:
                    continue
                
            except Exception as e:
                print(e)
                continue
    

# Function to open application
def Open(input):
    if 'chrome' in input:
        Speak("Google Chrome")
        os.startfile(
            "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk")
        return
    elif 'android studio' in input:
        Speak("Android Studio")
        os.startfile(
            "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Android Studio\Android Studio.lnk")
        return
    elif 'pycharm' in input:
        Speak("Pycharm")
        os.startfile(
            "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm Community Edition 2023.1.lnk")
        return
    elif 'word' in input:
        Speak("Microsoft Word")
        os.startfile(
            "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2016\Word 2016.lnk")
        return
    elif 'excel' in input:
        Speak("Microsoft Excel")
        os.startfile(
            "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2016\Excel 2016.lnk")
        return
    elif 'valorant' in input:
        Speak("Valorant")
        os.startfile(
            "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Riot Games\VALORANT.lnk")
        return
    elif 'unity' in input:
        Speak("Unity Hub")
        os.startfile(r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Unity Hub.lnk")
        return
    elif 'blender' in input:
        Speak("Blender")
        os.startfile(r"C:\Users\Rudrransh\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\blender\blender.lnk")
        return
    elif 'code' in input:
        Speak("Visual Studio Code")
        os.startfile(r"C:\Users\Rudrransh\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk")
        return
    elif 'teams' in input:
        Speak("Microsoft Teams")
        os.startfile(r"C:\Users\Rudrransh\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Microsoft Teams (work or school).lnk")
        return
    else:
        Speak("Sorry. The application you said could not be found")
        return

# Function to calculate
def Calculate(input):
    query = input.split(' ', 1)[1]
    client = wolframalpha.Client(wolfram_id)
    res = client.query(query)
    answer = next(res.results).text
    Speak(answer)
    return

# Function to process the command
async def Process(input):
    try:
        if 'search' in input or 'google' in input:
            Speak("Searching")
            SearchGoogle(input)
            return

        elif 'play' in input.lower():
            Speak("Playing")
            PlayYoutube(input)
            return

        elif "who are you" in input or "define yourself" in input:
            speak = '''Hello, I am Taylor. Your personal Assistant. I am here to make your life easier. You can command me to perform various tasks such as calculating sums or opening applications etcetra'''
            Speak(speak)
            return

        elif "who made you" in input or "created you" in input:
            speak = "I have been created by Rudrransh Saxena."
            Speak(speak)
            return

        elif "calculate" in input:
            Speak("Calculating")
            Calculate(input)
            return

        elif 'open' in input:
            Speak("Opening")
            Open(input)
            return

        else:
            Speak("I can search the web for you, Do you want to continue?")
            ans = Listen()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                Speak("Searching")
                SearchGoogle(input)
                return
            else:
                return

    except Exception as e:
        print(e)
        Speak("I don't understand, I can search the web for you, Do you want to continue?")
        ans = Listen()
        if 'yes' in str(ans) or 'yeah' in str(ans):
            Speak("Searching")
            SearchGoogle(input)
            return


if __name__ == "__main__":
    # Ask the name of user and says Hello
    Speak("What's your name Human?")
    name ='Human'
    name = Listen()
    Speak("Hello " + name + '.')
    
    # Ask for command on loop
    while(1):
        print("-----Inside main while loop-----")
        Speak("What can i do for you?")
        text = Listen()
 
        if text == 0:
            continue
 
        if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
            Speak("Ok bye "+ name+'.')
            break
 
        # Calling process text to process the query
        asyncio.run(Process(text))