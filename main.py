from tkinter import *
from tkinter import messagebox
import pyperclip
import json

from password_gen import GeneratePassword

FONT_NAME = "Arial"
WHITE = "#ffffff"
BLACK = "#000000"
EMAIL = "work.phumelela@gmail.com"


# --------------------------------- SEARCH -------------------------------------- #
def search():
    website = web_entry.get()
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No Details for {website} exist.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_button_clicked():
    password = GeneratePassword()
    password_text = password.generate_password()
    password_entry.insert(0, password_text)
    pyperclip.copy(password_text)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_button_clicked():
    website = web_entry.get()
    user_text = user_entry.get()
    pass_text = password_entry.get()
    new_data = {
        website: {
            "email": user_text,
            "password": pass_text,
        }
    }

    if len(website) == 0 or len(pass_text) == 0 or len(user_text) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any empty fields.")

    else:
        try:
            # Look for "passwords.json"
            with open("passwords.json", "r") as file:
                data = json.load(file)
                data.update(new_data)

        # If it doesn't exist, create it and put something in it
        except FileNotFoundError:
            with open("passwords.json", "w") as file:
                json.dump(new_data, file)
        else:
            # If the file does exist, we can finally write it.
            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)

        # Clear all entry fields
        web_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20, bg=BLACK)

canvas = Canvas(width=200, height=200, bg=BLACK, highlightthickness=0)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(column=1, row=0)

# Labels
web_label = Label(text="Website:", font=(FONT_NAME, 15, "normal"))
web_label.config(bg=BLACK, fg=WHITE)
web_label.grid(column=0, row=1, pady=10)

user_label = Label(text="Email/Username:", font=(FONT_NAME, 15, "normal"))
user_label.config(bg=BLACK, fg=WHITE)
user_label.grid(column=0, row=2, pady=10)

password_label = Label(text="Password:", font=(FONT_NAME, 15, "normal"))
password_label.config(bg=BLACK, fg=WHITE)
password_label.grid(column=0, row=3, pady=10)

# Entries
web_entry = Entry(width=19, highlightthickness=1)
web_entry.grid(column=1, row=1)
web_entry.focus()

user_entry = Entry(width=35, bg=BLACK, highlightthickness=0)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, EMAIL)

password_entry = Entry(width=19, bg=BLACK, highlightthickness=0)
password_entry.grid(column=1, row=3)

# Buttons
search_button = Button(text="Search", command=search)
search_button.config(bg=BLACK, highlightbackground=BLACK, width=12)
search_button.grid(column=2, row=1)

generate_button = Button(text="Generate Password", command=generate_button_clicked)
generate_button.config(bg=BLACK, highlightbackground=BLACK, width=12)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", command=add_button_clicked)
add_button.config(bg=BLACK, highlightbackground=BLACK, width=33)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
