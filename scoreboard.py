from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.life = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(200, 300)
        self.write(self.score, align="center", font=("Courier", 50, "normal"))
        self.goto(-200, 300)
        self.write(self.life, align="center", font=("Courier", 50, "normal"))

    def yellow_point(self):
        self.score += 1
        self.update_scoreboard()

    def green_point(self):
        self.score += 3
        self.update_scoreboard()

    def orange_point(self):
        self.score += 5
        self.update_scoreboard()

    def red_point(self):
        self.score += 7
        self.update_scoreboard()

    def reduce_life(self):
        self.life -= 1
        self.update_scoreboard()
