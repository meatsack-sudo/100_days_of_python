from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("/home/meatsack/Desktop/python_100_days/100_days_of_python/snake_game/data.txt") as data:
            self.highscore = int(data.read())
        self.score = 0
        print(self.highscore)
        self.hideturtle()
        self.goto(0, 380)
        self.color("white")
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Arial', 14, 'normal'))

    def score_up(self):
        self.clear()
        self.score += 1
        self.write(arg=f"Score: {self.score} High Score: {self.highscore}", move=False, align="center", font=('Arial', 14, 'normal'))

    def reset(self):
        if self.score > int(self.highscore):
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.score_up()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.color("white")
    #     self.write(arg="Game Over", move=False, align="center", font=('Arial', 14, 'normal'))

