from tkinter import *
# from PIL import ImageTk,Image
root =Tk()
# canv = Canvas(root,bg='red')
# canv.pack(fill="both", expand=True)
photo = PhotoImage(file='n.png')
lable1 = Label(root,image=photo)
lable1.pack(fill="both", expand=True)
root.mainloop()