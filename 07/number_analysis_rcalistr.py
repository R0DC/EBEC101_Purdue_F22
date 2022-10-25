"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 07.2 - Number Analysis
Date: 10/24/2022

Description:
    The program calculates different properties of a
    number list: highest, lowest, total and average

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
def get_number_list():
    nums = [] #Initialize an empty list
    for i in range(1,11):
        user_input = float(input(f"  number {i:2d} of 10: ")) #Request 10 user inputs
        nums.append(user_input)
    return nums

def main():
    print("Enter 10 numbers:")
    nums = get_number_list()
    #Print the properties
    print(f"Highest number: {max(nums):.2f}")
    print(f"Lowest number: {min(nums):.2f}")
    print(f"Total: {sum(nums):.2f}")
    print(f"Average: {sum(nums)/len(nums):.2f}")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
