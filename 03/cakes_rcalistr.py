"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 03.1 - Cakes
Date: 09/12/2022

Description:
    A program that makes a cake with the 
    number of layers specified by the user

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
    layers = int(input("Enter the number of layers: "))
    layers_left = layers #Sets the remaning layers to draw
    for r in range(1,layers+1):
        layers_left -=1 #Decrease layers remaining
        print(' '*layers_left + '[', end='') #Start the layer
        for c in range (1,r*2):
            print('*', end='') #Print the layer
        print(']') #End the layer


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
