from turtle import Turtle, Screen

tom = Turtle()
tom.penup()
tom.bk(400)
tom.pendown()
for _ in range(1, 51):
    tom.penup()
    tom.forward(10)
    tom.pendown()
    tom.forward(10)


screen = Screen()
screen.exitonclick()
