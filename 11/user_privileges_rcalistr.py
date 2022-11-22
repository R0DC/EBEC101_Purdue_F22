"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 11.5 - User Privileges
Date: 11/21/2022

Description:
    The program displays the privileges a user has.
    It is possible to grant and revoke privileges
    if calling the correct commands.

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
class Privileges():
    def __init__(self,privs):
        if not privs: #If the priveleges input set is empty, give the user some default privileges
            self.privs = {'interact','post'}
        else:
            self.privs = privs

    def grant(self,new_priv): #Grant privilege and add it to the set of privileges
        self.privs.add(new_priv.lower())
        print(f"Granted {new_priv}")

    def revoke(self,new_priv): #Revoke privilege and remove it to the set of privileges
        self.privs.remove(new_priv.lower())
        print(f"Revoked {new_priv}")

    def get_privs(self): #List the privileges the user has in alphabetical order
        priv_list = list(self.privs)
        priv_list.sort()
        priv_list = str(priv_list).strip("[]").replace("'",'')
        return priv_list

class User():
    def __init__(self,name,email,privs):
        self.name = name
        self.email = email
        self.privs = Privileges(privs)

    def describe_user(self):
        print("User Profile")
        print(f"  Name: {self.name}")
        print(f"  Email: {self.email}")
        print(f"  Privs: {self.privs.get_privs()}")


"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""


def main():
    user = User('Alice','alice@example.com',{})
    user.describe_user()
    user.privs.grant('teleport')
    user.describe_user()
    user.privs.revoke('post')
    user.describe_user()


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
