from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(300, 260)
        self.write(f"Score : {self.score}", align="center", font=("Courier", 20, "normal"))

    def add_score(self, i):
        self.score += i
        self.update_score()

    def flash_gameover_screen(self, win):
        self.goto(0, 0)
        if win:
            self.color("SeaGreen1")
            self.write(f"You Completed the Game !\nYour score : {self.score}", align="center", font=("Courier", 30, "normal"))
        else:
            self.color("red1")
            self.write(f"You Lost !\nYour score : {self.score}", align="center", font=("Courier", 50, "normal"))
