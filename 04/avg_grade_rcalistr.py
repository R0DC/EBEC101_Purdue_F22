"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 04.3 - Avg Grade
Date: 9/24/2022

Description:
    Computes the the average of five input numbers
    and displays the grade for each input number.

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
def get_valid_score():
    score = 0
    score = float(input("Enter a score: "))
    while True: #Loop checks for a correct input and returns the score once it is valid
        if score >= 0 and score <= 100:
            determine_grade(score)
            return score
        else:
            print("  Invalid Input. Please try again.")
            score = float(input("Enter a score: "))


def calc_average(score_list):
    sum = 0
    for n in range(0,len(score_list)): #Goes through the five scores
        sum += score_list[n] #Computes the sum of the entire list
    average = sum / (n + 1) #Computes the average 
    return average

#Grade selection and returns the letter
def determine_grade(score):
    if score >= 92 and score <= 100:
        letter = 'A'
    elif score < 92 and score >= 82:
        letter = 'B'
    elif score < 82 and score >= 73:
        letter = 'C'
    elif score < 73 and score >= 64:
        letter = 'D'
    else:
        letter = 'F'
    return letter
    

def main():
    score_list = [0,0,0,0,0]
    for n in range(0,len(score_list)):
        score = get_valid_score()
        letter = determine_grade(score)
        print(f"  The letter grade for {score:.1f} is " + letter + '.')
        score_list[n] = score #Adds the score to the aggregated list of scores
    avg = calc_average(score_list)
    print(f"\nResults:")
    print(f"  The average score is {avg:.2f}.")
    print(f"  The letter grade for {avg:.2f} is " + determine_grade(avg) + '.')



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
