#Random dot
import colorgram
from turtle import *
import turtle
import random
rgb=[]
# Extract 6 colors from an image.
colors = colorgram.extract('image.jpg', 200)
for c in colors:
    r=c.rgb.r
    g = c.rgb.g
    b=c.rgb.b
    rgb.append((r,g,b))


print(len(rgb))
screen=Screen()
timy=Turtle()
a=-10
b=0
turtle.colormode(255)
for g in range(50):
    a=a+10
    timy.penup()
    timy.goto(-40,a)
    for h in range(10):
        timy.penup()
        timy.forward(20)
        timy.dot(10)
        timy.color(random.choice(rgb))



screen.exitonclick()
