"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 05.3 - Star pattern
Date: 10/09/2022

Description:
    Draws star-shaped patterns given number of points

Contributors:
    Rodion Calistr, rcalistr@purdue.edu [repeat for each]

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
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()

def main():
    nr_points = int(input("Input number of points: ")) #Ask for nr of points
    speed(0.6)
    angle_A = 360 / nr_points #Compute inner angle
    angle_B = 2 * angle_A #Compute concave angle
    side_length = 60
    setheading(-90+angle_A) #Set direction
    color('black','pink') #Set color of shape
    begin_fill()
    #Draw the shape
    for n in range(0,nr_points):
        forward(side_length)
        right(angle_A)
        backward(side_length)
        left(angle_B)
    end_fill()




"""Do not change anything below this line."""
if __name__ == '__main__':
    start()
    main()
    done()
