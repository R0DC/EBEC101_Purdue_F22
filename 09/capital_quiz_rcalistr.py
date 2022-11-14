"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 09.1 - Capital Quiz
Date: 10/31/2022

Description:
    Loads a file with the US states and their capitals,
    picks a random state and asks the user to guess
    the capital of the state. 

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
import random

"""Write new functions below this line (starting with unit 4)."""
def get_state_data():
    data = []
    state_capital = {}
    with open('state_capitals.txt','r') as fo:
        for line in fo:
            data.append(line.rstrip())
    for m in range(0,len(data)):
        state_capital.update([(data[m].split(',')[1].strip(),data[m].split(',')[0].strip())]) #Load the data read into a dictionary
    return state_capital

def main():
    cor_counter = 0
    tot_counter = 0
    state_capital = get_state_data()
    while True:
        choice = random.choice(list(state_capital.items())) #Get a random choice of state and capital
        state, capital = choice[0], choice[1] #Assign state and capital values
        user_capital_guess = input(f"What is the capital of {state} (enter 0 to quit)? ")
        if user_capital_guess == '0':
            break #If the user is tired, they hit 0 and the loop quits
        else:
            if user_capital_guess.lower() == capital.lower(): #Case insensitive guesses are good
                print("  That is correct!")
                cor_counter += 1
                tot_counter += 1
                del state_capital[state] #If the user guesses correctly, the state can't be used again
            else:
                print(f'  That is incorrect.\n  The capital of {state} is {capital}.')
                #If the user does not guess the state, add the state to the end of the dictionary
                del state_capital[state]
                state_capital[state] = capital
                tot_counter += 1
    print(f'You answered {cor_counter} out of {tot_counter} questions correctly.')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
