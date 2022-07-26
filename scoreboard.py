from turtle import Turtle

FONT = ('Arial', 20, 'normal')
GAME_OVER_FONT = ('Arial', 45, 'bold')
LEVEL_DISPLAY_POSITION = (-240, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(LEVEL_DISPLAY_POSITION)
        self.write(arg=f"Level: {self.level}", align='center', font=FONT)

    def update_level(self, car_manager):
        self.level += 1
        car_manager.update_level()
        self.clear()
        self.write(arg=f"Level: {self.level}", align='center', font=FONT)

    @staticmethod
    def display_game_over():
        game_over_text = Turtle()
        game_over_text.hideturtle()
        game_over_text.color("red")
        game_over_text.write(arg="GAME OVER", align='center', font=GAME_OVER_FONT)
