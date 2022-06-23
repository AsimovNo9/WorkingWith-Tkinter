from tkinter import *

root = Tk()

# Making a grid utilizes the label attached method grid with the position in cartesian coordinate style
label_1 = Label(root, text="Hello World").grid(row=0, column=0)
label_2 = Label(root, text="Welcome to the end").grid(row=1, column=0)

root.mainloop()
