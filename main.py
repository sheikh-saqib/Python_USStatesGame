import turtle

import pandas as pandas

from map_states import Map_States

screen = turtle.Screen()

screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
map_states = Map_States()
data = pandas.read_csv("50_states.csv")
states_list = data.state.tolist()
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(f"{len(guessed_state)}/50 States Correct", "What's another state's name").title()

    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states_list:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_row = data[data.state == answer_state]
        t.goto(int(state_row.x), int(state_row.y))
        t.write(state_row.state.item())
