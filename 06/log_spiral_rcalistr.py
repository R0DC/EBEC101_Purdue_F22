"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 06.4 - Log Spiral
Date: MM/DD/YYYY

Description:
    Computes the x and y coordinates for a log
    spiral and draws the spiral.

Contributors:
    odion Calistru, rcalistr@purdue.edu [repeat for each]

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
import math

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(5)


def main():
    penup()
    a = 4 #First constant
    b = 0.22 #Second constant
    for theta in range(0,360*3+1):
        theta_rads = math.radians(theta) #Converts degrees to radians
        x = a * math.exp(b*theta_rads)*math.cos(theta_rads) #Computes x position
        y = a * math.exp(b*theta_rads)*math.sin(theta_rads) #Computes y positions
        goto(x,y) #Draws the spiral
        pendown()


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
