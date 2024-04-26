import tkinter


def convert_it():
    inp = float(entry_celsius.get())
    out = (inp*9/5) + 32
    fah_result.config(text=f"{out}")


degree = chr(176)
window = tkinter.Tk()
window.minsize(width=300, height=200)
window.config(padx=10)
window.title("Celsius to Fahrenheit")

label = tkinter.Label(text="Temp Converter", font=("Arial", 15, "bold"))
label.grid(column=2, row=0)
label.config(padx=10, pady=20)

entry_celsius = tkinter.Entry(width=10)
entry_celsius.grid(column=2, row=1)

label_celsius = tkinter.Label(text=f"{degree}C", font=("arial", 15))
label_celsius.grid(column=3, row=1)

equals_label = tkinter.Label(text="is equals to ", font=("arial", 15))
equals_label.grid(column=1, row=2)

fah_result = tkinter.Label(text="0", font=("arial", 25))
fah_result.grid(column=2, row=2)

fah_label = tkinter.Label(text=f"{degree}F", font=("arial", 15))
fah_label.grid(column=3, row=2)

button_cal = tkinter.Button(text="Convert", width=10, command=convert_it)
button_cal.grid(column=2, row=3)

window.mainloop()
