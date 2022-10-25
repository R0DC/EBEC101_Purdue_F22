"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 05.1 - Maze
Date: 10/09/2022

Description:
    Helps a lost turtle find its way out of a maze

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
    bgpic("maze.png")
    shape("turtle")
    color("green")
    width(5)


def main():
    #Down #1
    right(90);forward(10)
    #Left #1
    right(90);forward(60)
    #Down #2
    left(90);forward(75)
    #Left #2
    right(90);forward(50)
    #Down #3
    left(90);forward(120)
    #Left #3
    right(90);forward(25)
    #Down #4 
    left(90);forward(25)
    #Right #1
    left(90);forward(362)
    #Up #1
    left(90);forward(230)
    #Right #2
    right(90);forward(15)



"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
