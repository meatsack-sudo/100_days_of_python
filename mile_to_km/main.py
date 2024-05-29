from tkinter import *

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=10)
window.config(padx=20, pady=20)

def calculate():
        km = int(user_input.get()) * 1.609
        result_label.config(text=f"{km}", background="white")
    # else:
    #     result_label.config(text="Please input a number")

#Labels
miles_label = Label(text="Miles", font=("Arial", 16))
is_equal_label = Label(text="is equal to", font=("Arial", 16))
km_label = Label(text="KM", font=("Arial", 16))
result_label = Label(text="0", font=("Arial", 16), background="white", width=5)


miles_label.grid(column=2, row=0)
is_equal_label.grid(column=0, row=1)
km_label.grid(column=2, row=1)
result_label.grid(column=1, row=1)

#Button
button = Button(text="Calculate", command=calculate)
button.grid(column=1, row=2)

#Entry
user_input = Entry(width=10)
user_input.grid(column=1, row=0)


window.mainloop()