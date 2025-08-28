from turtle import *

import pandas
import pandas as pd

screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)  # Register the shape (useful for turtles)
screen.bgpic(image)     # Set as background image


#get coord on click
def mouse_click_coord(x,y):
    print(x,y)
onscreenclick(mouse_click_coord)

data = pd.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Correct", "What is a state name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        print(missing_states)
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_name = data[data.state == answer_state]
        t.goto(state_name.x.iloc[0], state_name.y.iloc[0])
        t.write(state_name.state.iloc[0])







