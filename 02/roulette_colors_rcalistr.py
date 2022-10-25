"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 02.3 - Roulette Colors
Date: 09/08/2022
Description:
    Determines the color pocket for a user input number.

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
    pkt_nr = int(input("Please choose a pocket number: "))
    if 0 <= pkt_nr < 37:
        if pkt_nr == 0: #If 0, set color to green
            color = 'green'
        elif (1 <= pkt_nr < 11) or (19 <= pkt_nr < 29):
            if pkt_nr % 2 == 0: #If even, set color to black
                color = 'black'
            else: #If odd, set color to red
                color = 'red'
        elif (11 <= pkt_nr < 19) or (29 <= pkt_nr < 37):
            if pkt_nr % 2 == 0: #If even, set color to red
                color = 'red'
            else: #If odd, set color to black
                color = 'black'
        else:
            return None
        print(f"  Pocket number {pkt_nr} is " + color + '.')
    else: 
        print("  Invalid Input!")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
