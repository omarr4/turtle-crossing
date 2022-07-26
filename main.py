import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.colormode(255)
screen.listen()
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.onkey(fun=player.move_forward, key='Up')
counter = 0
sleep_time = 0.1
while True:
    screen.update()
    time.sleep(sleep_time)

    counter += 1
    if counter % 4 == 0:
        car = car_manager.generate_car()

    if player.finished_level():
        scoreboard.update_level(car_manager)
        player.restart()
        sleep_time -= 0.02
        print(sleep_time)

    if not car_manager.move_cars(player):
        scoreboard.display_game_over()
        break

screen.exitonclick()