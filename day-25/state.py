from turtle import Turtle


class State(Turtle):
    def __init__(self):
        super().__init__()
        self.create_state()

    def create_state(self):
        self.penup()
        self.hideturtle()
