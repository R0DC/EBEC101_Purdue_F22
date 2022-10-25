"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 10/13/2022

Description:
    Draws the individual letters used in the
    random_vowels_rcalistr.py program

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

#Draws the letter a
def draw_a():
    pendown()
    circle(25,360)
    circle(25,90)
    forward(25)
    backward(50)
    right(90)
    penup()
    forward(25)

#Draws the letter e
def draw_e():
    pendown()
    circle(25,45)
    circle(25,-45)
    circle(25,-270)
    left(90)
    forward(50)
    penup()
    backward(50)
    right(90)
    forward(12.5)
    right(90)

#Draws the letter i
def draw_i():
    pendown()
    left(90)
    forward(50)
    penup()
    forward(15)
    dot(10)
    backward(75)
    right(90)
    forward(50)

#Draws the letter o
def draw_o():
    pendown()
    circle(25,360)
    penup()
    forward(25)

#Draws the letter u
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
    forward(25)


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    pass

"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
