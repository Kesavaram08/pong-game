from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
ball = Ball()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
ball.create_ball()

right = Paddle((350, 0))
left = Paddle((-350, 0))
scoreboard = Scoreboard()


screen.listen()
screen.onkey(right.up, "Up")
screen.onkey(right.down, "Down")

screen.onkey(left.up, "w")
screen.onkey(left.down, "s")


is_on = True

while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right) < 50 and ball.xcor() > 300 or ball.distance(left) < 50 and ball.xcor() < -300:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
