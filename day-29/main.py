from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)


def generate_password():
    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    website_len = len(website)
    password_len = len(password)
    print(website_len)
    if website_len == 0 or password_len == 0:
        messagebox.showinfo(title="Warning!", message="Please don't leave empty entry")
    else:
        is_ok = messagebox.askyesno(title='Confirm', message=f'Do you want add this information to database ?\n'
                                                             f' {website}\n {username}\n {password}')
        if is_ok:
            with open("text.txt", "a", encoding='utf-8') as file:
                file.write(f"Website: {website} | Username: {username} | Password: {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)

label1 = Label(text="Website:")
label1.grid(column=0, row=1)

website_entry = Entry(width=55)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

label2 = Label(text="Email/Username")
label2.grid(column=0, row=2)

username_entry = Entry(width=55)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "m.alaly1998@gmail.com")

label3 = Label(text="Password")
label3.grid(column=0, row=3)

password_entry = Entry(width=36)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, columnspan=2)

add_button = Button(width=45, text="Add", command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
