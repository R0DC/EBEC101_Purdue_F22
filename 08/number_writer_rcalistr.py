"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 08.4 - Number Writer
Date: 10/24/2022

Description:
    Generates random numbers from 1019 through 1215 
    and adds writes them to a text file

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

def main():
    user_input = int(input('How many numbers would you like? '))
    with open('random_numbers.txt','w') as fo:
        for n in range(user_input):
            fo.write(str(random.randint(1019,1215))) #Generate the random random, convert to string and write to the text file
            fo.write('\n') #Add a new line


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
