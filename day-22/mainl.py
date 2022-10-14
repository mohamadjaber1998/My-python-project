from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)
ball = Ball()
r_scoreboard = Scoreboard((50, 250))
l_scoreboard = Scoreboard((-50, 250))
screen.listen()
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

screen.onkeypress(fun=r_paddle.move_up, key='Up')
screen.onkeypress(fun=r_paddle.move_down, key='Down')
screen.onkeypress(fun=l_paddle.move_up, key='w')
screen.onkeypress(fun=l_paddle.move_down, key='s')

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.05)
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_x()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_y()

screen.exitonclick()
