
import tkinter
from tkinter import *


win= tkinter.Tk()
win.title("Rounded Button")


win.geometry("700x300")



def my_command():
   text.config(text= "You have clicked Me...")

click_btn= PhotoImage(file='BK.png')
button= Button(win, image=click_btn,command= my_command,
borderwidth=0)
button.pack(pady=30)

click_btn1= PhotoImage(file='BQ.png')
button1= Button(win, image=click_btn1,command= my_command,
borderwidth=0)
button1.pack(pady=30)

text= Label(win, text= "")
text.pack(pady=30)

win.mainloop()
