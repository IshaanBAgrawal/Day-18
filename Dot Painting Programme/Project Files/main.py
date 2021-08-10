import turtle as t
from colors import colors_list
import random

tom = t.Turtle()
t.colormode(255)

tom.speed("fastest")
tom.penup()
tom.bk(225)
tom.right(90)
tom.fd(222)
tom.left(90)
tom.pendown()

for __ in range(10):
    for _ in range(10):
        tom.color(random.choice(colors_list))
        tom.dot(20)
        tom.penup()
        tom.fd(50)
    tom.left(90)
    tom.penup()
    tom.fd(50)
    tom.left(90)
    tom.fd(500)
    tom.right(180)

screen = t.Screen()
screen.exitonclick()
