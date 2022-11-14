"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 09.2 - World Series
Date: MM/DD/YYYY

Description:
    Loads the file with the MLB World Series winners.
    Then shows which team won by year and how many
    times the team won the World Series

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
def load_winners_data():
    data = []
    num_wins = {}
    year_winner = {}
    with open('WorldSeriesWinners.txt','r') as fo:
        for line in fo:
            data.append(line.rstrip())
    #Counts how many times each team won the World Series
    for m in data:
        wins = 0
        for n in data:
            if m == n:
                wins += 1
        num_wins[m] = wins
    #Shows the year when each team won the World Series
    i = 0
    for year in range(1903,2022):
        if year == 1904 or year == 1994: #World Series was not played in 1904 and 1994
            pass
        else:
            year_winner[year] = data[i]
            i += 1
    return num_wins, year_winner

def main():
    num_wins, year_winner = load_winners_data()
    user_input = int(input("Enter a year in the range 1903 -- 2021: "))
    if user_input < 1903 or user_input > 2021:
        print(f'  Data for the year {user_input} is not included in this system.')
    elif user_input == 1904 or user_input == 1994:
        print(f"  The World Series wasn't played in the year {user_input}.")
    else:
        print(f"  The {year_winner[user_input]} won the World Series in {user_input}.\n  They have won the World Series {num_wins[year_winner[user_input]]} times.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
