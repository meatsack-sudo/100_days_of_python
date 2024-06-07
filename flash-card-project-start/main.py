from tkinter import *
from tkinter import messagebox
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "arial"

# ---------------------------- DATA SETUP ------------------------------- #

#This would be better accomplished with OS library and checking for the file.
try:
    with open("C:/Users/Meatsack/Desktop/100_days_of_python/flash-card-project-start/data/words_to_learn.csv", "r"):
       df = pd.read_csv("C:/Users/Meatsack/Desktop/100_days_of_python/flash-card-project-start/data/words_to_learn.csv")
 
except FileNotFoundError:
    df = pd.read_csv("C:/Users/Meatsack/Desktop/100_days_of_python/flash-card-project-start/data/french_words.csv")

#df = pd.read_csv("C:/Users/Meatsack/Desktop/100_days_of_python/flash-card-project-start/data/french_words.csv")
word_dict = df.to_dict(orient="records")

# ---------------------------- ANSWER HANDLING ------------------------------- #

flashcard_number_start = random.randint(0, 101)

def next_card():
    global flip_timer
    global word_dict
    global flashcard_number_start
    window.after_cancel(flip_timer)
    flashcard_number = random.randint(0, 101)
    canvas.itemconfig(dictionary_word, text=f"{word_dict[flashcard_number]["French"]}", font=(FONT_NAME, 60, "bold"))
    canvas.itemconfig(language_label, text="French")
    canvas.itemconfig(flashcard_image, image=flashcard_front_image)
    flashcard_number_start = flashcard_number
    flip_timer = window.after(3000, flip_card)

def answer_right():
    word_dict.remove(word_dict[flashcard_number_start])
    #print(word_dict(["English"][flashcard_number_start]))
    updated_word_dict = pd.DataFrame(word_dict)
    updated_word_dict.to_csv("C:/Users/Meatsack/Desktop/100_days_of_python/flash-card-project-start/data/words_to_learn.csv", index=False)
    next_card()


def answer_wrong():
    next_card()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

#Buttons
right_button_image = PhotoImage(file="C:/Users/Meatsack/Desktop/100_days_of_python/flash-card-project-start/images/right.png")
wrong_button_image = PhotoImage(file="C:/Users/Meatsack/Desktop/100_days_of_python/flash-card-project-start/images/wrong.png")

right_canvas = Canvas(width=50, height=50)
wrong_canvas = Canvas(width=50, height=50)

right_button = Button(image=right_button_image, command=answer_right)
wrong_button = Button(image=wrong_button_image, command=answer_wrong)

right_button.grid(column=0, row=1)
wrong_button.grid(column=1, row=1)

def flip_card():
    canvas.itemconfig(flashcard_image, image=flashcard_back_image)
    canvas.itemconfig(language_label, text="English")
    canvas.itemconfig(dictionary_word, text=f"{word_dict[flashcard_number_start]["English"]}")

# canvas for the logo

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard_front_image = PhotoImage(file="C:/Users/Meatsack/Desktop/100_days_of_python/flash-card-project-start/images/card_front.png")
flashcard_back_image = PhotoImage(file="C:/Users/Meatsack/Desktop/100_days_of_python/flash-card-project-start/images/card_back.png")


flashcard_image = canvas.create_image(400, 263, image=flashcard_front_image)
language_label = canvas.create_text(400, 150, text=f"French", font=(FONT_NAME, 40, "italic"))
dictionary_word = canvas.create_text(400, 263, text=f"{word_dict[flashcard_number_start]["French"]}", font=(FONT_NAME, 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

flip_timer = window.after(3000, flip_card)

window.mainloop()