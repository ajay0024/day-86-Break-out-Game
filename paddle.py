from turtle import Turtle
import turtle


class Paddle(Turtle):
    p_width = 100
    p_height = 20
    corner = turtle.Vec2D(p_width / 2, p_height / 2) * (1 / abs(turtle.Vec2D(p_width / 2, p_height / 2)))

    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("DeepSkyBlue3")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=self.p_height/20, stretch_len=self.p_width/20)
        # self.left(90)
        self.goto(pos)
        self.direction="left"
        self.speed=0

    def move(self):
        if self.direction=="left":
            self.back(self.speed)
        else:
            self.forward(self.speed)
        pass

    def start_move_left(self):
        self.speed=10
        self.direction="left"

    def start_move_right(self):
        self.speed = 10
        self.direction = "right"

    def stop_move(self):
        self.speed=0
