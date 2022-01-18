from turtle import Turtle,Screen
import random
import time

import scoreboard
from Snake import Snake
from food import Food, Wall
from scoreboard import Score
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
wall = Wall()
Snake = Snake()
ball = Food()
screen.listen()
screen.onkeypress(Snake.up, "Up")
screen.onkeypress(Snake.down, "Down")
screen.onkeypress(Snake.left, "Left")
screen.onkeypress(Snake.right, "Right")
Score_board = Score()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    Snake.move()

    if Snake.head.distance(ball) < 15:
        ball.refresh()
        Score_board.increase_score()
        Snake.update()

    if Snake.head.xcor() > 280 or Snake.head.xcor() < -300 or Snake.head.ycor() < -280 or Snake.head.ycor() > 280:
        screen.bye()

    for segment in Snake.segment[1:]:

        if Snake.head.distance(segment) < 10:
            screen.bye()
screen.exitonclick()