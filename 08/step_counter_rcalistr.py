"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 08.6 - Step Counter
Date: 10/29/2022

Description:
    Given a list of steps taken each day for 365 days,
    the program computes the average steps taken
    each month

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
    data = []
    steps = []
    Months = ['January','February','March','April','May','June','July','August','September','October','November','December'] #Months in a year
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31] #Days of months
    steps_mon = [0,0,0,0,0,0,0,0,0,0,0,0]
    start = 0 #Keeps track of the month the loop is in

    with open('steps.txt','r') as fo:
        for line in fo:
            data.append(line.rstrip()) #Read the lines from the file into the list
    
    for _ in data:
        steps.append(float(_)) #Convert the strings into float values

    for month in range(0,len(Months)):
        for days in range(0,month_days[month]):
            steps_mon[month] += steps[days + start] #Sums up steps for a month
        start += month_days[month] #Iterates which month the steps are counted for

    print("The average steps taken each month were:")
    for m in range(0,len(Months)):
        print(f"{Months[m]:>10} : {steps_mon[m]/month_days[m]:7.2f}")
        
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
