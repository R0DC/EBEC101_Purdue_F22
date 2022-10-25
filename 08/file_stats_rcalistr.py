"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 08.3 - File Stats
Date: 10/24/2022
Description:
    Returns total number of words, lines and average number
    of words per line for the text file

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
    with open('frontiero_v_richardson.txt') as fo:
        tot_words = len(fo.read().split()) #Get total number of words

    with open('frontiero_v_richardson.txt') as fo:
        tot_lines = len(fo.readlines()) #Get total number of lines

    print(f"Total number of words: {tot_words}")
    print(f"Total number of lines: {tot_lines}")
    print(f"Average number of words per line: {tot_words / tot_lines:.1f}") #Prints the average number of words per line


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
