from tkinter import *
import time
from subprocess import Popen

Freq = 2500
Dur = 150

top = Tk()
top.title('MapAwareness')
top.geometry('200x100') # Size 200, 200

def start():
    import os
#    os.system("python test.py")
    Popen(["python", "speech2text.py"])


def stop():
    print ("Stop")
    top.destroy()

startButton = Button(top, height=2, width=20, text ="Start",
command = start)
stopButton = Button(top, height=2, width=20, text ="Stop",
command = stop)

startButton.pack()
stopButton.pack()
top.mainloop()