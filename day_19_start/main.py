from turtle import Turtle, Screen
import random

is_race_on = False
# tim = Turtle(shape="turtle")
screen = Screen()

# def move_forward():
#     tim.forward(5)

# def move_backward():
#     tim.back(5)

# def turn_right():
#     tim.right(5)

# def turn_left():
#     tim.left(5)

# def clear():
#     tim.clear()


# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="d", fun=turn_right)
# screen.onkey(key="a", fun=turn_left)
# screen.onkey(key="c", fun=clear)

screen.setup(height=400, width=500)
colors = ["red", "blue", "teal", "purple", "green", "orange"]
user_bet = screen.textinput("Bet Input", prompt="Which turtle will win the race? Enter a color from the list: " + str(colors))


turtles = {}

for color in colors:
    y_coord_add = int(screen.window_height() - 300 - (25 * colors.index(color)))
    turtles[f"turtle_{color}"] = Turtle(shape="turtle")
    turtles[f"turtle_{color}"].penup()
    turtles[f"turtle_{color}"].color(color)
    turtles[f"turtle_{color}"].goto(-230, y_coord_add)

if user_bet:
    is_race_on = True

while is_race_on:
    for key, turtle in turtles.items():
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet.lower():
                print(f"You've won. The winning turtle is {user_bet}")
            else:
                print(f"You've lost. The winning turtle was {winning_color}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)



#tim.penup()
#tim.goto(-230, -100)


screen.exitonclick()