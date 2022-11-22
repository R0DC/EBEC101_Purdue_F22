"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 11.3 - Rockets
Date: 11/21/2022

Description:
    The program computes the cost per launch for
    traditional rockets and reusable rockets.

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

class Rocket():
    def __init__(self,name,booster_cost, upper_stage_cost,fuel_cost):
        self.name = name
        self.booster_cost = booster_cost
        self.upper_stage_cost = upper_stage_cost
        self.fuel_cost = fuel_cost

    def cost_per_launch(self): #Calculates the total cost per launch of non-reusable rockets and prints the cost
        cost_launch = self.booster_cost + self.upper_stage_cost + self.fuel_cost
        print(f"This {self.name} cost {cost_launch} million per launch.")

class ReusableRocket(Rocket):
    def __init__(self,name,booster_cost, upper_stage_cost,fuel_cost,uses):
        super().__init__(name,booster_cost, upper_stage_cost,fuel_cost)
        self.uses = uses

    def cost_per_launch(self): #Calculates the total cost per launch of reusable rockets and prints the cost
        cost_launch = (self.booster_cost / self.uses) + self.upper_stage_cost + self.fuel_cost
        print(f"This {self.name} cost {cost_launch} million per launch.")

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""


def main():
    Atlas = Rocket('Atlas V',65.4,42.6,0.23)
    Atlas.cost_per_launch()
    Ariane = Rocket('Ariane 5',83.5,55.6,0.69)
    Ariane.cost_per_launch()
    LongMarch = Rocket('Long March 3B',28.5,19.0,2.38)
    LongMarch.cost_per_launch()
    Soyuz2 = Rocket('Soyuz 2',20.9,13.9,0.24)
    Soyuz2.cost_per_launch()
    Falcon = ReusableRocket('Falcon 9',43.0,18.6,0.45,10)
    Falcon.cost_per_launch()



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
