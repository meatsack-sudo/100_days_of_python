from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.goto(position)
        self.color("white")
        if position[0] == -175:
            self.write(arg=f"Score: {self.l_score}", move=False, align="left", font=('Arial', 14, 'normal'))
        else:
            self.write(arg=f"Score: {self.r_score}", move=False, align="right", font=('Arial', 14, 'normal'))

    def score_up(self, side):
        self.clear()
        if side == "left":
            self.l_score += 1
            self.write(arg=f"Score: {self.l_score}", move=False, align="left", font=('Arial', 14, 'normal'))

        if side == "right":
            self.r_score += 1
            self.write(arg=f"Score: {self.r_score}", move=False, align="left", font=('Arial', 14, 'normal'))

    def game_over(self, side):
        self.penup()
        self.goto(0, 0)
        self.color("white")
        self.write(arg=f"{side} side won.", move=False, align="center", font=('Arial', 14, 'normal'))

