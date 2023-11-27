import turtle
import random
# setup the window with a background colour
window = turtle.Screen()

# assign a name to your turtle
elsa = turtle.Turtle()
elsa.speed(0)

# create one branch of the snowflake
def branch():
    for i in range(3):
        for i in range(3):
            elsa.forward(30)
            elsa.backward(30)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(30)
        elsa.left(45)
    elsa.right(90) 
    elsa.forward(90)

for i in range(8):
    branch()
    elsa.left(45)

