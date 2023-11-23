from turtle import Turtle
ALIGMENT = 'center'
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.score = 0
        self.update_scoreboard()
        self.hideturtle()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", move = False, align = ALIGMENT, font=FONT)


    def add_score(self):
        self.score += 1
        self.update_scoreboard()


    def gameover(self):
        self.goto(0 ,0)
        self.write(f"Game over", move = False, align = ALIGMENT, font=FONT)