"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 08.2 - Phone Number Converter
Date: 10/24/2022

Description:
    Takes alphanumeric phone numbers and converts them
    to digit-only numbers using the keypad mapping

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
def convert_number(str_inp):
    phone_nr = []
    phone_nr_digit = []
    phone_nr = str_inp.split('-') #Splits the string into substrings
    for m in phone_nr:
        phone_nr_portion = [] #Reset list for each portion of the numbers
        for i in m:
            if i.isalpha(): #Checks for letters
                #Keypad letter mapping
                if i.upper() in ('A','B','C'):
                    phone_nr_portion.append('2')
                elif i.upper() in ('D','E','F'):
                    phone_nr_portion.append('3')
                elif i.upper() in ('G','H','I'):
                    phone_nr_portion.append('4')
                elif i.upper() in ('J','K','L'):
                    phone_nr_portion.append('5')
                elif i.upper() in ('M','N','O'):
                   phone_nr_portion.append('6')
                elif i.upper() in ('P','Q','R','S'):
                    phone_nr_portion.append('7')
                elif i.upper() in ('T','U','V'):
                    phone_nr_portion.append('8')
                elif i.upper() in ('W','X','Y','Z'):
                    phone_nr_portion.append('9')
                else:
                    pass
            else:
                phone_nr_portion.append(i)
        phone_nr_digit.append(''.join(phone_nr_portion)) #Form the number string from the list
    return '-'.join(phone_nr_digit)

def main():
    user_input = input('Enter a telephone number: ')
    phone_nr = convert_number(user_input)
    print('The phone number is ' + phone_nr)


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
