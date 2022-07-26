from turtle import Turtle

START_POSITION = (0, -280)
FINISH_LINE_Y = 300
MOVE_SPEED = 10
COLLISION_DISTANCE = 23


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.restart()
        self.shape("turtle")
        self.color('green')
        self.setheading(90)

    def move_forward(self):
        self.forward(MOVE_SPEED)

    def collision(self, car):
        return self.distance(car) < COLLISION_DISTANCE

    def finished_level(self):
        return self.ycor() >= FINISH_LINE_Y

    def restart(self):
        self.goto(START_POSITION)

