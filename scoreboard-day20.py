from turtle import Turtle


class ScoreBored(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(0, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def end_game(self):
        self.goto(0, 0)
        self.write("Game Over.", move=False, align='center', font=('Arial', 20, 'normal'))
