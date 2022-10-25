"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 04.2 - Lucky Sum
Date: 9/24/2022

Description:
    Computes the sum of all numbers that are
    not divisible by 3 between two inputs 

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
def lucky_sum(int1, int2):
    sum = 0
    for n in range(min(int1,int2),max(int1,int2)+1,1): #Loops from lower input number to higher input number
        if n % 3 > 0: #Checks for non-divisibility and computes the sum
            sum += n
    return sum

def main():
    int1 = int(input("Enter the first integer: "))
    int2 = int(input("Enter the second integer: "))
    sum = lucky_sum(int1, int2)
    print(f"The sum of the lucky numbers is {sum:,.0f}.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
