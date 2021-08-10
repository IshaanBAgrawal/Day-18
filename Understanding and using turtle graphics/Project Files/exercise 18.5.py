import turtle as t
import random

tom = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


degree_rotation = 5
tom.speed("fastest")


def draw_circle():
    global degree_rotation
    tom.color(random_color())
    tom.circle(100)
    tom.left(5)
    degree_rotation += 5


while degree_rotation != 360 and degree_rotation < 360:
    draw_circle()

screen = t.Screen()
screen.exitonclick()

