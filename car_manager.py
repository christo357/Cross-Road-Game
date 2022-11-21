from turtle import Turtle
import random as rm

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10



class CarManager(Turtle):
    def __init__(self, ):
        super().__init__()
        self.color(rm.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=.75,stretch_len=1.75)
        self.penup()
        self.goto(350, rm.randint(-15, 15)*10)
        self.motion()

    def motion(self):
        # while self.xcor()>-400:
        #     x = self.xcor() - STARTING_MOVE_DISTANCE
        #     y = self.ycor()
        #     self.goto(x, y)
        self.backward(STARTING_MOVE_DISTANCE)


