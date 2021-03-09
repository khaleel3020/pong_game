from turtle import Screen
from ball import Ball
from pandle import Pandle
import time
from scoreboard import Scoreboard
screen = Screen()
screen.tracer(0)
screen.setup(width=1200, height=900)
screen.bgcolor('black')
screen.title('Pong')
ball = Ball((0, 0))
r_paddle = Pandle((580, 0))
l_paddle = Pandle((-580, 0))
score = Scoreboard()
screen.listen()
screen.onkey(key='Up', fun=r_paddle.up)
screen.onkey(key='Down', fun=r_paddle.down)
screen.onkey(key='w', fun=l_paddle.up)
screen.onkey(key='s', fun=l_paddle.down)

is_game_on = True
while is_game_on:

    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    if -430 > ball.ycor() or ball.ycor() > 430:
        ball.bounce()
    if ball.distance(r_paddle) < 60 and ball.xcor() > 550 \
            or ball.distance(l_paddle) < 60 and ball.xcor() < -550:
        ball.touch()
    if ball.xcor() > 590:
        ball.reset()
        score.l_point()

    if ball.xcor() < -590:
        ball.reset()
        score.r_point()


screen.exitonclick()