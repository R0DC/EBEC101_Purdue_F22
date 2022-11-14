"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 10.3 - COVID 19 Cases
Date: 11/12/2022

Description:
    The program plots the total number of cases of Covid-19 
    in Indiana from 2020 to 2022 in the form of a bar plot.

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
import datetime

"""Write new functions below this line (starting with unit 4)."""


def main():
    data = []
    first_date, last_date, new_cases, new_deaths, total_cases = [], [], [], [], []
    with open('indiana_covid-19_data_fall_2022.txt','r') as fo:
        for line in fo:
            data.append(line.rstrip()) #Read the data from the text file and convert to flaot type
    
    #Assigns the various data found in a line of the 'data' list to other lists
    for item in data:
        first_date.append(item.split()[0])
        last_date.append(item.split()[1])
        new_cases.append(float(item.split()[2]))
        new_deaths.append(float(item.split()[3]))
    
    #Computes the total number of cases in thousands
    previous_week = 0
    for nr in new_cases:
        total_cases.append((nr + previous_week)/1000)
        previous_week = (nr + previous_week)

    #Re-defines the date such that it can be plotted
    first_date_fixed = []
    for date in first_date:
        y, m, d = date.split('-')
        dt = datetime.date(int(y), int(m), int(d))
        first_date_fixed.append(dt)
    
    fig, ax = plt.subplots() #Generate the figure and axes
    ax.bar(first_date_fixed, total_cases, width=7) #Plot the data as a bar graph with bar width of 7 pixels
    ax.set_title('Weekly Positive COVID-19 Cases in Indiana') #Set title
    #Set the axes titles/labels
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Cases (in thousands)')
    #Set axes ticks
    ax.set_yticks([0,250,500,750,1000,1250,1500,1750,2000, 2250])
    #Fixes the formatting of the x/date axis
    fig.autofmt_xdate()
    plt.show()


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
