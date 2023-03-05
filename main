import os
import json
import base64
import pathlib
import warnings
from shutil import *
import glob
import json

warnings.filterwarnings(action='ignore')

def show_saved(data):
    if data == {}:
        print('No data.json file found, create a new one with Mode: 3')
    else:
        print(data)

def saveJson(data): # create or overrides existing json file
    with open('data.json', 'w') as fp:
        json.dump(data, fp, sort_keys=True, indent=4)

def loadJson(): # loads the json file to dict
    try:
        with open('data.json', 'r') as fp:
            data = json.load(fp)
    except:
        data = {}
    return data
    
def copytree(src, dst, symlinks=False, ignore=None):    # takes source and saves it to destination folder
    names = os.listdir(src)
    if ignore is not None:
        ignored_names = ignore(src, names)
    else:
        ignored_names = set()

    if not os.path.isdir(dst): # This one line does the trick
        os.makedirs(dst)
    errors = []
    for name in names:
        if name in ignored_names:
            continue
        srcname = os.path.join(src, name)
        dstname = os.path.join(dst, name)
        try:
            if symlinks and os.path.islink(srcname):
                linkto = os.readlink(srcname)
                os.symlink(linkto, dstname)
            elif os.path.isdir(srcname):
                copytree(srcname, dstname, symlinks, ignore)
            else:
                # Will raise a SpecialFileError for unsupported file types
                copy2(srcname, dstname)
        # catch the Error from the recursive copytree so that we can
        # continue with other files
        except Error as err:
            errors.extend(err.args[0])
        except EnvironmentError as why:
            errors.append((srcname, dstname, str(why)))
    try:
        copystat(src, dst)
    except OSErrora as why:
        if WindowsError is not None and isinstance(why, WindowsError):
            # Copying file access times may fail on Windows
            pass
        else:
            errors.extend((src, dst, str(why)))
    if errors:
        raise errors
    
def backup_apply():   # applys the saved backup to the normal valorant folder
    if os.path.isdir('backup'):
        backup_path = "backup\Saved\Config"
        destination_dir = pathlib.Path(os.getenv('LOCALAPPDATA')) / r'VALORANT\Saved\Config'
        copytree(backup_path, destination_dir)
        print("Successfully applied the backup! \n")
    else:
        print("create a backup first")
    
def backup_save():   # make a backup from saves folder
    backup_path = pathlib.Path(os.getenv('LOCALAPPDATA')) / r'VALORANT\Saved\Config'
    destination_dir = "backup\Saved\Config"
    print(backup_path)
    print(destination_dir)
    copytree(backup_path, destination_dir)
    print("Successfully created a backup! \n")

def saveSettingslocal(data):    # saves the current account folder and creates a json dic with a userinput name
    RiotLocalMachine_path = pathlib.Path(os.getenv('LOCALAPPDATA')) / r'VALORANT\Saved\Config\Windows\RiotLocalMachine.ini'
    if not RiotLocalMachine_path.is_file():
        raise RuntimeError('Last Account not found')

    with open(RiotLocalMachine_path, 'r') as lockfile:
        data = lockfile.read().split('=')
        string = data[1].strip()
        localuser = string + "-eu"
    localname = "VALORANT/Saved/Config/" + localuser
    localsettings_path = pathlib.Path(os.getenv('LOCALAPPDATA')) / localname
    destination_dir = "saves/" + localuser
    print("Type a name for your Account")
    userinput = str(input("Name: "))
    if not localuser in data.values() and not userinput in data.keys():
        data [userinput] = localuser
        saveJson(data)
        copytree(localsettings_path, destination_dir, False, None)
        print("Settings successfully saved! \n")
    elif localname in data.values():
        print('name already exists')
    else:
        print('save already exists')

def pastSettingslocal(data):
    if data == {}:
        print('No data.json file found, create a new one with Mode: 3')
    else:
        print("Type your Account you want to copy the settings from.")
        src = str(input("Name: "))
        print("Type your account you want to paste the settings to.")
        dst = str(input("Name: "))
        source_dir = "saves/" + data[src]
        localname = "VALORANT/Saved/Config/" + data[dst]
        destination_dir = pathlib.Path(os.getenv('LOCALAPPDATA')) / localname
        copytree(source_dir, destination_dir)
        print("Settings successfully applied! \n")
    

def program_start():
    if os.path.isdir(pathlib.Path(os.getenv('LOCALAPPDATA')) / r'VALORANT\Saved\Config'):
        print("\nFußfetisch Accountsharing")
        print("Mode 1. Show created names")
        print("Mode 2. Backup")
        print("Mode 3. Save your current settings")
        print("Mode 4. Apply settings")
        print("Mode 5. Quit")
        userinput = int(input("Mode: "))
        while True:
            data = loadJson()
            if userinput == 1:
                show_saved(data)
                program_start()
            elif userinput == 2:
                print("Mode 1. Create a backup")
                print("Mode 2. Apply the backup")
                userinput = int(input("Mode: "))
                if userinput == 1:
                    backup_save()
                elif userinput == 2:
                    backup_apply()
                else:
                    print("you have to type a number \n")
                    quit()
                program_start()
            elif userinput == 3:
                saveSettingslocal(data)
                program_start()
            elif userinput == 4:
                pastSettingslocal(data)
                program_start() 
            elif userinput == 5:
                quit()  
            else:
                print("you have to type a number \n")
                quit()
    else:
        print('no valorant settings found')

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
program_start()
