"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 10/13/2022

Description:
    Pulls the vowels from the vowels.py program,
    then puts them in a list, randomizes them 
    and draws them

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

"""Import modules below this line (starting with unit 6)."""
from turtle import *
import vowels #Imports the vowels program
import random


"""Write new functions below this line (starting with unit 4)."""


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
    x = -220
    y = -30
    letters = [vowels.draw_a, vowels.draw_e, vowels.draw_i, vowels.draw_o, vowels.draw_u] #Puts all of the letters functions inside an list
    var = random.sample(letters,5) #Randomizes the order of the letters
    #Loops through the letters, drawing each letter
    for n in range(len(letters)):
        var[n]()
        x += 100
        setheading(0)
        goto(x,y)





"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
