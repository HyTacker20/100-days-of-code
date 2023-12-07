from turtle import Turtle


class Scoreboard:
    def __init__(self):
        self.score = 0
        self.scoreboard = Turtle()
        self.scoreboard.goto(0, 270)
        self.scoreboard.color('white')
        self.scoreboard.shape("blank")
        self.scoreboard.write(f"Score: {self.score}", align='center', font=('Arial', 16, 'bold'))

    def add_score(self):
        self.score += 1
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.score}", align='center', font=('Arial', 16, 'bold'))

    def game_over(self):
        self.scoreboard = Turtle()
        self.scoreboard.goto(0, 0)
        self.scoreboard.color('white')
        self.scoreboard.shape("blank")
        self.scoreboard.write("GAME OVER!", align='center', font=('Arial', 25, 'bold'))
