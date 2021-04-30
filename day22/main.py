from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

ball = Ball()
scoreboard = Scoreboard()
paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
screen = Screen()

screen.bgcolor("black")
screen.setup(width= 800, height= 600)
screen.title("Pong")
screen.tracer(0)

screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.xcor() > 320 and ball.distance(paddle_r) < 50 or ball.xcor() < -320 and ball.distance(paddle_l) < 50:
        ball.bounce_x()
    if ball.xcor() > 330:
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -330:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
