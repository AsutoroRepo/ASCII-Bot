import pyautogui
import pyperclip
from tkinter import *
import time

def type_unicode(text):
    pyperclip.copy(text)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)


def printASCII(ASCII_art):
    for line in ASCII_art.split('\n'):
        
        print(line)
        type_unicode(line)
        pyautogui.press("enter")
        time.sleep(.25)
# Make a window with a text area with tkinter
root = Tk()
root.title("ASCII Art Generator")
root.geometry("500x500")
# Create a text box
text_box = Text(root, width=50, height=10)
text_box.pack()
# Create a button to generate the ASCII art
button = Button(root, text="Sumbit ASCII Art", command=lambda: printASCII(text_box.get("1.0", "end-1c")))

button.pack()
# Start the GUIv

root.mainloop() 


