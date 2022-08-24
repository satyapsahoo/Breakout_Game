from turtle import Turtle


class Brick(Turtle):

    def __init__(self, brick_color, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color(brick_color)
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.penup()
        self.goto(x_pos, y_pos)
        self.x_range = (self.xcor() - 25, self.xcor() + 25)  # considering stretch_len as 3

