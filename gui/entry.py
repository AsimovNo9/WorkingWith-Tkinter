from cgitb import grey
from tkinter import *

root = Tk()

# Creating the input object, packing it into the window,
# and inserting default text into the form
e = Entry(root, width=25, bg="grey", fg="white")
e.pack()
e.insert(0, "What's your name buddy?")


def clbkButton():
    """Creating a callback function that gets executed when the button is clicked.
    As an example, this just prints the button has been clicked.
    """
    myLabel = Label(
        root, text=f"You have saved {e.get()}"
    )  # Passing the input defined as e above with the get() method of the Entry class
    myLabel.pack()


myButton = Button(root, text="Save Name", command=clbkButton, fg="black", bg="green")
myButton.pack()

root.mainloop()
