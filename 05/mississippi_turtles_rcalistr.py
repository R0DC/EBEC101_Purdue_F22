"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 05.4 - Mississippi Turtles
Date: 10/14/2022

Description:
    Draws the words "Mississippi turtles" 
    after the letters have been defined

Contributors:
    Rodion Calistru, rcalistr@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""
from turtle import *

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    color("purple")

def draw_e():
    forward(30)
    pendown()
    circle(30,45)
    circle(30,-45)
    circle(30,-270)
    left(90)
    forward(60)
    penup()
    backward(60)
    left(90)
    forward(30)
    left(90)
    penup()

def draw_i():
    pendown()
    left(90)
    forward(50)
    penup()
    forward(15)
    dot(10)
    backward(65)
    right(90)
    penup()

def draw_l():
    pendown()
    left(90)
    forward(100)
    backward(100)
    right(90)
    penup()

def draw_M():
    pendown()
    left(90)
    forward(100)
    circle(-20,180)
    forward(100)
    backward(100)
    left(180)
    circle(-20,180)
    forward(100)
    left(90)
    penup()

def draw_p():
    pendown()
    left(90)
    forward(50)
    backward(100)
    forward(50)
    right(90)
    penup()
    forward(25)
    pendown()
    circle(25,360)
    penup()
    forward(25)

def draw_r():
    pendown()
    left(90)
    forward(50)
    right(90)
    penup()
    forward(20)
    right(180)
    pendown()
    circle(20,90)
    penup()
    forward(40)
    left(90)
    forward(20)

def draw_s():
    pendown()
    forward(10)
    circle(15,180)
    circle(-15,180)
    forward(10)
    penup()
    right(90)
    forward(60)
    left(90)

def draw_t():
    forward(30)
    pendown()
    left(90)
    forward(100)
    backward(30)
    right(90)
    backward(30)
    forward(60)
    penup()
    right(90)
    forward(70)
    left(90)

def draw_u():
    setheading(90)
    forward(50)
    setheading(0)
    pendown()
    right(90)
    forward(25)
    circle(25,180)
    forward(25)
    backward(50)
    right(90)
    penup()


def main():
    """After these lines, call your letter drawing functions
    as needed to draw the words "Mississippi turtles".
    """
    penup()
    goto(-240, 40)
    mississippi = [draw_M, draw_i, draw_s, draw_s, draw_i, draw_s, draw_s, draw_i, draw_p, draw_p, draw_i] #Puts 'Mississippi' in a list
    turtles = [draw_t, draw_u, draw_r, draw_t, draw_l, draw_e, draw_s] #Puts 'turtles' in a list
    #Draws the words
    for n in range(len(mississippi)):
        mississippi[n]()
        forward(20)
    goto(-240,-140)
    for m in range(len(turtles)):
        turtles[m]()
        forward(20)


"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
