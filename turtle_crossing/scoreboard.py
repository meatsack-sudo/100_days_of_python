from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.round_number = 1
        self.penup()
        self.hideturtle()
        self.goto(-180, 240)
        self.color("black")
        self.display = self.write(arg=f"Round: {self.round_number}", move=False, align="center", font=FONT)

    def round_up(self):
        self.clear()
        self.round_number += 1
        self.display =self.write(arg=f"Round: {self.round_number}", move=False, align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("black")
        self.write(arg="Game Over", move=False, align="center", font=FONT)
    
