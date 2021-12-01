# https://docs.python.org/3/library/turtle.html

import turtle
import time

timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("blue")

my_screen = turtle.Screen()

time.sleep(1)
for i in range(0,4):
    timmy.forward(100)
    timmy.right(90)

timmy.left(90)

for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

my_screen.exitonclick()

