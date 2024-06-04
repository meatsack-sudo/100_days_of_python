from tkinter import *
from tkinter import messagebox
import os
from random import choice, randint, shuffle
import pyperclip
import json

FONT_NAME = "Courier"
FILE_DIR = os.path.expanduser("~/Desktop/100_days_of_python/password-manager-start/data.json")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    if len(password_entry.get()) > 0:
        password_entry.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))] 
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password_entry.get())

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():

    user_website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if not user_website or not email or not password:
        messagebox.showwarning(title="Missing fields", message="Please fill out all fields.")
        return

    new_data = {
        user_website: {
            "email": email,
            "password": password
        }
    }

    #global FILE_DIR
    if not os.path.isfile(FILE_DIR):
        messagebox.showinfo(title="File not found", message=f"Creating {FILE_DIR}. All login infomration will be stored here.")
        with open(FILE_DIR, "w") as file:
            json.dump(new_data, file, indent=4)
    else:
        with open(FILE_DIR, "r") as file:
            try:
            #Reading old data
                data = json.load(file)
            #Updating old data with new data
            except json.JSONDecodeError:
                data = {}

        data.update(new_data)

        with open(FILE_DIR, "w") as file:
            #Saving updated data
            json.dump(data, file, indent=4)

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    #file.write("Website | Email/Username | Password")

# ---------------------------- SEARCH SETUP ------------------------------- #

def find_password():

    try:
        with open(FILE_DIR, "r") as file:
            json_file = json.load(file)

    except FileNotFoundError:
        messagebox.showerror(title="File not found", message="Could not find a file with login information. Add login information and I'll create the file.")

    website = website_entry.get()

    if website_entry.get() in json_file:
        messagebox.showinfo(title=f"{website.title()} log in information", message=f"Website: {website}\nEmail: {json_file[website]["email"]}\nPassword: {json_file[website]["password"]}")
    else:
        messagebox.showerror(title="No data found", message="No matching website found. Try your search again or add login information.")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#website label and entry
website_label = Label(text="Website:", justify="left", font=(FONT_NAME, 10))
website_entry = Entry(width=30)
website_entry.focus()


website_label.grid(column=0, row=1, sticky="w")
website_entry.grid(column=1, row=1, sticky="e")

#email/username label and entry
email_username_label = Label(text="Email/Username:", justify="left", font=(FONT_NAME, 10))
email_username_entry = Entry(width=50)

email_username_label.grid(column=0, row=2, sticky="w")
email_username_entry.grid(column=1, row=2, columnspan=2, sticky="e")
email_username_entry.insert(END, "alexerombou@gmail.com")

#password label, entry, button
password_label = Label(text="Password:", justify="left", font=(FONT_NAME, 10))
password_entry = Entry(width=30)
gen_password_button = Button(text="Generate Password", width=16, command=generate_password)

password_label.grid(column=0, row=3, sticky="w")
password_entry.grid(column=1, row=3, sticky="e")
gen_password_button.grid(column=2, row=3, sticky="e")

#add button
add_button = Button(text="Add", width=36, command=save_password)

add_button.grid(column=1, row=4, columnspan=2)

#search button
search_button = Button(text="Search", width=16, command=find_password)
search_button.grid(column=2, row=1)

# canvas for the logo
canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="C:/Users/Meatsack/Desktop/100_days_of_python/password-manager-start/logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(column=1, row=0)

window.mainloop()
