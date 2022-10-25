"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 07.1 - Multiples of N
Date: 10/24/2022

Description:
    Program returns which numbers in a list
    are multiples of a user-defined input

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
def multiples_of(num, num_list):
    multiples_of_num = [] #Initializes an empty array to store the correct values
    for i in num_list:
        if i % num == 0: #Checks if the number is fully divisible by the user-specified number
            multiples_of_num.append(i) #If the number is fully divisible, store it in a list that then gets returned
    return multiples_of_num

def main():
    num = 13
    num_list = [19, 1599, -546, 10, 39, -58, 1, 85, 201, -91, 286, 799, 406]
    multiples_of_num = multiples_of(num, num_list)
    print(f"Original list of numbers:\n  {num_list}")
    print(f"Numbers in the list that are multiples of {num:0d}:\n  {multiples_of_num}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
