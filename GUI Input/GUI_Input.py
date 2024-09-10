from tkinter import *
from PIL import Image, ImageTk

window = Tk()

def submit():
   username = entry.get()
   print("Hello "+ username)

def delete():
   entry.delete(0,END)

def backspace():
   entry.delete(len(entry.get())-1,END)

entry = Entry(window,font=("Arial",30))
button_submit = Button(window,font=("Arial",18),command=submit,text="Submit")
button_delete = Button(window,font=("Arial",18),command=delete,text="Delete")
button_backspace = Button(window,font=("Arial",18),command=backspace,text="Delete")

entry.pack()
button_submit.pack(side=RIGHT)
button_delete.pack(side=LEFT)
button_backspace.pack(side=RIGHT)
window.mainloop()