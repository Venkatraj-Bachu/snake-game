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
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.goto((0, 270))

    def update_screen(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_screen()
