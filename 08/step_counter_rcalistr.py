"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 08.6 - Assignment Name
Date: MM/DD/YYYY

Description:
    Describe your program here.

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
    Months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    month_days = [31,28,31,30,31,30,30,31,31,30,31,30,31]
    steps_mon = [0,0,0,0,0,0,0,0,0,0,0,0]
    counter = 0
    with open('steps.txt','r') as fo:
        for line in fo:
            data.append(line.rstrip()) #Read the lines from the file into the list
    
    for _ in data:
        steps.append(float(n)) #Convert the strings into float values

    for nr_record in range(len(steps)):
        if 0 <= nr_record < 31:
            steps_mon[0] = steps[nr_record]
        elif 31 <= nr_record < 31 + 28:
        

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
