"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 04.5 - Prime List
Date: 9/24/2022

Description:
    The program accepts a user input, computes the numbers
    that come before it and analyzes which numbers 
    leading to the input number are prime and lists them

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
    if prime == 1: #1 is not a prime number
        prime_check = False
    else:
        for n in range (2 ,prime):
            check = prime % n #Checks if the input number is divisible by each number leading up to it
            if check == 0: #If an input number is not a prime, exits the loop
                prime_check = False
                break
    return prime_check

def main():
    prime = int(input("Enter a positive integer: "))
    print(f"The primes up to {prime} are:", end='')
    for n in range(1,prime+1): #Loops through all numbers leading up to the input number
        check = is_prime(n)
        if check == True:
            print(f" {n}",end='') #Prints the current number if it is prime
            if n >= prime:
                print("",end='')
            else:
                print(",",end='')
                


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
