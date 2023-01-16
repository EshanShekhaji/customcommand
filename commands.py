import os

def epic():
    print("Process Started: EpicGamesLauncher.exe")
    os.startfile("E:\epicgames\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe")

def exitx():
    exit()

cmnd_list = {
    'epic': epic,
    'exit': exitx
}

print ("ia m here")