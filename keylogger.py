from pynput.keyboard import Listener

#log_file="C:\Users\Hassan Eissa\github\Keylogger"

def on_press(key):
    print(key)

def on_release(rel):
    print(rel)

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
