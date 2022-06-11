
import sys
import os
import pyttsx3
import webbrowser
import pyautogui
import maskpass
import time



engine = pyttsx3.init()

projects = '/home/codemap/Documents/Projects/Python'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

password = maskpass.askpass(mask="")

def create_project():
    folder = sys.argv[1]# Get input of the folder's name


    webbrowser.open('https://github.com/new')
    time.sleep(5)
    pyautogui.moveTo(860,480)
    pyautogui.click()
    pyautogui.write(folder)
    time.sleep(2)
    pyautogui.moveTo(609,817)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(860,480)
    pyautogui.click()
    pyautogui.press('enter')
    pyautogui.press('enter')



    time.sleep(5)

    os.chdir(projects) # Going into my projects directory

    os.system(f'git clone https://github.com/MadhanDevlpr/{folder}.git') # intializing git



    os.chdir(f"{projects}")
    os.system('subl .')



create_project()
speak('Your project has been successfully established.')


# Made by me, for me, to spped up my workflow 

