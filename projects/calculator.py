from tkinter import *

root = Tk()
root.title("Calculator")

# Create calc. display
input_1 = Entry(root, width=35, borderwidth=5)
input_1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Making buttons
def button_clbks(number):
    input_1.delete(0, END)
    input_1.insert(0, number)


def create_buttons():
    button_one = Button(
        root, text="1", padx=50, pady=20, command=lambda: button_clbks(1)
    )
    button_two = Button(
        root, text="2", padx=50, pady=20, command=lambda: button_clbks(2)
    )
    button_three = Button(
        root, text="3", padx=50, pady=20, command=lambda: button_clbks(3)
    )
    button_four = Button(
        root, text="4", padx=50, pady=20, command=lambda: button_clbks(4)
    )
    button_five = Button(
        root, text="5", padx=50, pady=20, command=lambda: button_clbks(5)
    )
    button_six = Button(
        root, text="6", padx=50, pady=20, command=lambda: button_clbks(6)
    )
    button_seven = Button(
        root, text="7", padx=50, pady=20, command=lambda: button_clbks(7)
    )
    button_eight = Button(
        root, text="8", padx=50, pady=20, command=lambda: button_clbks(8)
    )
    button_nine = Button(
        root, text="9", padx=50, pady=20, command=lambda: button_clbks(9)
    )
    button_zero = Button(
        root, text="0", padx=50, pady=20, command=lambda: button_clbks(0)
    )

    button_add = Button(root, text="+", padx=50, pady=20, command=button_clbks).grid(
        row=5, column=0
    )

    button_equals = Button(root, text="=", padx=91, pady=20, command=button_clbks).grid(
        row=5, column=1, columnspan=2
    )

    button_clear = Button(
        root, text="Clear", padx=91, pady=20, command=button_clbks
    ).grid(row=4, column=1, columnspan=3)
    button_zero.grid(row=4, column=0)
    button_one.grid(row=3, column=0)
    button_two.grid(row=3, column=1)
    button_three.grid(row=3, column=2)
    button_four.grid(row=2, column=0)
    button_five.grid(row=2, column=1)
    button_six.grid(row=2, column=2)
    button_seven.grid(row=1, column=0)
    button_eight.grid(row=1, column=1)
    button_nine.grid(row=1, column=2)


if __name__ == "__main__":
    create_buttons()
    root.mainloop()
