from turtle import Turtle

SPEED = (10, 10)


class GameObject(Turtle):
    def __init__(self, pos=(0, 0), color="AliceBlue", shape="square", updatespeed="fast",width=20,height=20):
        super().__init__()
        self.color = color
        self.penup()
        self.shape(shape)
        self.speed(updatespeed)
        self.shapesize(stretch_wid=width/ 20, stretch_len=height / 20)
        self.right(90)
        self.goto(pos)

    def set_speed(self, speed=(10, 10)):
        self.speed = list(SPEED)

    def move(self):
        if abs(self.ycor()) >= 290:  # if bounce
            self.speed[1] *= -1  # invert y speed
        if abs(self.xcor()) >= 390:  # if bounce
            self.speed[0] *= -1  # invert y speed
        new_position = self.pos() + self.speed
        self.goto(new_position)

    def bounce_y(self):
        self.speed[0] *= -1
        pass

    def start_again(self):
        print("start again")
        self.goto(0, 0)
        self.bounce_x()

    def move(self):
        if self.direction=="forward":
            self.back(self.speed)
        else:
            self.forward(self.speed)
        pass

    def start_move_left(self):
        self.speed=10
        self.direction="backward"

    def start_move_right(self):
        self.speed = 10
        self.direction = "forward"

    def stop_move(self):
        self.speed=0
