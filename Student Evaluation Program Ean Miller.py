# Author: Ean Miller
# Program: Student Evaluation Program Ean Miller.py
# Description: This program evaluates a student's GPA and determines if they are an honor student, on the Dean's List, or neither.
continueProgram = True
while continueProgram == True:
    print("{Please enter the last name of the student you wish to evaluate:}")
    last_name = input()
    if last_name == "ZZZ":
        print("{No student to evaluate.}")
        print("{Ending program.}")
        continueProgram = False
    else:
        print("{Please enter the first name of the student you wish to evaluate:}")
        first_name = input()
        print("{Please enter the GPA of the student you wish to evaluate:}")   
        gpa = float(input())
        if gpa >= 3.5:
            print("{The student is on the Dean's List.}")
        elif gpa >= 3.25:
            print("{The student is an honor student.}")
        else:
            print("{The student is neither an honor student nor on the Dean's List.}")
    print("Would you like to evaluate another student? (Y/N)")
    response = input()
    if response == "Y":
        continueProgram = True
    else:    
        print("{Thank you for using the student evaluation program.}")
        print("{Ending program.}")
        continueProgram = False