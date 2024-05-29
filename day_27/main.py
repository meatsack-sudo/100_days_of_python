from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def button_clicked():
    global click_count
    click_count += 1
    my_label.config(text=f"Times clicked: {click_count}")
    new_label.config(text="Button got clicked.")
    another_label.config(text=f"{input.get()}")

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
#my_label.place(x=0, y=200)
#Can't used grid with pack
my_label.grid(column=0, row=0)
my_label.config(text="New Text")
new_label = Label(font=("Arial", 24, "bold"))
new_label.grid(column=4, row=1)
another_label = Label(font=("Arial", 24, "bold"))
another_label.grid(column=1, row=0)

#my_label["text"] = "New Text"

#Button
button = Button(text="Click me", command=button_clicked)
button.grid(column=2, row=0)

#entry
input = Entry(width=10)
input.grid(column=3, row=0)
print(input.get())



click_count = 0









window.mainloop()