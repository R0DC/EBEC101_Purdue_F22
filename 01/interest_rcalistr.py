"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 01.2 - Interest
Date: 09/01/2022

Description:
    The program calculates the final value of a bank account.
    The user must input the principal amount originally deposited,
    the annual interest rate, the number of times per year that
    the interest is compounded and how many years it will compound.
    The program then returns the final value in USD after the amount
    of years the user input.

Contributors:
    Rodion Calistru, rcalistr@purdue.edu

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
    print("Enter the following parameters.")
    principal = float(input("  The initial deposit? ")) #Reguests the user to input original principal amount of money deposited
    interest = float(input("  The annual interest rate in percent? ")) #Reguests the user to input annual interest rate
    n_year = float(input("  The number of years the account earn interest? ")) #Reguests the user to input how many times per year is the interest compounded
    n_comp = float(input("  The number of times interest is compounded each year: ")) #Reguests the user to input the number of years it will compound
    FV = principal*(1 + (interest/100)/n_comp)**(n_comp*n_year) #Computes the final value given the user inputs
    print(f"The balance of this account will be ${FV:,.2f} after {n_year:3.1f} years.") #Prints the formatted final value


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
