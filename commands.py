import os

def epic():
    print("Process Started: EpicGamesLauncher.exe")
    os.startfile("E:\epicgames\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe")

def exitx():
    exit()

def print_help():
    print('''
this
is
it
        ''')

cmnd_list = {
    'epic': epic,
    'exit': exitx,
    'help': print_help
}