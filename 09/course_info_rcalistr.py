"""
Author: Rodion Calistru, rcalistr@purdue.edu
Assignment: 09.3 - Course Info
Date: 10/31/2022

Description:
    Displays course data (room, instructor, time)
    based on user input course number

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
def get_course_data():
    course_data = {'CS101':{'room':'3004','instructor':'Django','time':'9:00 a.m.'},
                   'CS102':{'room':'4501','instructor':'Idle','time':'10:00 a.m.'},
                   'CS103':{'room':'6755','instructor':'Rich','time':'11:00 a.m.'},
                   'NT110':{'room':'1244','instructor':'Marshal','time':'12:00 p.m.'},
                   'CM241':{'room':'1411','instructor':'Pickle','time':'2:00 p.m.'},}
    return course_data

def main():
    course_data = get_course_data()
    user_inp = input("Enter a course number: ")
    if user_inp in course_data:
        course = course_data.get(user_inp) #Retrieve user-specified course dictrionary
        #Retrieve course specifics
        room = course.get('room')
        instructor =  course.get('instructor')
        time = course.get('time')
        print(f"  The details for course {user_inp} are:")
        print(f"{'Instructor':>14}: {instructor}")
        print(f"{'Room':>14}: {room}")
        print(f"{'Time':>14}: {time}")
    else:
        print(f"  {user_inp} is an invalid course number.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
