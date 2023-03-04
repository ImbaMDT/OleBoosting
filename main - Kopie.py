import os
import json
import base64
import pathlib
import warnings
import shutil

warnings.filterwarnings(action='ignore')

def backup():
    backup_path = pathlib.Path(os.getenv('LOCALAPPDATA')) / r'VALORANT\Saved\Config'
    destination_dir = "backup\Saved\Config"
    shutil.copytree(backup_path, destination_dir)


def saveSettingslocal():
    RiotLocalMachine_path = pathlib.Path(os.getenv('LOCALAPPDATA')) / r'VALORANT\Saved\Config\Windows\RiotLocalMachine.ini'
    if not RiotLocalMachine_path.is_file():
        raise RuntimeError('Last Account not found')

    with open(RiotLocalMachine_path, 'r') as lockfile:
        data = lockfile.read().split('=')
        string = data[1].strip()
        localuser = string + "-eu"
    localname = "VALORANT/Saved/Config/" + localuser
    localsettings_path = pathlib.Path(os.getenv('LOCALAPPDATA')) / localname
    destination_dir = localuser
    shutil.copytree(localsettings_path, destination_dir)


def applySettings():
    lockfile_path = pathlib.Path(os.getenv('LOCALAPPDATA')) / r'Riot Games\Riot Client\Config\lockfile'
    if not lockfile_path.is_file():
        raise RuntimeError('Lockfile not found')

    with open("settings.json", "r") as settings_data, open(lockfile_path, "r") as lockfile:
        data = lockfile.read().split(':')
        headers = {
            "Authorization": "Basic " + base64.b64encode(('riot:' + data[3]).encode()).decode()
        }
        requests.put("https://127.0.0.1:" + data[2] + "/player-preferences/v1/data-json/Ares.PlayerSettings",
                     verify=False, headers=headers, data=settings_data).json()


print(r'''
  ____  _      ____                  _   _                                  
 / __ \| |    |  _ \                | | (_)                                 
| |  | | | ___| |_) | ___   ___  ___| |_ _ _ __   __ _   ___ ___  _ __ ___  
| |  | | |/ _ \  _ < / _ \ / _ \/ __| __| | '_ \ / _` | / __/ _ \| '_ ` _ \ 
| |__| | |  __/ |_) | (_) | (_) \__ \ |_| | | | | (_| || (_| (_) | | | | | |
 \____/|_|\___|____/ \___/ \___/|___/\__|_|_| |_|\__, (_)___\___/|_| |_| |_|
                                                  __/ |                     
                                                 |___/                       

''')

print("Fußfetisch Accountsharing")
print("Mode 1. Create a backup")
print("Mode 2. Save your current settings")
print("Mode 3. Apply settings")
userinput = int(input("Mode: "))

while True:
    if userinput == 1:
        backup()
        print("Successfully backup!")
        quit()
    elif userinput == 2:
        saveSettingslocal()
        print("Settings successfully saved!")
        quit()
    elif userinput == 3:
        applySettings()
        print("Settings successfully applied!")
        quit()        
    else:
        print("Open VALORANT or enter the right number!")
        quit()
