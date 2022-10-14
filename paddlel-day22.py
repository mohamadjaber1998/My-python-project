from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.positions = (x, y)
        self.create_paddle()

    def create_paddle(self):
        self.shape('square')
        self.shapesize(4, 1, 0)
        self.color('white')
        self.penup()
        self.goto(self.positions[0], self.positions[1])

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
