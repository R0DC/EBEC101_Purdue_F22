"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 08.1 - Pig Latin
Date: 10/24/2022

Description:
    The program takes a string input and converts it
    into pig latin by removing the first letter,
    putting it at the end and adding 'ay' at the end.

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
def pig(inp_str):
    new_str = []
    str_list = inp_str.split(' ') #Splits the string into substrings i.e. words
    for word in str_list:
        new_word = word + word[0] + 'ay' #Adds the first letter and 'ay' at the end
        new_word = new_word.lstrip(new_word[0]) #Removes the first letter
        new_str.append(new_word)
    new_str = ' '.join(new_str) #Joins all characters into a string
    new_str = new_str.capitalize().strip()
    return new_str


def main():
    user_input = input('Enter a string: ')
    pig_latin = pig(user_input)
    print('Pig latin: ' + pig_latin)


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
