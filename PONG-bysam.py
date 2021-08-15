#Author:Samantha Melgar
#Date: January 30, 2021
#Purpose: Create Pong

from cs1lib import*
from random import randint

pressed_a = False
pressed_z = False
pressed_k = False
pressed_m = False
pressed_q = False
pressed_space = False

lx = 0 #left paddle x position
ly = 0
rx = 400 #right paddle x position
ry = 320

LENGTH = 80
WIDTH = 20

WINDOW_X = 400
WINDOW_Y = 400

#ball starting position
ball_x = 200
ball_y = 200
BALL_R = 10

velocity_x = randint(-5,5)
velocity_y = randint(-5,5)


def draw_paddles():
    global ball_x, bally_y, BALL_R, WIDTH, LENGTH, lx, ly, rx, ry
    #draw background
    set_clear_color(0,0,0) #black
    clear()

    #draw left paddle
    set_fill_color(1, 1, 1) #white
    draw_rectangle(0, ly, 20, 80)
    #draw right paddle
    draw_rectangle(380, ry, 20, 80)

    #draw pong ball
    set_fill_color(1, 1, 1) #white
    draw_circle(ball_x, ball_y, BALL_R)

    ball_move() #reappaears in the frames
    ball_hits_wall()
    ball_meets_paddle()

def keydown(key):
    global pressed_a, pressed_z, pressed_k, pressed_m, pressed_q, ly, ry, ball_x, ball_y, BALL_R, velocity_y, velocity_x, pressed_space

    if key == "a":
        pressed_a = True
    if key == "z":
        pressed_z = True
    if key == "k":
        pressed_k = True
    if key == "m":
        pressed_m = True

    if key == "q":
        pressed_q = True

    if key == " ":
        pressed_space = True


    # Left Paddle movement
    if pressed_a:  # is pressed_a true?
        ly -= 25
    if pressed_z:
        ly += 25

    # Right Paddle movement:
    if pressed_k:
        ry -= 25
    if pressed_m:
        ry += 25

    if velocity_x == 0:
        velocity_x = 3
    if velocity_y == 0:
        velocity_y = 3

    # quit the game

    if pressed_q:
        quit()

    #bounds
    if ly <= 0:
        ly = 0

    if ly >= 320:
        ly = 320

    if ry <= 0:
        y2 = 0

    if ry >= 320:
        ry = 320

    if pressed_space:
        ly = 0
        ry = 320
        ball_x = 200
        ball_y = 200
        BALL_R = 10
        velocity_x = randint(-5, 5)
        velocity_y = randint(-5, 5)

def key_release(key):
    global pressed_a, pressed_z, pressed_k, pressed_m, pressed_space
    if key == "a":
        pressed_a = False
    if key == "z":
        pressed_z = False
    if key == "k":
        pressed_k = False
    if key == "m":
        pressed_m = False
    if key == " ":
        pressed_space = False



def ball_move():
    global ball_x, ball_y, velocity_x, velocity_y
    ball_x += velocity_x
    ball_y += velocity_y

def ball_hits_wall():
    global rx, ry, ball_x, ball_y,BALL_R, velocity_x, velocity_y,ly
    #restart as soon as it hits the wall
    if ball_x >= 400:
        ly = 0
        ry = 320
        ball_x = 200
        ball_y = 200
        BALL_R = 10
        velocity_x = randint(-5, 5)
        velocity_y = randint(-5, 5)

    if ball_x <= 0:
        ly = 0
        ry = 320
        ball_x = 200
        ball_y = 200
        BALL_R = 10
        velocity_x = randint(-5, 5)
        velocity_y = randint(-5, 5)

def ball_meets_paddle():
    global velocity_x, velocity_y, ly, ry, lx, rx, ball_x, ball_y, BALL_R, LENGTH, WIDTH

    if ball_y - BALL_R <= 0: #hits walls
        velocity_y *= -1

    if ball_y + BALL_R >= 400:
        velocity_y *= -1

    if ly + 80 >= ball_y and ball_y >= ly and ball_x - BALL_R <= 20:
        velocity_x *= -1

    if ry + 80 >= ball_y and ball_y >= ry and ball_x - BALL_R >= 360: 
        velocity_x *= -1



start_graphics(draw_paddles, key_press=keydown, key_release=key_release)
