import turtle 
from turtle2gif import turtle2gif

pen = turtle.Turtle() 
pen.hideturtle()

def curve(): 
    for i in range(200): 
        pen.right(1) 
        pen.forward(1) 

def draw(): 
    pen.begin_fill() 
    pen.left(140) 
    pen.forward(113) 
    curve() 
    pen.left(120) 
    curve() 
    pen.forward(112) 

turtle2gif.convert(draw, 5, 10)
