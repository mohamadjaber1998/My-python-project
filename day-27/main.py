from tkinter import *


def clicked():
    number = int(my_entry.get())
    result = round(number * 1.6)
    my_label2["text"] = result


window = Tk()
window.title("My first GUI")
window.minsize(width=200, height=150)
window.config(padx=50, pady=0)

my_label1 = Label(text="Is equal to", font=("Arial", 20))
my_label1.grid(column=0, row=1)
my_label1.config(padx=10)

my_entry = Entry(width=10)
my_entry.grid(column=1, row=0)

my_label = Label(text="Miles", font=("Arial", 20))
my_label.grid(column=2, row=0)
my_label.config(padx=10)

my_button = Button(text="Change", command=clicked)
my_button.grid(column=1, row=2)

my_label2 = Label(text=0, font=("Arial", 20))
my_label2.grid(column=1, row=1)
my_label2.config(padx=10, pady=10)

my_label3 = Label(text="KM", font=("Arial", 20))
my_label3.grid(column=2, row=1)
my_label3.config(padx=10)
window.mainloop()

