from tkinter import *
import winsound
from playsound import playsound
def playSound():
    playsound("lai.mp3",False)
    print("z")
def stopSound():
    winsound.PlaySound(None, winsound.SND_PURGE)
root = Tk()
button1 = Button(root,text='Play Sound',command=playSound)
button1.pack()

button2 = Button(root,text='Play Sound',command=stopSound)
button2.pack()

root.mainloop()

