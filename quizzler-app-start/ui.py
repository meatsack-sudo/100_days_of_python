from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0, )
        self.canvas.grid(column=0, row=1, columnspan=2, padx=50, pady=50)
        
        self.score_text = Label(text="Score:" + " 0", fg="white", bg=THEME_COLOR)
        self.score_text.grid(column=1, row=0)

        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some question text", fill=THEME_COLOR, font=("Arial", 20, "italic"))

        true_image = PhotoImage(file="C:/Users/Meatsack/Desktop/python training/100_days_of_python/quizzler-app-start/images/true.png")
        self.true_button = Button(image=true_image, command=self.true_button_select)
        self.true_button.grid(column=0, row=2)

        false_image = PhotoImage(file="C:/Users/Meatsack/Desktop/python training/100_days_of_python/quizzler-app-start/images/false.png"    )
        self.false_button = Button(image=false_image, command=self.false_button_select)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score_text.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")



    def true_button_select(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_button_select(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)