from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open('data.txt', 'r+') as f:
            score = f.readline()
            if score == '':
                print(str(self.high_score))
                f.write(str(self.high_score))
            else:
                self.high_score = int(score)
        self.up()
        self.goto(0, 270)
        self.color('white')
        self.shape("blank")
        self.write(f"Score: {self.score} High score: {self.high_score}", align='center', font=('Arial', 16, 'bold'))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align='center', font=('Arial', 16, 'bold'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as f:
                f.write(str(self.high_score))
        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align='center', font=('Arial', 16, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.color('white')
        self.shape("blank")
        self.write("GAME OVER!", align='center', font=('Arial', 25, 'bold'))
