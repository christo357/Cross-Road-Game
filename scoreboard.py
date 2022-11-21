from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 0
        self.hideturtle()
        self.goto(-200, 250)
        self.update()

    def update(self):
        self.clear()
        self.write("LEVEL : "+str(self.level), align="center", font=FONT)

    def level_increment(self):
        self.level += 1
        self.update()

    def game_over(self):
        self.goto(0, 200)
        self.color("red")
        self.write("GAME OVER!!",align="center",font=("Courier", 44, "normal"))



