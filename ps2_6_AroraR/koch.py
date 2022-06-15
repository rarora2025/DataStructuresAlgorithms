"""
Description: this program creates the koch snowflake recursively
Original Author: Rahul Arora

"""

#importing turtle
import turtle

#defining presets for turtle, making it reset in top-left corner
t = turtle.Turtle()
t.pu()
t.forward(-200)
t.left(90)
t.forward(100)
t.right(90)
t.pd()

#recursive function that builds koch snowflake, takes in parameter for how complex you want the snowflake
def build_koch(iterations):
     #base case
    if (iterations == 0):
        t.forward(50)
        return
     
     #recursion....
    build_koch(iterations-1)
    t.left(60)
    build_koch(iterations-1)
    t.right(120)
    build_koch(iterations-1)
    t.left(60)
    build_koch(iterations-1)
    #60-120-60 triangle

#calling koch, in for loop to repeat it and make a full snowflake
for i in range(3):    
        build_koch(2)
        t.right(120)

