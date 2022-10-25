"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 09/08/2022

Description:
    The program calculates the Reynolds number given user input.
    The user must select a temperature from three options,
    input water velocity in m/s and the pipe diameter in m.
    The code then outputs the Reynolds number formatted
    according to the scientific notation.

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
    temp = float(input("Enter the temperature in °C as 5, 20, or 50: ")) #Requests the user to select a temperature from three options
    vel = float(input("Enter the velocity of water in the pipe (m/s): ")) #Requests the user to input the velocity of the water going into the pipe
    diam = float(input("Enter the pipe's diameter (m): ")) #Requests the user to input the pipe diameter
    #Selection logic which will set the kinematic viscosity of water given the temperature
    if temp == 5:
        nu = 1.52E-6
    elif temp == 20:
        nu = 1E-6
    elif temp == 50:
        nu = 5.54E-7
    else:
        return None
    Re = (vel*diam)/nu #Computes the Reynolds number
    print(f'At {temp}°C, the Reynolds number for flow at {vel} m/s in a {diam} m diameter pipe is {Re:.2e}.') #Outputs the formatted Reynolds number


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
