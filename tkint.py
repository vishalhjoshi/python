from tkinter import *
root = Tk()
topframe = Frame(root)
topframe.pack()

bottomframe = Frame(root)
bottomframe.pack(side = BOTTOM)

textbox1 = Entry(topframe,text="This is text box1")
textbox1.pack()
label1  = Label(topframe,text='Label1')
label1.pack()

textbox2 = Entry(topframe,text="This is text box2")
textbox2.pack()
label2  = Label(topframe,text='Label2')
label2.pack()




button1 = Button(topframe,text='Button1',fg='white',bg='green')
button1.pack(side = LEFT)
button2 = Button(topframe,text='Button2',fg='white',bg='red')
button2.pack(side = LEFT)
button3 = Button(topframe,text='Button3',fg='white',bg='blue')
button3.pack(side = LEFT)

root.mainloop()