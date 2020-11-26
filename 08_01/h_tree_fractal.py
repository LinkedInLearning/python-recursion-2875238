"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""
import turtle

SPEED = 5
BG_COLOR = "blue"
PEN_COLOR = "lightgreen"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
DRAWING_WIDTH = 700
DRAWING_HEIGHT = 700
PEN_WIDTH = 5
TITLE = "H-Tree Fractal with Python Turtle Graphics"
FRACTAL_DEPTH = 2


def draw_line(tur, pos1, pos2):
    # print("Drawing from", pos1, "to", pos2)  # Uncomment for tracing the algorithm.
    tur.penup()
    tur.goto(pos1[0], pos1[1])
    tur.pendown()
    tur.goto(pos2[0], pos2[1])


def recursive_draw(tur, x, y, width, height, count):
    draw_line(
        tur,
        [x + width * 0.25, y + height // 2],
        [x + width * 0.75, y + height // 2],
    )
    draw_line(
        tur,
        [x + width * 0.25, y + (height * 0.5) // 2],
        [x + width * 0.25, y + (height * 1.5) // 2],
    )
    draw_line(
        tur,
        [x + width * 0.75, y + (height * 0.5) // 2],
        [x + width * 0.75, y + (height * 1.5) // 2],
    )

    if count <= 0:  # The base case
        return
    else:  # The recursive step
        count -= 1
        # Top left
        recursive_draw(tur, x, y, width // 2, height // 2, count)
        # Top right
        recursive_draw(tur, x + width // 2, y, width // 2, height // 2, count)
        # Bottom left
        recursive_draw(tur, x, y + width // 2, width // 2, height // 2, count)
        # Bottom right
        recursive_draw(tur, x + width // 2, y + width // 2, width // 2, height // 2, count)


if __name__ == "__main__":
    # Screen setup
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title(TITLE)
    screen.bgcolor(BG_COLOR)

    # Turtle artist (pen) setup
    artist = turtle.Turtle()
    artist.hideturtle()
    artist.pensize(PEN_WIDTH)
    artist.color(PEN_COLOR)
    artist.speed(SPEED)

    # Initial call to recursive draw function
    recursive_draw(artist, - DRAWING_WIDTH / 2, - DRAWING_HEIGHT / 2, DRAWING_WIDTH, DRAWING_HEIGHT, FRACTAL_DEPTH)

    # Every Python Turtle program needs this (or an equivalent) to work correctly.
    turtle.done()
