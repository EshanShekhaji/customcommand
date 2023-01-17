import os
import webbrowser
import time


def print_help():
    print('''
CCLI v0.1b
Custom CLI made to make terminal life easier.
Here is a list of commands specific to CCLI:

help:   displays this screen
epic:   starts epic games launcher
exit:   exits the program
cmd:    cmd mode
python: python mode
        ''')

def epic():
    print("Process started: EpicGamesLauncher.exe")
    os.startfile("E:\epicgames\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe")

def exitx():
    print("Goodbye from CCLI!")
    time.sleep(1)
    exit()

def python():
    print("You are now in python. press Ctrl+Z and Return to exit.")
    os.system('cmd /c python')

def cmd():
    print("You are now in cmd. Type 'exit' to exit.")
    os.system('cmd')

def youtube():
    print('Process started: chrome:https://youtube.com')
    webbrowser.open_new_tab('https://youtube.com')


cmnd_list = {
    'epic': epic,
    'exit': exitx,
    'help': print_help,
    'python': python,
    'cmd': cmd,
    'yt': youtube,
}