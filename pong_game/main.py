from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.setup(width=800, height=600)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
l_scoreboard = Scoreboard((-175, 280))
r_scoreboard = Scoreboard((175, 280))

screen.onkey(key="Up", fun=r_paddle.go_up)
screen.onkey(key="Down", fun=r_paddle.go_down)
screen.onkey(key="w", fun=l_paddle.go_up)
screen.onkey(key="s", fun=l_paddle.go_down)

player_1_score = 0
player_2_score = 0

screen.listen()

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.ball_clear()
        l_scoreboard.score_up("left")
    
    if ball.xcor() < -380:
        ball.ball_clear()
        r_scoreboard.score_up("right")

    if l_scoreboard.l_score == 5:
        game_is_on = False
        l_scoreboard.game_over("left")

    if r_scoreboard.r_score == 5:
        game_is_on = False
        r_scoreboard.game_over("right")

    l_scoreboard
    r_scoreboard

    

    


    


screen.exitonclick()