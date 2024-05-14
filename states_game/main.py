import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "states_game\\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("states_game\\50_states.csv")

# Your solution
# correct_states = []
# def check_answer(state):
#     if state.title() in data.state.values:
#         guess_correct(state)


# def guess_correct(state):
#     correct_states.append(state)
#     turtle_state = turtle.Turtle()
#     turtle_state.hideturtle()
#     turtle_state.penup()
#     turtle_state.color("black")
#     turtle_state.goto(get_x(state), get_y(state))
#     turtle_state.write(f"{state}", move=True, align="center")


# def get_x(state):
#     filtered_data = data[data["state"] == state]
#     x_coord = filtered_data['x'].iloc[0]
#     return x_coord

# def get_y(state):
#     filtered_data = data[data["state"] == state.title()]
#     y_coord = filtered_data['y'].iloc[0]
#     return y_coord

# turtle.shape(image)


# while len(correct_states) < 50:
#     answer_state = screen.textinput(title=f"{len(correct_states)}/50 States Correct", prompt="What's another state's name?")
#     check_answer(answer_state.title())

guessed_states = []
all_states = data.state.to_list()
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")

    if answer_state.lower() == "exit":
        forgot_states = [state for state in all_states if state not in guessed_states]
        # forgot_states = []
        # for state in all_states:
        #     if state.lower() not in guessed_states:
        #         forgot_states.append(state)
        data_frame = pandas.DataFrame(forgot_states)
        data_frame.to_csv("states_game\\forgotten_states.csv", index=False)
        break
    
        

    if answer_state.title() in all_states:
        guessed_states.append(answer_state.lower())
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == answer_state.title()]
        t.goto(int(state_data['x'].iloc[0]), int(state_data['y'].iloc[0]))
        t.write(answer_state)
        #This line would also work
        #t.write(state_data.state.item())

#states_to_learn.csv



turtle.mainloop()