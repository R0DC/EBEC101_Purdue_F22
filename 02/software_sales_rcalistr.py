"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 02.2 - Software Sales
Date: 09/08/2022

Description:
    Computes the discount for software sales based on user input.
    Depending on amount of software packages purchased,
    the discount increases proportionately.

Contributors:
    Name, login@purdue.edu [repeat for each]

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
    pckgs = float(input("How many packages will be purchased: "))
    pckg_pr = 880 #Standard price of 1 package
    if pckgs > 0:
        #Discount brackets
        if 0 <= pckgs < 4:
            disc = 0
        elif  4 <= pckgs < 40:
            disc = 10
        elif 40 <= pckgs < 200:
            disc = 15
        elif 200 <= pckgs < 1000:
            disc = 30
        else:
            disc = 42
        if disc == 0: #If the number of packages purchased is less than 3, no discount is applied
            pckg_tot = pckg_pr * pckgs
            print(f"  No discount applied.\n  The total price to purchase {pckgs:,.0f} packages is ${pckg_tot:,.2f}.")
        else:
            pckg_tot = pckg_pr * pckgs * (1 - disc/100) #Compute the total price of the purchase
            print(f"  {disc}% discount applied.\n  The total price to purchase {pckgs:.0f} packages is ${pckg_tot:,.2f}.")
    else:
        print("  Invalid Input!")
        


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
