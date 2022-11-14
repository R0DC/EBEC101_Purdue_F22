"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 10.2 - Gas Prices
Date: 11/12/2022

Description:
    The program plots the weekly gas prices from 2008
    in a line graph.

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
import matplotlib.pyplot as plt

"""Write new functions below this line (starting with unit 4)."""

def main():
    data = []
    weeks = range(1,53)
    with open('2008_Weekly_Gas_Averages.txt','r') as fo:
        for line in fo:
            data.append(float(line.rstrip())) #Read the data from the text file and convert to flaot type
    fig, ax = plt.subplots() #Generate the figure and axes
    ax.plot(weeks, data) #Plot the data as a line graph
    ax.set_title('2008 Weekly Gas Prices') #Set title
    #Set the axes titles/labels
    ax.set_xlabel('Weeks (by number)')
    ax.set_ylabel('Average Price (dollars/gallon)')
    #Set axes limits
    ax.set_xlim(1,52)
    ax.set_ylim(1.5,4.25)
    #Set axes ticks
    ax.set_xticks([10,20,30,40,50])
    ax.set_yticks([1.5,2.0,2.5,3.0,3.5,4.0])
    ax.grid() #Turns on the grid
    plt.show()


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
