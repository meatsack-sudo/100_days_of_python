from tkinter import *

FONT_NAME = "Courier"



# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    pass

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    pass

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#website label and entry
website_label = Label(text="Website:", font=(FONT_NAME, 16))
website_entry = Entry(width=35)

website_label.grid(column=0, row=1)
website_entry.grid(column=1, row=1, columnspan=2)

#email/username label and entry
email_username_label = Label(text="Email/Username:", font=(FONT_NAME, 16))
email_username_entry = Entry(width=35)

email_username_label.grid(column=0, row=2)
email_username_entry.grid(column=1, row=2, columnspan=2)

#password label, entry, button
password_label = Label(text="Password:", font=(FONT_NAME, 16))
password_entry = Entry(width=21)
gen_password_button = Button(text="Generate Password", command=generate_password)

password_label.grid(column=0, row=3)
password_entry.grid(column=1, row=3)
gen_password_button.grid(column=2, row=3)

#add button
add_button = Button(text="Add", width=36, command=add_password)

add_button.grid(column=1, row=4, columnspan=2)

canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="C:/Users/Meatsack/Desktop/100_days_of_python/password-manager-start/logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(column=1, row=0)

window.mainloop()