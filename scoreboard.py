from turtle import Turtle
ALIGMENT = 'center'
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        with open("high_score.txt", mode='r') as record_score:
            self.high_score = int(record_score.read())
        self.penup()
        self.goto(x=0, y=270)
        self.score = 0
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move = False, align = ALIGMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("high_score.txt", mode='w') as record_score:
                record_score.write(str(self.score))
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def add_score(self):
        self.score += 1
        self.update_scoreboard()


    # def gameover(self):
    #     self.goto(0 ,0)
    #     self.write(f"Game over", move = False, align = ALIGMENT, font=FONT)