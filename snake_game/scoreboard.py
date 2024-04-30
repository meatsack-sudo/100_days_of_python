from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(0, 380)
        self.color("white")
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Arial', 14, 'normal'))

    def score_up(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Arial', 14, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write(arg="Game Over", move=False, align="center", font=('Arial', 14, 'normal'))

