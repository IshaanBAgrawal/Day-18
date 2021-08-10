from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape('turtle')
turtle.color("magenta")

for _ in range(1, 5):
    turtle.fd(100)
    turtle.left(90)

screen = Screen()
screen.exitonclick()
