"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 10.4 - Sin Cos
Date: 11/12/2022

Description:
    Computes and draws the sine and cosine waves

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
import math
import matplotlib.pyplot as plt

"""Write new functions below this line (starting with unit 4)."""


def main():
    angle_rads,sine,cosine=[],[],[]
    #Computes the values of sine and cosine
    for angle in range(0,360):
        angle_rads.append(math.radians(angle))
        sine.append(math.sin(math.radians(angle)))
        cosine.append(math.cos(math.radians(angle)))

    fig, ax = plt.subplots() #Generate the figure and axes
    ax.plot(angle_rads,sine,'r') #Draws the red sine wave
    ax.plot(angle_rads,cosine,'b') #Drwas the blue cosine wave
    ax.set_xlim([0,math.radians(380)])
    #Set axes ticks
    ax.set_xticks([math.radians(90),math.radians(180),math.radians(270),math.radians(360)],labels=[r'$\pi/2$',r'$\pi$',r'$3\pi/2$',r'$2\pi$']) #Draws the ticks and labels them with pi 
    ax.set_yticks([-1,1])
    #Remove the top and right spines, make the bottom spine the center spine
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_position('zero')
    plt.show()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
