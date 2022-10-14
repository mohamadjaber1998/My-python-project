import turtle
from turtle import Turtle, Screen
import random
color_list = [(226, 231, 235), (54, 108, 149), (225, 201, 108), (134, 85, 58), (229, 235, 234), (224, 141, 62),
              (197, 144, 171), (143, 180, 206), (137, 82, 106), (210, 90, 68), (232, 226, 194), (188, 78, 122),
              (69, 101, 86), (132, 183, 132), (65, 156, 86), (137, 132, 74), (48, 155, 195), (183, 191, 202),
              (232, 221, 225), (58, 47, 41), (47, 59, 96), (38, 44, 64), (106, 46, 54), (41, 55, 48),
              (12, 104, 95), (118, 125, 145), (182, 194, 199), (215, 176, 187), (223, 178, 168), (54, 45, 52),
              (179, 199, 184), (133, 41, 39), (76, 63, 49)]

x_value = -200
y_value = -100


def paint():
    color_rgb = random.choice(color_list)
    tim.pencolor(color_rgb)
    tim.pendown()
    tim.forward(1)
    tim.penup()
    tim.forward(40)




turtle.colormode(255)
tim = Turtle()
tim.penup()
tim.setx(x_value)
tim.sety(y_value)


tim.pensize(15)
for i in range(10):
    for j in range(10):
        tim.setpos(x_value + 40, y_value + 40)
        paint()




screen = Screen()
screen.exitonclick()