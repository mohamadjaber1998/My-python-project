from turtle import Turtle


class Scoreboard(Turtle,):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.position = position
        self.create_scoreboard(self.position)

    def create_scoreboard(self, position):
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.color('white')
        self.write(self.score, True, align='center', font=('Arial', 25, 'normal'))
