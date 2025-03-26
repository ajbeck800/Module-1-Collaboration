#Author: AJ Beck
#File Name: ifElseAndWhile.py
#Description: Python app that accepts student names and GPAs and tests if the student qualifies for either the Dean's List or the Honor Roll.

#Ask for and accept a student's last name.
lastName = input("Enter your last name: ")

#Quit processing student records if the last name entered is 'ZZZ'.
quitRecords = 'ZZZ'

#Ask for and accept a student's first name.
firstName = input("Enter your first name: ")

#Ask for and accept the student's GPA as a float.
stringGPA = input("Enter your GPA: ")
GPA = float(stringGPA)

#Test if the student's GPA is 3.5 or greater and, if so, print a message saying that the student has made the Dean's List.
if (GPA > 3.5):
    print(f"{firstName} {lastName} has made the Dean's List!")

#Test if the student's GPA is 3.25 or greater and, if so, print a message saying that the student has made the Honor Roll.
if (GPA > 3.5):
    print(f"{firstName} {lastName} has made the Honor Roll!")