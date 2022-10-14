from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake = []
        self.values_tuple = [(0, 0), (-20, 0), (-40, 0)]
        self.create_snake()

    def create_snake(self):
        for position in self.values_tuple:
            new_turtle = Turtle(shape='square')
            new_turtle.color('white')
            new_turtle.penup()
            new_turtle.goto(position)
            self.snake.append(new_turtle)

    def move(self):
        for seg in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg - 1].xcor()
            new_y = self.snake[seg - 1].ycor()
            self.snake[seg].goto(new_x, new_y)
        self.snake[0].forward(10)

    def turn_up(self):
        if not self.snake[0].heading() == 270:
            self.snake[0].setheading(90)

    def turn_down(self):
        if not self.snake[0].heading() == 90:
            self.snake[0].setheading(270)

    def turn_left(self):
        if not self.snake[0].heading() == 0:
            self.snake[0].setheading(180)

    def turn_right(self):
        if not self.snake[0].heading() == 180:
            self.snake[0].setheading(0)

    def create_turtle(self):
        new_turtle = Turtle(shape='square')
        new_turtle.color('white')
        new_turtle.penup()
        return new_turtle
