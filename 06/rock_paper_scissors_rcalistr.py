"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 06.2 - Rock Paper Scissors
Date: 10/09/2022

Description:
    A rock-paper-scissors game. Generates computer choice
    and compares it to the user input. If there is a tie,
    the program restarts.

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

def get_computer_choice():
    return random.choice(['rock','paper','scissors']) #Generate computer choice

def get_player_choice():
    #Request a valid input from the user
    while True:
        user_choice = input('Choose rock, paper, or scissors: ')
        if user_choice in ['rock','paper','scissors']:
            return user_choice
        else:
            print('You made an invalid choice. Please try again.')

def get_winner(pc_choice,player_choice):
    #Winner selections structure
    if pc_choice == player_choice:
        return 'tie'

    elif pc_choice == 'rock':
        if player_choice == 'paper':
            print('  paper beats rock')
            return 'player'
        elif player_choice == 'scissors':
            print('  rock beats scissors')
            return 'computer'

    elif pc_choice == 'paper':
        if player_choice == 'scissors':
            print('  scissors beats paper')
            return 'player'
        elif player_choice == 'rock':
            print('  paper beats rock')
            return 'computer'

    elif pc_choice == 'scissors':
        if player_choice == 'rock':
            print('  rock beats scissors')
            return 'player'
        elif player_choice == 'paper':
            print('  scissors beats paper')
            return 'computer'
    else:
        return None
        
        

def main():
    pc_choice = get_computer_choice() #Generates computer choice
    player_choice = get_player_choice() #Generates user input
    print(f'  The computer chose {pc_choice}, and you chose {player_choice}.')
    winner = get_winner(pc_choice,player_choice) #Finds the winner
    if winner == 'player':
        print('  You won the game!\nThanks for playing.')
    elif winner == 'computer':
        print('  You lost.  Better luck next time.\nThanks for playing.')
    else: #If tie, restart the game
        print("  It's a tie. Starting over.\n")
        main()


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
