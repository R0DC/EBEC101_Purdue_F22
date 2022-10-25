"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 07.3 - Roll Analysis
Date: 10/24/2022

Description:
    The program rolls 1,000,000 dice and collects the values.
    It then computes the probability of different possible sums.

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
def roll_d6():
    return random.randint(1,6) #Roll a random number from 1 to 6

def get_2d6_rolls(num_rolls):
    results = []
    for _ in range(1,num_rolls+1):
        results.append(roll_d6()+roll_d6()) #Roll the die twice and add the sum to the list
    return results


def main():
    num_rolls = 1000000
    results = get_2d6_rolls(num_rolls)
    print("Roll  Frequency")
    for i in range(2,12+1):
        print(f" {i:2d}   {results.count(i)/len(results)*100:6,.2f}%") #Print the statistics



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
