from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        self.level = 0
        super().__init__()
        self.up()
        self.goto(-280, 250)
        self.color('black')
        self.shape("blank")
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def add_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color('black')
        self.shape("blank")
        self.write("GAME OVER!", align='center', font=FONT)

