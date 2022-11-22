"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 11.1 - Dice
Date: 11/20/2022

Description:
    The program defines the Dice object,
    which rolls the specified number of dice given
    the number of dice sides and prints the results.

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
import random

class Dice():
    def __init__(self,sides):
        self.sides=sides
        self.rolls = []

    def roll(self): #Generates a random number between 1 and however many sides the die has
        return random.randint(1,self.sides)

    def n_rolls(self,num): #Generates dice rolls specified by input
        print(f"Rolling a {self.sides} sided dice {num} times: ", end = '')
        for _ in range(num):
            if _ < num-1:
                print(self.roll(),end=', ')
            else:
                print(self.roll(),end='')
        print()

"""Write new functions below this line (starting with unit 4)."""


def main():
    six_sided = Dice(6)
    ten_sided = Dice(10)
    twenty_sided = Dice(20)
    six_sided.n_rolls(10)
    ten_sided.n_rolls(10)
    twenty_sided.n_rolls(10)


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
