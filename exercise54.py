# This is where Exercise 5.4 goes
# Name: Elizabeth Tenorio

import math
from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()


def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    fd(t, length*n)
    lt(t, angle)
    draw(t, length, n-1)
    rt(t, 2*angle)
    draw(t, length, n-1)
    lt(t, angle)
    bk(t, length*n)

# This is the code to construct a Koch curve
#def koch(turtle, len):
#    for i in range(4):
#        fd(bob, 100)
#        lt(bob)

draw(bob, 4, 50)
