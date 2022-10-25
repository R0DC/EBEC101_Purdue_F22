"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 07.4 - Magic Square
Date: 10/24/2022

Description:
    The program determines whether a square fulfills several criteria,
    such as that all numbers are unique and are between 1 and 9.
    The sum of the squares must also equal 15, otherwise the square
    is not magic.

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
def print_square(two_dim_array): #Print the magic square
    rows, cols = 3,3
    for r in range(rows):
        print(' ',end='')
        for c in range(cols):
            print(f"{two_dim_array[r][c]:2d}", end='')
        print()
    return None

def is_magic(two_dim_array):
    rows, cols = 3,3
    total_list = []
    total = 0
    test = 15
    #Compute the total along the rows
    for r in range(rows):
        for c in range(cols):
            total += two_dim_array[r][c]
        total_list.append(total)
    #Compute the total along the columns
    for c in range(cols):
        for r in range(rows):
            total += two_dim_array[c][r]
        total_list.append(total)
    #Total the diagonal totals
    diag1 = two_dim_array[0][0] + two_dim_array[1][1] + two_dim_array[2][2]
    diag2 = two_dim_array[2][0] + two_dim_array[1][1] + two_dim_array[0][2]
    total_list.extend([diag1, diag2])
    for m in total_list:
        if m != test:
            return False
        else:
            return True

#Checks that the input square has unique numbers
def all_unique(two_dim_array):
    #Checks whether there are duplicates in the list
    for m in range(len(two_dim_array)):
        for n in range(len(two_dim_array)):
            if m != n:
                if two_dim_array[m] == two_dim_array[n]: #If there are duplicates, the square is not magic
                    return False
                else:
                    return True

def unique_magic(two_dim_array): #Prints the squares
    print("Your square is:")
    print_square(two_dim_array)
    uniques = all_unique(two_dim_array)
    if uniques:
        magic = is_magic(two_dim_array)
        if magic:
            print("It is a Lo Shu magic square!")
        else:
            print("It is not a Lo Shu magic square.")
    else:
        print("It is not a Lo Shu magic square.")


def main():
    lo_shu1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    lo_shu2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    lo_shu3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    unique_magic(lo_shu1)
    print()
    unique_magic(lo_shu2)
    print()
    unique_magic(lo_shu3)

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
