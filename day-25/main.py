import turtle
import pandas as pd
from state import State
import time

df = pd.read_csv("50_states.csv")

states = df["state"].to_list()
score = 0
screen = turtle.Screen()
screen.title("U.S.A")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_is_on = True
state_class = State()
screen.tracer(0)
guessed_states = []
not_guessed_states = []
while len(guessed_states) < 50:
    screen.update()
    time.sleep(0.1)
    answer_state = screen.textinput(title=f"{score}/50 Guess the state", prompt="What another state's name? ").title()
    if answer_state == 'Exit':
        for state in states:
            if state not in guessed_states:
                not_guessed_states.append(state)
        csv_file_guessed = pd.DataFrame(guessed_states)
        csv_file_guessed.to_csv("My Guessed States")
        csv_file_not_guessed = pd.DataFrame(not_guessed_states)
        csv_file_not_guessed.to_csv("Not Guessed States")
        break
    if answer_state in states:
        score += 1
        state_class.goto(x=int(df[df["state"] == answer_state]["x"]), y=int(df[df["state"] == answer_state]["y"]))
        state_class.write(answer_state, move=True, align='center', font=('Arial', 8, 'normal'))
        guessed_states.append(answer_state)

