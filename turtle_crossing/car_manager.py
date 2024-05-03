from turtle import Turtle
import random
from scoreboard import Scoreboard

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
#scoreboard = Scoreboard()


class CarManager(Turtle):
    
    def __init__(self, scoreboard):
        super().__init__()
        self.scoreboard = scoreboard
        self.shape("square")
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(280, random.randint(-280, 280))
        self.setheading(180)

    
    
    def move(self):
        if self.scoreboard.round_number == 1:
            new_x = self.xcor() - (STARTING_MOVE_DISTANCE)
        else:
            new_x = self.xcor() - (STARTING_MOVE_DISTANCE) - (MOVE_INCREMENT)
        y = self.ycor()
        self.goto(new_x, y)
        pass

    def reset(self):
        self.goto(280, random.randint(-280, 280))


