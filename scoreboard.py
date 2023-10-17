from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto((0, 270))

    def update_screen(self):
        self.clear()
        self.write(f"Score: {self.score}", align='center', font=FONT)
