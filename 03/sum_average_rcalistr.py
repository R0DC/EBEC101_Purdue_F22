"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 03.2 - Sum Average
Date: 09/12/2022

Description:
    The program computes the sum average given
    user input numbers

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


"""Write new functions below this line (starting with unit 4)."""


def main():
    iter = 0 #Initialize the iteration counter
    total = 0 #Initialize the total
    while True:
        num = float(input('Enter a non-negative number (negative to quit): '))
        if num < 0 and iter == 0: #If the iteration counter is 0 and the total is 0, exit the program
            print("  You didn't enter any numbers.")
            break
        elif num >= 0 and iter >= 0: #If the input is positive and the iteration is greater than 0
            iter += 1
            total += num
        elif num < 0 and iter >= 0: #Exit condition: if input is negative and iteration greater than 0, computer average
            avg = total/iter
            print(f"  You entered {iter:.0f} numbers.")
            print(f"  Their sum is {total:.3f} and their average is {avg:.3f}.")
            break
        else:
            return None


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
