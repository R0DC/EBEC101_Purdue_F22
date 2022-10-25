"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 02.4 - Time Calculator
Date: 09/08/2022

Description:
    The program computes how the input number of seconds
    divides into days, hours, minutes and seconds. 

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
    time = int(input("Please enter a time in seconds: ")) #Request user input in seconds
    days = int(time // 86400) #Computes days
    hrs = int(time % 86400 // 3600) #Computes hours
    mins = int(time % 3600 // 60) #Computes minutes
    sec = int(time % 60) #Computes remaining seconds
    if time > 59: #If the inputs is larger than a minute
        print(f"  {time:,d} seconds equals ", end='')
        if days: #If there are enough seconds to make a day, print the 'days' portion
            print(f"{days} day(s)", end ='')
        #If there are hours, check if there are days and minutes/seconds
        if hrs: 
            if days:
                if mins or sec:
                    print(", ", end ='')
                else:
                    print(' and ', end = '')
            print(f'{hrs} hour(s)', end='')
        #If there are minutes, check if there are hours and seconds
        if mins:
            if hrs:
                if sec:
                    print(', ', end = '')
                else:
                    print(' and ', end = '')
            print(f'{mins} minute(s)', end='')
        #If at the end there are still seconds left, print the final bit of the output
        if sec:
            print(' and ', end = '')
            print(f'{sec} second(s)', end='')
        print('.')
    #If the input number is less than a minute, prints out the corresponding output
    else:
        print(f"  {time:,.0f} seconds is less than one minute.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
