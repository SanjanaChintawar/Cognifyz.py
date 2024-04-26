import re
import tkinter


def check_email():
    user_email = email_entry.get()
    email_conditions = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"

    if re.search(email_conditions, user_email):
        header_label.config(text="Valid Email", foreground="green", bg="white")
    else:
        header_label.config(text="Invalid Email", foreground="red", bg="white")


window = tkinter.Tk()
window.minsize(width=500, height=300)
window.config(pady=20, padx=20)
window.title("Is your email valid?")

header_label = tkinter.Label(text="Email Validator", font=("Arial", 30, "bold"), foreground="dark blue",
                             bg="light gray")
header_label.place(x=130, y=50)

email_label = tkinter.Label(text="Enter Your Email:", font=("Arial", 16, "bold"))
email_label.place(x=30, y=150)

email_entry = tkinter.Entry(width=25)
email_entry.focus()
email_entry.place(x=170, y=150)

check_button = tkinter.Button(text="Check email", font=("Arial", 15, "normal"), foreground="blue", command=check_email)
check_button.place(x=150, y=200)

window.mainloop()
