from turtle import Turtle, Screen
import colorgram
import random

colors = colorgram.extract('image.jpg', 36)

color_list = []

for color in range(len(colors)):
    color_sample = colors[color]
    rgb = color_sample.rgb
    rgb_unnamed = (rgb[0], rgb[1], rgb[2])
    color_list.append(rgb_unnamed)

print(len(color_list))

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.pensize(5)
keep_going = True
count = 0

while count < 11:
    for spot in range(10):
        tim.dot(None, color_list[random.randint(0, len(color_list) - 1)])
        tim.penup()
        tim.forward(15)
        tim.pendown()
    y_position = tim.ycor()
    x_position = tim.xcor()
    position = tim.pos()
    print(position)
    tim.teleport(0, y_position + 12)
    count += 1































screen.exitonclick()
