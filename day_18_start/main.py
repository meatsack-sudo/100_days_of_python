from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("red")
screen = Screen()
screen.colormode(255)
keep_going = True


# tim.forward(100)
# tim.right(90)

#Drawing a square
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

#tim.pencolor(screen.bgcolor())

#Dashed line - 50 forward - 10 blank - 50 forward
# for _ in range(10):
#     tim.forward(20)
#     tim.penup()
#     tim.forward(5)
#     tim.pendown()
#     tim.forward(20)


# for sides in range(4, 10):
#     tim.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     for side in range(sides):
#         tim.forward(100)
#         tim.right(360 / sides)

def random_direction(random_number):
    if random_number == 1:
        return "forward"
    if random_number == 2:
        return "backward"
    if random_number == 3:
        return "right"
    if random_number == 4:
        return "left"
    
def random_color():
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return(color)

tim.pensize(10)
tim.speed("fastest")
    
# while keep_going:
#     if tim.xcor() > screen.window_width() / 2 or tim.ycor() > screen.window_height() / 2:
#         break
#     coinflip = random.randint(0, 1)
#     if coinflip == 0:
#         tim.left(90)
#     else:
#         tim.right(90)
#     tim.color(random_color())
#     tim.forward(25)

for _ in range(200):
    tim.circle(180)
    tim.color(random_color())
    tim.right(10)

# direction = random_direction(random.randint(1, 4))
# print(direction)





























screen.exitonclick()