"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 04.1 - Falling
Date: 9/24/2022

Description:
    The program computes the distance fallen
    on Venus given the equation and constant
    provided over 50 seconds.

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
g = 8.87 #Venus acceleration paramater [m/s^2] 

def falling_dist(time):
    distance = 0.5 * g * time**2 #Computes the distance fallen
    return distance

def main():
    print('Time (s)  Distance (m)')
    print('----------------------')
    for time in range(5,55,5):
        distance = falling_dist(time)
        print(f"{time:8.0f} {distance:13.1f}")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
