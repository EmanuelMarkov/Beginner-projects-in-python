from tkinter import *
from PIL import Image, ImageTk
def click():
    print("You clicked the button HSSSSS")
    
window = Tk() #instance of a window for us
window.geometry("520x420")
window.title("EmoCodeFirstGUI")

logo = PhotoImage(file=r"C:\Users\Filche\Beginner-projects-in-python\GUI\png-clipart-leaf-logo-green-leaves-green-and-teal-leaf-logo-text-maple-leaf.png")
window.iconphoto(True,logo)
window.config(background="black")


#button
button = Button(window, text="Click me",command=click,font=("Comic sans",30),fg="red",activebackground="white",activeforeground="black")

photoOfCat = PhotoImage(file=r"C:\Users\Filche\Beginner-projects-in-python\GUI\Cat.png")

lable = Label(window,
              text="Hi, I am Wiskers"
              ,fg="white"
              ,bg="black"
              ,font=("Ariel",40,"bold")
              ,relief=RAISED
              ,bd=10
              )


lable.pack()


photo = Label(window,image=photoOfCat,bg="black")

photo.pack()


button.pack()

window.mainloop()