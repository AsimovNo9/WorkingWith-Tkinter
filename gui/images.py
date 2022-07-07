from tkinter import *


root = Tk()
root.title("Images")
root.iconbitmap(
    "C:/Users/adeda/Desktop/MachineLearningPytorch/TkinterPractice/images/icon.ico"
)


button_quit = Button(root, text="Exit", bg="red", fg="yellow", command=root.quit)
button_quit.pack()
root.mainloop()
