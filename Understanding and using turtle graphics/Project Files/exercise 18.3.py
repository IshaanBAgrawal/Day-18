from turtle import Turtle, Screen
import random

color = ["chartreuse", "DeepPink", "DarkViolet", "cyan", "aquamarine", "goldenrod1", "DeepSkyBlue2", "green",
         "GreenYellow", "LightSeaGreen", "magenta", "OrangeRed", "LimeGreen", "purple", 'navy']
tom = Turtle()
tom.sides = 3
while tom.sides <= 10:
    for _ in range(tom.sides):
        tom.right(360 / tom.sides)
        tom.forward(100)
    tom.color(random.choice(color))
    tom.sides += 1

screen = Screen()
screen.exitonclick()
