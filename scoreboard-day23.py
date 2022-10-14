from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.create_scoreboard()

    def create_scoreboard(self):
        self.hideturtle()
        self.penup()
        self.goto(-240, 270)
        self.write(f"Level: {self.level}", True, align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over.", True, align='center', font=FONT)

    def increased_level(self):
        self.clear()
        self.goto(-240, 270)
        self.write(f"Level: {self.level}", True, align='center', font=FONT)