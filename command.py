import os
from commands import cmnd_list
from commands import *

print(' CCLI v0.1b (unstable)')
print(' Type "help" for a list of available commands.\n')


def process_cmnd(cmnd):
    identify_cmnd(cmnd)

def identify_cmnd(cmnd):
    if cmnd in cmnd_list:
        cmnd_list[cmnd]()
    else: cmd_cmnd(cmnd)

def cmd_cmnd(cmnd):
    os.system(f'cmd /c {cmnd}')

while True:
    cmnd = input('>>> ')
    identify_cmnd(cmnd)

