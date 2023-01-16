import os
import commands
from commands import cmnd_list
from commands import *

print('''
    Custom Command Console v0
    All cmd commands are available as well as some custom ones.
    Jump in and out of cmd by typing 'cmd'. Exit using "exit".
''')



def process_cmnd(cmnd):
    identify_cmnd(cmnd)

def identify_cmnd(cmnd):
    if cmnd in cmnd_list:
        cmnd_list[cmnd]()
    else: cmd_cmnd(cmnd)

def cmd_cmnd(cmnd):
    os.system(f'cmd /c {cmnd}')


exit = False
while exit == False:
    cmnd = input(">>> ")
    identify_cmnd(cmnd)
    exit == False

