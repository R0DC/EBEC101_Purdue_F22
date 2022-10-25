"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 03.3 - Rainfall
Date: 09/12/2022

Description:
    The program computs the total and average
    rainfall over years

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
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] #Initialize the list of months
    total_rain = 0
    while True:
        yrs = int(input("Enter the number of years: "))
        if yrs <= 0: #Input must be greater than 0
            print("Invalid input; years must be greater than 0.")
            break
        elif yrs > 0:
            for n in range(yrs):
                print(f"  For year No. {n+1}")
                for m in months:
                    while True: #Condition to ensure that the user inputs only positive rainfall values
                        rainfall = float(input("    Enter the rainfall for " + m + ".: "))
                        if rainfall < 0: #If the input is negative, prompt the user to input a positive value
                            print("    Invalid input; rainfall cannot be negative.")
                        else: #If the input is positive, compute total and leave the loop
                            total_rain += rainfall
                            break
            print(f"There are {yrs*12} months.")
            print(f"The total rainfall was {total_rain:.2f} inches.")
            print(f"The monthly average rainfall was {total_rain/(yrs*12):.2f} inches.")
            break
        else:
            return None


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
