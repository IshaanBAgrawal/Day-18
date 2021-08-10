from turtle import Turtle, Screen
import random

tom = Turtle()

color = ["chartreuse", "DeepPink", "DarkViolet", "cyan", "aquamarine", "goldenrod1", "DeepSkyBlue2", "green",
         "GreenYellow", "LightSeaGreen", "magenta", "OrangeRed", "LimeGreen", "purple", 'navy']

tom.shape("turtle")
tom.pensize(11)
tom.speed("fastest")
directions = [90, 180, 270, 0]

for _ in range(500):
    tom.color(random.choice(color))
    tom.right(random.choice(directions))
    tom.forward(25)

screen = Screen()
screen.exitonclick()
