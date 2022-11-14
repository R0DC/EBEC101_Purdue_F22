"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 10.1 - Monthly Sales
Date: 11/12/2022

Description:
    Displays monthly sales in a pie chart using the 
    data the user input.

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
def user_input():
    months = ('January','February','March','April','May','June','July','August','September','October','November','December') #Months in a year
    sales_months = []
    for m in months:
        #Ask for monthly sales and append to the list
        sale = int(input(f'Enter the sales for {m}: '))
        sales_months.append(sale)
    return sales_months, months


def main():
    sales_months, months = user_input()
    color_hex = ['#4D4038', '#BAA892', '#5B6870', '#6E99B4', '#A3D6D7', '#085C11', '#849E2A', '#C3BE0B', '#E9E45B', '#6B4536', '#B46012', '#FF9B1A'] #Purdue’s retired secondary color palette hex codes
    fig, ax = plt.subplots() #Generate the figure and the axes
    ax.pie(sales_months, colors=color_hex, labels=months) #Generate the pie chart using the months as labels and the Purdue’s retired secondary color palette
    ax.set_title('Monthly Sales Values')
    plt.show()


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
