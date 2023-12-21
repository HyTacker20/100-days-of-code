from tkinter import *


def button_clicked():
    miles = miles_input.get()
    try:
        kms = float(miles) * 1.609344
        result_label.config(text=round(kms, 5))
    except ValueError:
        pass


window = Tk()
window.title("My first GUI program")
window.minsize(width=200, height=100)
window.config(padx=10, pady=10)

miles_input = Entry(width=10)
miles_input.grid(column=2, row=1)

miles_label = Label(text="Miles", font=("Arial", 10))
miles_label.grid(column=3, row=1)

equal_label = Label(text="is equal to", font=("Arial", 10))
equal_label.grid(column=1, row=2)

km_label = Label(text="Km", font=("Arial", 10))
km_label.grid(column=3, row=2)

result_label = Label(text="0", font=("Arial", 10))
result_label.grid(column=2, row=2)

button = Button(text="Click me!", command=button_clicked)
button.grid(column=2, row=3)

window.mainloop()
