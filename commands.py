import os
import webbrowser
import time


def print_help():
    print('''
 CCLI v0.3b
 Custom CLI made to make terminal life easier.

 Here is a list of commands specific to CCLI:

GENERAL:
help:   displays this screen
exit:   exits the program
cmd:    cmd mode
python: python mode

SYSTEM:
unity:  starts unity hub
epic:   starts epic games launcher

BROWSER:
yt:     opens https://youtube.com
trello: opens https://trello.com
kite:   opens https://kite.zerodha.com and https://pro.upstox.com
        ''')


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

def trello():
    print('Process started: chrome:https://trello.com')
    webbrowser.open_new_tab('https://trello.com')

def epic():
    print("Process started: EpicGamesLauncher.exe")
    os.startfile("E:\epicgames\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe")

def unity():
    print('Process started: UnityHub.exe')
    print('a little bug happens here where the cursor move to the next line, just press enter :)')
    os.startfile("E:\\Unity\\UnityHub\\Unity Hub\\Unity Hub.exe")

def kite():
    print('Process started: chrome:https://pro.upstox.com')
    print('Process started: chrome:https://kite.zerodha.com')
    webbrowser.open_new_tab("https://pro.upstox.com")
    webbrowser.open_new_tab("https://kite.zerodha.com")

cmnd_list = {
    'epic': epic,
    'exit': exitx,
    'help': print_help,
    'python': python,
    'cmd': cmd,
    'yt': youtube,
    'trello': trello,
    'unity': unity,
    'kite': kite,

}