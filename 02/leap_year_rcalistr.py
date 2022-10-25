"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 02.1 - Leap Year
Date: 09/08/2022

Description:
   The program computes whether an input year is a leap year or not.

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
    year = int(input("Enter a year: ")) #Request input from user
    if (year % 100 == 0 and year % 400 == 0): #Check to make sure the year is divisible by 100 and 400
        print(f"The year {year} is a leap year.\nFebruary of {year} has 29 days.")
    elif (year % 100 != 0 and year % 4 == 0): #Check to make sure the year is divisible by 4 but not 100
        print(f"The year {year} is a leap year.\nFebruary of {year} has 29 days.")
    else: #If neither condition above is satisfied, the year is not a leap year
        print(f"The year {year} is not a leap year.\nFebruary of {year} has 28 days.")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
