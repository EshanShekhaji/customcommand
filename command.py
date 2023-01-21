import os
from commands import cmnd_list
from commands import priv_cmnd_list
from commands import password
from commands import login

print("ME WHEN THE")
print(' CCLI v1.0')
print(' Type "help" for a list of available commands.\n')

sudo = False

def process_cmnd(cmnd):
    identify_cmnd(cmnd)

def identify_cmnd(cmnd):
    if cmnd in cmnd_list:
        cmnd_list[cmnd]()
    elif cmnd == 'login':
        global sudo
        sudo = login()
    else: cmd_cmnd(cmnd)

def identify_priv_cmnd(cmnd):
    if cmnd in priv_cmnd_list:
        priv_cmnd_list[cmnd]()
    elif cmnd == 'login':
        global sudo
        sudo = login()
    else: cmd_cmnd(cmnd)

def cmd_cmnd(cmnd):
    os.system(f'cmd /c {cmnd}')



while True:
    cmnd = input('>>> ')
    if sudo == True:
        identify_priv_cmnd(cmnd)
    else: identify_cmnd(cmnd)
