"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 11.2 - Garage
Date: 11/21/2022

Description:
    The program simulates two garages and allows
    the user to add/remove cars to/from lots.

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
class Garage():
    def __init__(self,name,spaces,cars):
        self.name = name
        self.spaces = spaces
        self.cars = cars        

    def car_in(self): #Adds cars to the garage
        if self.cars < self.spaces: #If there are spaces available, add a car, otherwise print that the garage is full
            self.cars += 1
            print(f"  Added a car to {self.name} lot")
        else:
            print(f"  Lot {self.name} is full. Can not add another car.")

    def car_out(self): #Removes cars from the garage
        if self.cars > 0: #If the lot has any cars, remove one, otherwise print that the garage is empty
            self.cars -= 1
            print(f"  Removed a car from Lot {self.name}")
        else:
            print(f"  Lot {self.name} is empty. There are no cars to remove.")

    def status(self): #Output the status of the garage
        print(f"  Lot {self.name}: {self.spaces - self.cars} out of {self.spaces} spaces are available.")
        
"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""

def menu(): #Menu that the user can interact with
    print(f"------------ Menu ------------")
    print(f"  0. Exit")
    print(f"  1. Print current status.")
    print(f"  2. Add a car to A lot.")
    print(f"  3. Add a car to B lot.")
    print(f"  4. Remove a car from A lot.")
    print(f"  5. Remove a car from B lot.")

def main():
    LotA = Garage('A',10,8)
    LotB = Garage('B',15,1)
    print(f"Welcome to the Garage Manager!")
    menu()
    while True:
        userChoice = int(input("Please choose an option (0-5): "))
        #Makes sure that the user input is valid
        if userChoice not in [0,1,2,3,4,5]:
            print("Invalid choice!")
            menu()
        else:
            if userChoice == 0:
                break
            elif userChoice == 1:
                LotA.status()
                LotB.status()
            elif userChoice == 2:
                LotA.car_in()
            elif userChoice == 3:
                LotB.car_in()
            elif userChoice == 4:
                LotA.car_out()
            else:
                LotB.car_out()
    print(f"End of the Day Garage Status:")
    LotA.status()
    LotB.status()



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
