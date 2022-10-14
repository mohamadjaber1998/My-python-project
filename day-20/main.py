from turtle import Screen
from food import Food
import time
from Snake import Snake
from scoreboard import ScoreBored

screen = Screen()
snake = Snake()
food = Food()
scoreboard = ScoreBored()
screen.listen()
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake game')

screen.tracer(0)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.snake[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        scoreboard.update_score()
        new_turtle = snake.create_turtle()
        snake.snake.append(new_turtle)
    if snake.snake[0].xcor() > 280 or snake.snake[0].xcor() < -280\
            or snake.snake[0].ycor() > 280 or snake.snake[0].ycor() < -280:

        game_is_on = False
        scoreboard.end_game()

    for seg in snake.snake[1:]:
        if snake.snake[0].distance(seg) < 5:
            game_is_on = False
            scoreboard.end_game()

screen.exitonclick()
