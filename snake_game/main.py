from turtle import Turtle, Screen
import time  # Import time module to add delays
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.listen()
game_is_on = True
screen.setup(width=800, height=800)  # More explicit setup method for screen size
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Right", fun=snake.right)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)


screen.update()  # Initial update to draw the snake

while game_is_on:
    screen.update()
    time.sleep(0.1)  # Add a small delay to make the loop more manageable

    snake.move()

    #detect collision from food
    if snake.head.distance(food) < 15:
        scoreboard.score_up()
        snake.extend()
        food.refresh()

    #Detect collision with wall
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        scoreboard.game_over()
        game_is_on = False
    
    #Detec collision with tail
    #if head collides with any segment in tail:
    for segment in snake.segments[1:]:
        # if segment == snake.head:
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    scoreboard


screen.exitonclick()
