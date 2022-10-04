"""
    meteo.py
    assignment: lab 4
    language: python3
    author: YOUR NAME GOES HERE

"""

import turtle as t

def background():
    """
    load the background for the meteo weather map and
    set up the turtle window size and position in the screen's upper left.
    """
    screen = t.Screen()
    screen.bgpic("simland.png")
    t.setup(1100, 650, 0, 0)
    

def draw_rectangle(length, width):
    """
    draws a rectangle with the given length and width
    :param length:
    :param width:
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.left(90)
    pass # YOUR CODE GOES HERE



def snowflake(length=8):
    """
    draws a 6-arms snowflake
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up, width = 1
    """
    t.width(2)
    t.pendown()
    t.color("blue")
    for i in range(0,6):
        t.forward(length)
        t.backward(length)
        t.right(360/6)
    t.penup()
    t.width(1)

def draw_sun(r=16):
    """
    draws yellow sun
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up, width = 1
    """
    t.pencolor("yellow")
    t.fillcolor("yellow")
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def draw_rain(size=16):
    """
    draws 5 rain drops
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up, width = 1
     """
    t.penup()
    t.color("blue")
    t.back(size*2)
    t.right(90)
    t.forward(size*1.2)
    t.width(2)
    t.left(90)
    for i in range(5):
        t.pendown()
        t.left(80)
        t.forward(size)
        t.back(size)
        t.right(80)
        t.penup()
        t.forward(size/3)
    t.width(1)
    pass # YOUR CODE AND DOCSTRING  GOES HERE
    
def draw_cloud(r=16):
    """
    draws a pretty cloud as a combination of: 1 circle of radius r,
    2 circles of radius r/2 and a rectangle 2r x r
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up, pencolor black
    """
    t.pencolor("blue")
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(r/2)
    draw_rectangle(2.2*r, r)
    t.forward(1.2*r)
    t.circle(r)
    t.forward(1.2*r)
    t.circle(r/2)
    t.end_fill()
    t.pencolor("black")
    

def draw_snow(size=8):
    """
    draws 3 snowflakes and a cloud
    :pre-conditions: turtle faces east, pen up
    :post-conditions: turtle faces east, pen up
    """
    draw_cloud(2*size)
    t.up()
    t.backward(4*size)
    t.right(90)
    t.forward(size)
    t.left(90)
    snowflake(size)
    t.right(45)
    t.forward(2*size)
    t.left(45)
    snowflake(size)
    t.left(45)
    t.forward(2*size)
    t.right(45)
    snowflake(size)
    

if __name__ == "__main__":
    background()
    t.done()
