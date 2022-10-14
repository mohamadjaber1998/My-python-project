from turtle import Turtle, Screen
import random

screen = Screen()
turtle_list = []
color_list = ['red', 'orange', 'blue', 'purple', 'yellow', 'green']
new_y = -100


def random_step(object):
    object.fd(random.randint(1, 5))


for color in color_list:
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(color)
    turtle_list.append(new_turtle)


screen.setup(width=600, height=400)
user_input = screen.textinput(title="make a bet", prompt="choose a color to bet: ")

for turtle in turtle_list:
    new_y += 25
    turtle.goto(x=-275, y=new_y)

game_still_playing = True
while game_still_playing:

    for turtle in turtle_list:
        random_step(turtle)
        if turtle.pos()[0] >= 275:
            game_still_playing = False
            winner_turtle = turtle
            break
if winner_turtle.color()[0] == user_input:
    print("you win")
else:
    print(f"you lose, the winner turtle is: {winner_turtle.color()[0]}")
screen.listen()
screen.exitonclick()
