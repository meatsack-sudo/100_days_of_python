from tkinter import *
from tkinter import messagebox
import os
from random import choice, randint, shuffle
import pyperclip

FONT_NAME = "Courier"
FILE_DIR = os.path.expanduser("~/Desktop/100_days_of_python/password-manager-start/data.txt")

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
    #global FILE_DIR
    if os.path.isfile(FILE_DIR) == False:
        messagebox.showinfo(title="data.txt not found", message=f"Creating data.txt file at {FILE_DIR}. All login infomration will be stored here.")
        with open(FILE_DIR, "w") as file:
            file.write("Website | Email/Username | Password")

    if os.path.isfile(FILE_DIR):
        if len(website_entry.get()) < 3 or len(email_username_entry.get()) < 4 or len(password_entry.get()) < 4:
            empty_check = messagebox.askokcancel(title="Short entries detected", message=f"One or more of your entered fields seem incomplete. Would you like to continue?\nWebsite: {website_entry.get()}\nEmail/Username: {email_username_entry.get()}\nPassword: {password_entry.get()}")
            if empty_check:
                with open(FILE_DIR, "a") as file:
                    file.write("\n" + website_entry.get() + " | " + email_username_entry.get() + " | " + password_entry.get())
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
        else:
            is_ok = messagebox.askokcancel(title="Are you sure?", message=f"Would you like to save the following to data.txt? \n\nWebsite: {website_entry.get()}\nEmail/Username: {email_username_entry.get()}\nPassword: {password_entry.get()}")
        
            if is_ok:
                with open(FILE_DIR, "a") as file:
                    file.write("\n" + website_entry.get() + " | " + email_username_entry.get() + " | " + password_entry.get())
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#website label and entry
website_label = Label(text="Website:", justify="left", font=(FONT_NAME, 10))
website_entry = Entry(width=36)
website_entry.focus()


website_label.grid(column=0, row=1, sticky="w")
website_entry.grid(column=1, row=1, columnspan=2)

#email/username label and entry
email_username_label = Label(text="Email/Username:", justify="left", font=(FONT_NAME, 10))
email_username_entry = Entry(width=36)

email_username_label.grid(column=0, row=2, sticky="w")
email_username_entry.grid(column=1, row=2, columnspan=2)
email_username_entry.insert(END, "alexerombou@gmail.com")

#password label, entry, button
password_label = Label(text="Password:", justify="left", font=(FONT_NAME, 10))
password_entry = Entry(width=21)
gen_password_button = Button(text="Generate Password", command=generate_password)

password_label.grid(column=0, row=3, sticky="w")
password_entry.grid(column=1, row=3)
gen_password_button.grid(column=2, row=3)

#add button
add_button = Button(text="Add", width=36, command=save_password)

add_button.grid(column=1, row=4, columnspan=2)

# canvas for the logo
canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="C:/Users/Meatsack/Desktop/100_days_of_python/password-manager-start/logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(column=1, row=0)

window.mainloop()
