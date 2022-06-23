from tkinter import *

# Constructing a toplevel Tk widget, usually the main window of the application.
root = Tk()

myLabel = Label(root, text="Hello World")  # Creating a label widget
myLabel.pack()  # Placing the label unto the screen

root.mainloop()
