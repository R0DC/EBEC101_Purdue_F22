"""
Author: Rodion Calistr, rcalistr@purdue.edu
Assignment: 05.2 - Square Spiral
Date: 10/09/2022

Description:
    Draws a square spiral

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
    setup(564, 564)
    width(5)


def main():
    side = 12 #Define side length
    setheading(45) #Set turtle orientation
    #Draw the spiral
    for n in range(1,30):
        forward(side)
        right(90)
        side += 12


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
