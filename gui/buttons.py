from tkinter import *

root = Tk()


def clbkButton():
    """Creating a callback function that gets executed when the button is clicked.
    As an example, this just prints the button has been clicked.
    """
    myLabel = Label(root, text="The button has been clicked")
    myLabel.pack()


myButton = Button(root, text="Click Here", command=clbkButton, fg="black", bg="green")
myButton.pack()

root.mainloop()
