from aluLib import *
from random import randrange                                       #Import randrange to randomize numbers within a certain range

#Window/ Screen Dimensions
window_width = 1300
window_height = 700

#Randomize y-coordinate position of the left and right paddle
y_left = randrange(0, 550)
y_right = randrange(0, 550)

#Define the center of the circle (both x and y coordinates) to be at the center of the screen
x_cord = window_width / 2
y_cord = window_height / 2

#Initial ball velocities along the x and y axis
x_velocity = +4
y_velocity = -3

#Initial score count. Increases by +1 when the ball hits a paddle
score = 0

#Radius of the ball
ball_radius = 15

#Initial game state
game = False

#Draw the paddles and give them a red color
def paddles():
    disable_stroke()
    clear()

    set_fill_color(1, 0, 0)
    draw_rectangle(0, y_left, 20, 150) 

    set_fill_color(1, 0, 0)
    draw_rectangle(1280, y_right, 20, 150)


#Moving the paddles up and down when keys a, z, k and m are pressed. Code to restrict paddle movement to within the game window
def move_paddles():
    global y_right, y_left

    #to set limits to left paddle movement to within the window
    if is_key_pressed("z"):
        if y_left >= 550:
            y_left = 550
        else:
            y_left += 10
            paddles()


    elif is_key_pressed("a"):
        if y_left <= 0:
            y_left = 0
        else:
            y_left -= 10
            paddles()



    #to set limits to right paddle movement to within the window
    if is_key_pressed("m"):
        if y_right >= 550:
            y_right = 550
        else:
            y_right += 10
            paddles()


    elif is_key_pressed("k"):
        if y_right <= 0:
            y_right = 0
        else:
            y_right -= 10
            paddles()

#Set game status to true when space bar is clicked. This starts the game
def game_start():
    global game

    if is_key_pressed(" "):
        game = True
        return True

#Restart the game after the game has ended or when the space bar key is pressed
def restart():
    global x_cord, y_cord, game, x_velocity, y_velocity, score

    if is_key_pressed(" "):
        x_cord = window_width / 2
        y_cord = window_height / 2
        game = True
        x_velocity = +4
        y_velocity = -3
        score = 0

#Draw the ball and give it a blue color
def ball():
    disable_stroke()

    set_fill_color(0, 0, 1)
    draw_circle(x_cord, y_cord, ball_radius)

#Set the ball in motion automatically when the game starts i.e space bar key is pressed
def move_ball():
    global x_cord, y_cord

    if game == True:           #Set to: if game starts      Set to if "space key" is pressed set game_start to true
        x_cord += x_velocity
        y_cord += y_velocity
        ball()

#Display a "game over" message and the score count
def game_over1():
    global game

    enable_stroke()
    set_stroke_color(0, 0, 0)
    set_font_size(60)
    draw_text("Game Over", 450, 250)
    set_font_size(40)
    draw_text("SCORE: " + str(score), 540, 300)
    game = False

#Check for collision of the ball with the right paddle and return a boolean
def collision_right():
    return x_cord + ball_radius > 1272 and ((y_cord + ball_radius < y_right + 175) and (y_cord + ball_radius > y_right - 15 ))

#Check for collision of the ball with the left paddle and return a boolean
def collision_left():
    return x_cord - ball_radius < 21 and ((y_cord + ball_radius < y_left + 175) and (y_cord + ball_radius > y_left - 15))

#Check if ball has missed the right paddle then return a boolean
def miss_paddle_right():
    return x_cord + ball_radius > 1315 and not ((y_cord + ball_radius  < y_right + 165) and (y_cord + ball_radius > y_right ))

#Check if ball has missed the left paddle then return a boolean
def miss_paddle_left():
    return x_cord - ball_radius < -15 and not ((y_cord + ball_radius < y_left + 165) and (y_cord + ball_radius > y_left ))

#Check if the ball has hit a horizontal wall, both at the top and at the bottom
def horizontal_collision():
    return y_cord + ball_radius > 700 or (y_cord + ball_radius < 30)

#Bounce the ball when it hits a paddle or the horizontal walls. Displays a "game over" message and the score count when the ball misses a paddle and hits a vertical wall
def bounce_ball():
    global  x_velocity, y_velocity, score

    if collision_right() == True:
        x_velocity *= -1
        score += 1

    elif miss_paddle_right() == True:
        game_over1()
        x_velocity *= 0
        y_velocity *= 0

    elif collision_left() == True:
         x_velocity *= -1
         score += 1

    elif miss_paddle_left() == True:
         game_over1()
         x_velocity *= 0
         y_velocity *= 0

    elif horizontal_collision() == True:
         y_velocity *= -1

def main():

    game_start()
    paddles()
    move_paddles()
    ball()
    bounce_ball()
    move_ball()
    restart()

    #Quit the game and close the game window if "q" is pressed
    if is_key_pressed("q"):
        cs1_quit()

start_graphics(main, framerate= 100, width = window_width, height = window_height )