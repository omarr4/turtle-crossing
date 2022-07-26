from turtle import Turtle
import random

START_POSITION_X = 320  # for now
END_POSITION_X = -340
CAR_SPAWN_MIN_RANGE_Y = -260
CAR_SPAWN_MAX_RANGE_Y = 275
CAR_SPAWN_MIN_RANGE_X = 300
CAR_SPAWN_MAX_RANGE_X = 500
SPEED_INCREMENT = 1
STARTING_SPEED = 9


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed_forward = STARTING_SPEED

    def generate_car(self):
        car = Turtle(shape='square')
        car.penup()
        car.goto(self.random_position_rightside())
        car.color(self.get_random_color())
        car.setheading(180)
        car.shapesize(stretch_len=2)

        self.all_cars.append(car)
        return car

    def move_cars(self, player):
        for car in self.all_cars:
            car.forward(self.speed_forward)
            self.check_remove_car(car)
            if player.collision(car):
                print("meowww")
                return False
        return True

    def check_remove_car(self, car):
        if car.xcor() <= END_POSITION_X:
            car.hideturtle()
            self.all_cars.remove(car)

    def update_level(self):
        self.speed_forward += SPEED_INCREMENT

    @staticmethod
    def get_random_color():
        return (
            random.randint(0, 245),
            random.randint(0, 245),
            random.randint(0, 245)
        )

    @staticmethod
    def random_position_rightside():
        return (random.randint(CAR_SPAWN_MIN_RANGE_X, CAR_SPAWN_MAX_RANGE_X),
                random.randint(CAR_SPAWN_MIN_RANGE_Y, CAR_SPAWN_MAX_RANGE_Y))
