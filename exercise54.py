# This is where Exercise 5.4 goes
# Name: Elizabeth Tenorio

from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()

# This is the code to construct a Koch curve
# x = length
def koch(t, x):
  if x < 3:
    fd(t, x)
    return
  else:
    koch(t, x/3)
    lt(t, 60)
    koch(t, x/3)
    rt(t, 120)
    koch(t, x/3)
    lt(t, 60)
    koch(t, x/3)

#koch(bob, 500)

#Make a snowflake with n koch curves
def snowflake(t, x, n):
  if n <=0:
    return
  else:
    koch(t, x)
    n = n - 1
    snowflake(t, x, n)
#snowflake(bob, 500, 3)

#Cesaro fractal
# x = length
def cf(t, x):
  if x < 3:
    fd(t, x)
    return
  else:
    cf(t, x/3)
    lt(t, 85)
    cf(t, x/3)
    rt(t, 170)
    cf(t, x/3)
    lt(t, 85)
    cf(t, x/3)

#cf(bob, 500)

#Make a Cesaro snowflake
def csnowflake(t, x, n):
  if n <=0:
    return
  else:
    cf(t, x)
    n = n - 1
    csnowflake(t, x, n)
#csnowflake(bob, 100, 3)

wait_for_user()

