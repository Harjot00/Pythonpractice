from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(0.6, 0.6)
        self.penup()
        self.goto(random.randint(-280,280), random.randint(-280, 280))

    def refresh(self):
        self.goto(random.randint(-280,280), random.randint(-280, 280))


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 0)