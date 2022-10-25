"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 04.4 - Prime Numbers
Date: 9/24/2022

Description:
    Determines if an input number is a prime number or not

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
def is_prime(prime):
    prime_check = True #Assuming that an input number is a prime
    if prime <= 1: #1 is not a prime number
        prime_check = False
    else:
        for n in range (2 ,prime):
            check = prime % n #Checks if the input number is divisible by each number leading up to it
            if check == 0: #If an input number is not a prime, exits the loop
                prime_check = False
                break
    return prime_check


def main():
    prime = int(input("Enter a positive integer (-1 to quit): "))
    while True: 
        if prime > -1:
            TF = is_prime(prime)
            if TF == True:
                print(f"  {prime} is prime!")
            else:
                print(f"  {prime} is not prime.")
            break
        else:
            break


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
