from tkinter import *
import math
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
MARKS = ""
timer = None

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global MARKS
    global timer
    #Count minutes logic
    count_min = math.floor(count / 60)
    if count_min == 0:
        count_min = "00"
    elif count_min <= 9:
        count_min = "0" + str(count_min)
    
    #Count seconds logic    
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec <= 9:
        count_sec = "0" + str(count_sec)

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if REPS in [2, 4, 6, 8]:
            checkmark_label.config()
            MARKS += "✔"
        checkmark_label.config(text=MARKS)


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if REPS % 8 == 0:
        count_down(4)
        timer_label.config(text="Long Break", fg=RED)
    elif REPS % 2 == 0:
        count_down(3)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(5)
        timer_label.config(text="Work", fg=GREEN)
    

# ---------------------------- TIMER RESET ------------------------------- # 



def reset_timer():
    global MARKS
    global REPS
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    REPS = 0
    MARKS = ""


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

#Picture and counter
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="C:/Users/Meatsack/Desktop/100_days_of_python/pomodoro-start/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)



#Checkmarks
checkmark_label = Label(font=(FONT_NAME, 16, "bold"), bg=YELLOW, fg=GREEN)
checkmark_label.grid(column=1, row=3)

#Timer text
timer_label = Label(text="Timer", font=(FONT_NAME, 40, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)



#Buttons
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)


#use grid not pack



window.mainloop()