import time
import random as rm
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
# car = CarManager()

screen.listen()
screen.onkey(fun = player.move_f, key = "space")
screen.onkey(fun = player.move_f, key = "Up")
screen.onkey(fun = player.move_l, key = "Left")
screen.onkey(fun = player.move_r, key = "Right")

car_list =[]

screen.update()

game_is_on = True
j=0
t=0.1
while game_is_on:
    time.sleep(t)
    j += 1
    if j%8==0:
        new_car = CarManager()
        car_list.append(new_car)
        j=0
    for car in car_list:
        car.motion()
        if car.xcor() < -300:
            car_list.remove(car)
        if -20 < (car.ycor() - player.ycor()) < 22 and -30 < (player.xcor()-car.xcor()) < 30:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > 200:
        player.refresh()
        scoreboard.level_increment()
        t *= .6





    screen.update()

screen.exitonclick()
