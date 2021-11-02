import turtle, time
from turtle import Screen

import bricks
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

paddle_position = (0, -270)


def setup_screen(s):
    s.setup(width=800, height=600)
    turtle.bgcolor("gray10")
    s.title("🕹 BreakOut 🕹")
    turtle.tracer(0)


def set_on_listeners():
    screen.listen()
    screen.onkeypress(paddle.start_move_left, "Left")
    screen.onkeypress(paddle.start_move_right, "Right")
    screen.onkeyrelease(paddle.stop_move, "Left")
    screen.onkeyrelease(paddle.stop_move, "Right")


screen = Screen()
setup_screen(screen)

paddle = Paddle(paddle_position)
ball = Ball()
scoreboard = Scoreboard()
bricks = bricks.load_level_2()

set_on_listeners()

game_running = True
last_frame_time = time.time()

fps = 60
time_per_frame = 1 / fps
while game_running:

    time.sleep(time.time() - last_frame_time + time_per_frame)
    inframe = ball.move()
    paddle.move()
    collided_brick = False
    for brick in bricks:
        if ball.are_colliding(brick):
            brick.hideturtle()
            bricks.remove(brick)
            scoreboard.add_score(10)
    ball.check_collision_with_paddle(paddle)
    # print(len(bricks))
    if len(bricks) < 1:
        scoreboard.flash_gameover_screen(win=True)
        game_running = False
    if not inframe:
        for brick in bricks:
            brick.hideturtle()
        scoreboard.flash_gameover_screen(win=False)
        game_running = False

    screen.update()
    last_frame_time = time.time()

screen.exitonclick()
