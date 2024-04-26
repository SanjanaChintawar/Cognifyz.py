import tkinter
from tkinter import *


def check_for_palindrome():
    user_input = input_entry.get()
    reversed_input = user_input[::-1]

    if user_input == reversed_input:
        result_label.config(text="Yes!, It's a palindrome.", foreground="green")
    else:
        result_label.config(text="Nah!, It's not a palindrome.", foreground="red")


window = Tk()
window.title("Is Palindrome.")
window.minsize(width=600, height=400)
window.config(padx=20, pady=80)

result_label = Label(text="Is it a Palindrome ?", font=("Arial", 25, "bold"))
result_label.config(padx=0, pady=50)
result_label.grid(row=0, column=1)
#
input_label = Label(text="Enter the value: ", font=("Arial", 20, "bold"))
input_label.grid(row=1, column=0)
#
input_entry = tkinter.Entry(width=45)
input_entry.focus()
input_entry.grid(row=1, column=1, columnspan=2)
#
check_button = Button(text="Check", width=10, font=("Arial", 12, "normal"), command=check_for_palindrome)
check_button.grid(row=2, column=1)

window.mainloop()
