import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()

car_max = []

screen.onkey(key="Up", fun=player.move)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    chance_of_car = random.randint(0, 100)

    if len(car_max) < 20:
        if chance_of_car < 25:
            for i in range(1):
                car = CarManager(scoreboard)
                car.name = f"car_{i}"
                car_max.append(car)


    for cars in car_max:
        cars.move()
        if cars.distance(player) < 15:
            scoreboard.game_over()
            game_is_on = False
        if cars.xcor() < -280:
            cars.reset()

    if player.ycor() >= 280:
        player.round_up()
        scoreboard.round_up()

screen.exitonclick()
