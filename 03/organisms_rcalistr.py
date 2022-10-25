"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 03.4 - Organisms
Date: 09/12/2022

Description:
    The program computs the population of a bacteria
    based on starting population, growth percentage 
    and number of days

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
    start_pop = float(input("Starting population, in thousands: "))
    avg_d_inc = float(input("Average daily increase, in percent: "))
    nr_d = int(input("Number of days to multiply: "))
    print("Day   Approx. Pop")
    for d in range(nr_d+1):
        print(f"{d:3}{start_pop:14,.3f}") #Print the day and population size
        start_pop = start_pop * (1 + avg_d_inc / 100) #Compute total number of bacteria



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
