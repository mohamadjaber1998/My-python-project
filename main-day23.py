import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player1 = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(key='Up', fun=player1.move)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()
    for car in car_manager.cars:
        if car.distance(player1) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player1.distance(0, 300) < 40:
        scoreboard.level += 1
        scoreboard.increased_level()
        player1.goto(0, -280)
        car_manager.increase_level()
screen.exitonclick()
