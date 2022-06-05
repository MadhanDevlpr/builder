import sys
import os

projects = '/home/codemap/Documents/Projects/Python'



def create_project():
    folder = sys.argv[1]# Get input of the folder's name

    os.chdir(projects) # Going into my projects directory
    os.system(f'mkdir {folder}') # Making the folder
    os.chdir(f'{projects}/{folder}')

    os.system('touch README.md') # creating a readme.md file

    os.system('subl .')



create_project()
