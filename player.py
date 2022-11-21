from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.speed("fastest")
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_f(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)
        # y = self.ycor() + MOVE_DISTANCE
        # self.goto(self.xcor(), y)

    def move_l(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)
        # x = self.xcor() - MOVE_DISTANCE
        # self.goto(x, self.ycor())

    def move_r(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)
        # x = self.xcor() + MOVE_DISTANCE
        # self.goto(x, self.ycor())

    def refresh(self):
        self.goto(STARTING_POSITION)


