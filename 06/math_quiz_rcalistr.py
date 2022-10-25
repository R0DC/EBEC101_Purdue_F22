"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 06.1 - Math Quiz
Date: 10/09/2022

Description:
    A simple math quiz program that asks the user to compute
    the sum of the two numbers displayed

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

"""Write new functions below this line (starting with unit 4)."""
def random_number(nr_dig):
    return random.randrange(10**(nr_dig-1),10**nr_dig) #Generate a number between two orders of magnitude


def main():
    nr1 = random_number(2) #Generates first number
    nr2 = random_number(3) #Generates second number
    total = nr1 + nr2 #Sum the two numbers
    print(f"{nr1:5.0f}")
    print(f"+{nr2:4.0f}")
    print("-----")
    print("= ",end='')
    user_input = float(input('')) #Ask for user input
    if user_input == total:
        print('Correct -- Good Work!')
    else:
        print(f'Incorrect. The correct answer is {total:.0f}.')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
