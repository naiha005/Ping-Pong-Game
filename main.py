from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")

# Slipting screen into two parts
turtle = Turtle()
turtle.color('white')
turtle.pensize(5)
turtle.penup()
turtle.goto(0, -280)
turtle.setheading(90)
turtle.pendown()

for _ in range(280):
    turtle.forward(20)
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()


screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

is_game_on = True
while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect collision with top wall
    if ball.ycor() >= 280 or ball.ycor() < -280:
        # ball needs to bounce
        ball.bounce_y()

    # Detect collision with left and right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if r_paddle missed the ball
    if ball.xcor() > 370:
        ball.reset_ball()
        scoreboard.l_point()

    # Detect if the l_paddle missed the ball
    if ball.xcor() < - 370:
        ball.reset_ball()
        scoreboard.r_point()





screen.exitonclick()


