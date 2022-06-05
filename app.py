import sys
import os
import pyttsx3

engine = pyttsx3.init()

projects = '/home/codemap/Documents/Projects/Python'


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def create_project():
    folder = sys.argv[1]# Get input of the folder's name

    os.chdir(projects) # Going into my projects directory
    os.system(f'mkdir {folder}') # Making the folder
    os.chdir(f'{projects}/{folder}')

    os.system('touch app.py') # creating a python file

    os.system('subl .')



create_project()
speak('Your project has been successfully established.')