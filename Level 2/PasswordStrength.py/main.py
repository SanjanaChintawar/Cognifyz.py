import re
import tkinter


def check_strength():
    password = password_entry.get()
    if len(password) < 8:
        result.config(text="Password length must be greater than 8.", foreground="red")
    elif not re.search("[A-Z]", password):
        result.config(text="password should contain at least one uppercase", foreground="red")
    elif not re.search("[a-z]", password):
        result.config(text="password should contain at least one lowercase", foreground="red")
    elif not re.search("[0-9]", password):
        result.config(text="password should contain at least one number.", foreground="red")
    else:
        tag_label.config(text="Password is strong to use.", foreground="green", font=("Arial", 25, "bold"))
        result.config(text="")


window = tkinter.Tk()
window.minsize(width=500, height=400)
window.config(pady=20, padx=20)
window.title("Is your password strong?")

tag_label = tkinter.Label(text="Password Strength Checker", font=("Poplar Std", 25, "bold"), foreground="dark red")
tag_label.config(pady=20)
tag_label.place(x=50, y=30)

line_label = tkinter.Label(text="Enter The Password:", font=("Arial", 17))
line_label.place(x=-10, y=150)
#
password_entry = tkinter.Entry(width=30)
password_entry.focus()
password_entry.place(x=160, y=150)
#
check_button = tkinter.Button(text="Check", width=10, highlightthickness=0, command=check_strength)
check_button.place(x=160, y=200)

result = tkinter.Label(text="", font=("Arial", 18, "bold"))
result.place(x=30, y=270)

window.mainloop()
