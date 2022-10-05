import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, GameOver

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
player.make_player()
car = CarManager()
over = GameOver()
score = Scoreboard()
screen.listen()
screen.onkeypress(player.up, "w")
screen.onkeypress(player.down, "s")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.level()
    car.make_car()
    car.move()
    if player.ycor() > 260:
        player.make_player()
        car.increase_speed()
        score.increase_level()

    for turtles in car.all_turtles:
        if turtles.distance(player) < 15:
            over.write_over()
            game_is_on = False

screen.exitonclick()
