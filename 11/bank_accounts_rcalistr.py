"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 11.4 - Bank Accounts
Date: 11/21/2022

Description:
    The program imitates a bank account. It has 2 types
    of accounts: regular and savings. It allows the user 
    3 operations: deposit, withdraw and get balance.
    The savings account will accrue interest and add
    it to the total balance.

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

class Account():
    def __init__(self,balance):
        self.balance = balance
        print(f"New account balance: ${self.balance:.2f}")

    def deposit(self,amount): #Print the amount of money being deposited and print the available balance
        print(f"Deposit: ${amount:.2f}")
        self.balance += amount

    def withdraw(self,amount): #Print the amount of money being withdrawn and print the available balance
        if self.balance >= amount: #If the amount withdrawn is larger than the balance available, cancel the withdrawal
            print(f"Withdraw: ${amount:.2f}")
            self.balance -= amount
        else:
            print(f"Withdraw: ${amount:.2f}")
            print("Insufficient funds. Withdrawal canceled.")

    def get_balance(self): #Print the current available balance
        print(f"Balance: ${self.balance:.2f}")

class Savings(Account):
    def __init__(self, balance,interest_rate):
        super().__init__(balance)
        self.interest_rate = interest_rate

    def accrue_interest(self): #If the account is a savings-type, compute interest earned and add it to the balance
        interest_payment = self.balance * self.interest_rate/100
        print(f"Interest payment: ${interest_payment:.2f}")
        self.balance += interest_payment


"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""


def main():
    acc = Savings(200,10)
    acc.get_balance()
    acc.deposit(12.34)
    acc.get_balance()
    acc.withdraw(40.00)
    acc.get_balance()
    acc.withdraw(200.00)
    acc.get_balance()
    acc.accrue_interest()
    acc.accrue_interest()
    acc.accrue_interest()
    acc.withdraw(200.00)
    acc.get_balance()


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
