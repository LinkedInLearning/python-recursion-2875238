"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""

import turtle

DEPTH = 2


def draw_triangle(points, color, tur):
    tur.fillcolor(color)
    tur.up()
    tur.goto(points[0][0], points[0][1])
    tur.down()
    tur.begin_fill()
    tur.goto(points[1][0], points[1][1])
    tur.goto(points[2][0], points[2][1])
    tur.goto(points[0][0], points[0][1])
    tur.end_fill()


def get_mid_point(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinski(points, depth, tur):
    draw_triangle(points, available_colours[depth], tur)
    if depth > 0:
        # From bottom left vertex
        sierpinski([points[0],
                    get_mid_point(points[0], points[1]),
                    get_mid_point(points[0], points[2])],
                   depth - 1, tur)
        # From apex
        sierpinski([points[1],
                    get_mid_point(points[0], points[1]),
                    get_mid_point(points[1], points[2])],
                   depth - 1, tur)
        # From bottom right vertex
        sierpinski([points[2],
                    get_mid_point(points[2], points[1]),
                    get_mid_point(points[0], points[2])],
                   depth - 1, tur)


if __name__ == '__main__':
    available_colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    my_turtle = turtle.Turtle()
    # my_turtle.hideturtle()
    my_turtle.color('white')
    my_turtle.shape('turtle')
    my_turtle.pensize(5)
    my_turtle.speed(1)  # 1 is good for following along
    screen = turtle.Screen()
    screen.setup(600, 600)
    screen.title('Sierpinski Triangle')
    screen.bgcolor('black')
    vertices = [[-200, -100], [0, 200], [200, -100]]

    sierpinski(vertices, DEPTH, my_turtle)
    my_turtle.hideturtle()

    turtle.done()
