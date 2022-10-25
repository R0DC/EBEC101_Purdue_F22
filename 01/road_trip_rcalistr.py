"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 01.1 - Road Trip
Date: 09/01/2022

Description:
    A program that calculates the total cost of a round trip in USD. 
    The user must input the distance to the destination in miles, 
    the average price of fuel in dollars per gallon and the fuel efficiency
    of the vehicle in miles per gallon.

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
    print("Road trip fuel cost estimator:")
    distance = float(input("  How far away is your destination (miles)? ")) #Request user input for total distance in miles
    price_gallon = float(input("  What is the average price of gas (dollars per gallon)? ")) #Request user input for average price per gallon in dollars
    fuel_eff = float(input("  What is the fuel efficiency of your vehicle (mpg)? ")) #Request user input for their car's fuel efficiency
    cost = int((2*distance)*price_gallon/fuel_eff) #Calculates the total cost for the round trip in USD and rounds it down
    print(f"\nThe fuel cost for this trip is approximately ${cost:d}.") #Print the total cost in USD



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
