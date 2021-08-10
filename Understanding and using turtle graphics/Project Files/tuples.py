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


tom.pensize(11)
tom.speed("fastest")
directions = [90, 180, 270, 0]

for _ in range(500):
    tom.color(random_color())
    tom.right(random.choice(directions))
    tom.forward(25)

print("done")

screen = t.Screen()
screen.exitonclick()
