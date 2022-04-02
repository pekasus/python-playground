import turtle
import random
from turtle import Screen

# tr = turtle.Screen()
tr = Screen()
tr.bgcolor('black')
tr.colormode(255)
turtle.speed(0)
for x in range(500):
    r,b,g=random.randint(0,255),random.randint(0,255),random.randint(0,255)
    turtle.pencolor(r,g,b)
    turtle.fd(x+50)
    turtle.rt(91)
tr.exitonclick()