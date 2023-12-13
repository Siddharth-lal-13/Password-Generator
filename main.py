from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
import math
import os


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def size(value):
    return value


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    x = length.get()
    val = int(round(x/2))
    half = math.floor(val/2)

    password_list = [random.choice(letters) for _ in range(val)]
    password_list += [random.choice(symbols) for _ in range(half)]
    if val % 2 != 0:
        password_list += [random.choice(numbers) for _ in range(half + 1)]
    else:
        password_list += [random.choice(numbers) for _ in range(half)]

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        web: {
            "email": email,
            "password": password,
        },
    }

    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please don't leave any fields empty!")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data and updating it with new data
                data = json.load(data_file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    web = website_entry.get()

    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showerror(title="Error", message="No Data File Found.")
    else:
        if web in data:
            pyperclip.copy(data[web]['password'])
            messagebox.showinfo(title=web, message=f"Email/Username: {data[web]['email']} "
                                                   f"\nPassword: {data[web]['password']} "
                                                   f"\n\n(The password has been copied to the clipboard)")
        else:
            messagebox.showwarning(title="Error", message=f"No details for {web} exists.")


# ---------------------------- USERNAME ------------------------------- #
def user():
    user_id = email_entry.get()
    try:
        if os.path.getsize("username.txt") == 0:
            if len(email_entry.get()) == 0:
                messagebox.showinfo(title="Oops!", message="No username exists.")
            else:
                with open("username.txt", "w") as email_id:
                    email_id.write(user_id)
    except FileNotFoundError:
        with open("username.txt", "w") as email_id:
            email_id.write(user_id)
    else:
        if len(email_entry.get()) == 0:
            with open("username.txt", "r") as email_id:
                email_entry.insert(0, email_id.read())
        else:
            with open("username.txt", "w") as email_id:
                email_id.write(user_id)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

canvas = Canvas(window, width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website = Label(text="Website:")
website.grid(column=0, row=1)
username = Label(text="Email/Username:")
username.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entries
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1, sticky="ew")
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, sticky="ew")
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew")

# Buttons
search = Button(text="Search", command=find_password)
search.grid(column=2, row=1, sticky="ew", pady=5, padx=5)
save_id = Button(text="Save/Retrieve", command=user)
save_id.grid(column=2, row=2, sticky="ew", pady=5, padx=5)
generate = Button(text="Generate Password", command=generate_password)
generate.grid(column=2, row=3, sticky="ew", pady=5, padx=5)
add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=5, columnspan=2, sticky="ew", pady=5, padx=5)

# Scale
length = Scale(orient="horizontal", from_=4, to=20, command=size, tickinterval=2, resolution=2)
length.set(8)
length.grid(column=1, row=4, columnspan=2, sticky="ew")


window.mainloop()
