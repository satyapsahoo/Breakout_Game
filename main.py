from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from brick import Brick
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=800)
screen.title("Breakout Masters")
screen.tracer(0)

paddle = Paddle((0, -350))
ball = Ball()
scoreboard = Scoreboard()
hit_detect = 30

# Create and position the bricks in the game window. Each brick is a turtle.
y = 50
brick_yellow_list = []
for row in range(0, 2):
    for x in range(-240, 280, 80):
        brick_yellow = Brick("yellow", x, y)
        brick_yellow_list.append(brick_yellow)
    y += 30

brick_green_list = []
for row in range(0, 2):
    for x in range(-240, 280, 80):
        brick_green = Brick("green", x, y)
        brick_green_list.append(brick_green)
    y += 30

brick_orange_list = []
for row in range(0, 2):
    for x in range(-240, 280, 80):
        brick_orange = Brick("orange", x, y)
        brick_orange_list.append(brick_orange)
    y += 30

brick_red_list = []
for row in range(0, 2):
    for x in range(-240, 280, 80):
        brick_red = Brick("red", x, y)
        brick_red_list.append(brick_red)
    y += 30

brick_list = brick_yellow_list + brick_green_list + brick_orange_list + brick_red_list

# Move the paddle with keyboard
screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

# Run the game till the paddle misses the ball 3 times
while scoreboard.life > 0:
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 380:
        ball.bounce_y()

    if ball.xcor() < -280 or ball.xcor() > 280:
        ball.bounce_x()

    # Detect collision with paddle
    if ball.distance(paddle) < hit_detect and ball.ycor() < -320:
        ball.bounce_y()

    # Detect Paddle misses
    if ball.ycor() < -380:
        ball.reset_position()
        scoreboard.reduce_life()
        time.sleep(1)

    # Detect Brick Hit
    for brick in brick_list:
        if ball.distance(brick) < hit_detect:
            # Identify the color of brick and update scoreboard
            if brick in brick_yellow_list:
                scoreboard.yellow_point()
            elif brick in brick_green_list:
                scoreboard.green_point()
            elif brick in brick_orange_list:
                scoreboard.orange_point()
            elif brick in brick_red_list:
                scoreboard.red_point()

            # Identify the bounce direction if the ball hit the face or the edge of the brick
            if ball.xcor() in brick.x_range:
                ball.bounce_x()
            else:
                ball.bounce_y()
            brick.hideturtle()  # Hide the turtle where the ball hit
            brick_list.remove(brick)  # Remove the turtle from the brick list

screen.exitonclick()
