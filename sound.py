import winsound
import os
from playsound import playsound



winsound.Beep(1000,1000)  #Beep at 1000 Hz for 1000 ms

os.chdir('C:/Users/Area51/Desktop') #songs dir
# print(os.getcwd())
playsound('lai.mp3') #play sound with playsound




