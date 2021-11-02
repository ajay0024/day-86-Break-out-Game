import math
import turtle
from turtle import Turtle, Vec2D

SPEED = 6


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("AliceBlue")
        self.penup()
        self.shape("circle")
        initial_normal = Vec2D(1, 1) * (1 / abs(Vec2D(1, 1)))
        self.speed = SPEED * initial_normal

    def move(self):
        if self.ycor() >= 290:  # if bounce
            self.bounce_y()  # invert y speed
        if abs(self.xcor()) >= 390:  # if bounce
            self.bounce_x()  # invert x speed
        new_position = self.pos() + self.speed
        self.goto(new_position)
        if self.ycor() <= -310:
            return False
        return True

    def bounce_y(self):
        self.speed = Vec2D(self.speed[0], -self.speed[1])

    def bounce_x(self):
        self.speed = Vec2D(-self.speed[0], self.speed[1])

    def start_again(self):
        self.goto(0, 0)

    def are_colliding(self, brick):
        if brick.pos()[0] + brick.b_width / 2 >= self.pos()[0] - 10 and brick.pos()[0] - brick.b_width / 2 <= \
                self.pos()[0] + 10 and brick.pos()[1] + brick.b_height / 2 > self.pos()[1] - 10 and brick.pos()[1] - \
                brick.b_height / 2 <= self.pos()[1] + 10:
            collision_location = self.pos() - brick.pos()
            normal_corner = brick.corner
            normal_coll_loc = collision_location * (1 / abs(collision_location))
            coll_direction = ""
            if abs(normal_coll_loc[0]) < normal_corner[0]:
                if collision_location[1] < 0:
                    coll_direction = "B"
                else:
                    coll_direction = "T"
            else:
                if collision_location[0] < 0:
                    coll_direction = "L"
                else:
                    coll_direction = "R"

            original_speed = (self.speed[0], self.speed[1])
            if original_speed[0] < 0 and original_speed[1] > 0:
                if coll_direction == "R" or coll_direction == "T":
                    self.bounce_x()
                else:
                    self.bounce_y()
            if original_speed[0] > 0 and original_speed[1] > 0:
                if coll_direction == "L" or coll_direction == "T":
                    self.bounce_x()
                else:
                    self.bounce_y()
            if original_speed[0] < 0 and original_speed[1] < 0:
                if coll_direction == "R" or coll_direction == "B":
                    self.bounce_x()
                else:
                    self.bounce_y()
            if original_speed[0] > 0 and original_speed[1] < 0:
                if coll_direction == "L" or coll_direction == "B":
                    self.bounce_x()
                else:
                    self.bounce_y()
            return True
        else:
            return False

    def check_collision_with_paddle(self, paddle):
        if paddle.pos()[0] + paddle.p_width / 2 >= self.pos()[0] - 10 and paddle.pos()[0] - paddle.p_width / 2 <= \
                self.pos()[0] + 10 and paddle.pos()[1] + paddle.p_height / 2 > self.pos()[1] - 10 and paddle.pos()[1] - \
                paddle.p_height / 2 <= self.pos()[1] + 10:
            collision_location = self.pos() - paddle.pos()
            normal_corner = paddle.corner
            normal_coll_loc = collision_location * (1 / abs(collision_location))
            coll_direction = ""
            if abs(normal_coll_loc[0]) < normal_corner[0]:
                if collision_location[1] > 0:
                    coll_direction = "T"
            if coll_direction == "T":
                proportional_distance = collision_location[0] / (paddle.p_width / 2 + 10)
                deflection_power = 1  # in radians
                deflection = deflection_power * proportional_distance
                deflection_angle=1.5708-deflection
                # print(f"New Angle : {math.degrees(deflection_angle)}")
                self.speed = SPEED * Vec2D(math.cos(deflection_angle), abs(math.sin(deflection_angle)))
                # print("\n")
