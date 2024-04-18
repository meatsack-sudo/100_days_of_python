import turtle
import prettytable
# import another_module

# print(another_module.another_variable)

# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.fillcolor("blue")
# timmy.forward(100)

# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

table = prettytable.PrettyTable()

table.field_names = ["Pokemon Name", "Type"]
table.add_rows(
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"],
    ]
)
table.align = "l"
print(table)