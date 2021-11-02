from turtle import Turtle
import turtle


class Brick(Turtle):
    b_width = 40
    b_height = 20
    corner=turtle.Vec2D(b_width / 2, b_height / 2) * (1 / abs(turtle.Vec2D(b_width / 2, b_height / 2)))

    def __init__(self, pos, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.penup()
        self.speed("slow")
        self.shapesize(stretch_wid=self.b_width / 20, stretch_len=self.b_height / 20)
        self.right(90)
        self.goto(pos)


def make_line(brick_locations, start_pos, number, brick_width, brick_gap, color):
    for i in range(number):
        brick_locations.append(((start_pos[0] + i * (brick_width + brick_gap), start_pos[1]), color))


def load_level_0():
    brick_locations=[]
    bricks=[]
    make_line(brick_locations, (-350, 250), 15, Brick.b_width, 10, color="DeepPink")
    make_line(brick_locations, (-350, 220), 15, Brick.b_width, 10, color="DarkSeaGreen1")
    make_line(brick_locations, (-350, 190), 15, Brick.b_width, 10, color="DarkOliveGreen1")

    make_line(brick_locations, (-350, 150), 15, Brick.b_width, 10, color="DeepPink")
    make_line(brick_locations, (-350, 120), 15, Brick.b_width, 10, color="DarkSeaGreen1")
    make_line(brick_locations, (-350, 90), 15, Brick.b_width, 10, color="DarkOliveGreen1")

    for i in brick_locations:
        bricks.append(Brick(i[0], i[1]))

    return bricks

def load_level_1():
    brick_locations=[]
    bricks=[]
    make_line(brick_locations, (-350, 250), 15, Brick.b_width, 10, color="DeepPink")
    make_line(brick_locations, (-350, 210), 15, Brick.b_width, 10, color="DarkSeaGreen1")
    make_line(brick_locations, (-350, 170), 15, Brick.b_width, 10, color="DarkOliveGreen1")

    make_line(brick_locations, (-350, 130), 15, Brick.b_width, 10, color="DeepPink")
    make_line(brick_locations, (-350, 90), 15, Brick.b_width, 10, color="DarkSeaGreen1")
    make_line(brick_locations, (-350, 50), 15, Brick.b_width, 10, color="DarkOliveGreen1")

    for i in brick_locations:
        bricks.append(Brick(i[0], i[1]))

    return bricks

def load_level_2():
    brick_locations=[]
    bricks=[]
    make_line(brick_locations, (-350, 250), 15, Brick.b_width, 10, color="DeepPink")
    make_line(brick_locations, (-350, 210), 15, Brick.b_width, 10, color="DarkSeaGreen1")

    make_line(brick_locations, (-350, 90), 15, Brick.b_width, 10, color="DarkSeaGreen1")
    make_line(brick_locations, (-350, 50), 15, Brick.b_width, 10, color="DeepPink")

    for i in brick_locations:
        bricks.append(Brick(i[0], i[1]))

    return bricks