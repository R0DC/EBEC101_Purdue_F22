"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 09/01/2022

Description:
    The program tells the user the amount of butter,
    sugar and flour needed to make the user specified
    number of cookies.

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
    n_cookies = int(input("How many cookies do you want to make? ")) #Request user to input number of cookies desired
    cups_butter = n_cookies/48 * 1.25 #Calculate number of cups of butter needed for input number of cookies
    cups_sugar = n_cookies/48 * 1.5 #Calculate number of cups of sugar needed for input number of cookies
    cups_flour = n_cookies/48 * 2.5 #Calculate number of cups of flour needed for input number of cookies
    #Print the results
    print(f"To make {n_cookies:,.0f} cookies, you will need:")
    print(f"{cups_butter:10,.2f} cups of butter")
    print(f"{cups_sugar:10,.2f} cups of sugar")
    print(f"{cups_flour:10,.2f} cups of flour")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
