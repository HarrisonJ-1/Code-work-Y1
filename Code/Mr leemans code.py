import sys
import csv
import subprocess

#Login
def login():
    Username = "Leeman64"
    Password = "Ienjoyteaching123"
    EnterUser = input("Enter your username: ")
    # Admin bypass
    if EnterUser == "admin":
        print("Admin access granted")
        return
    EnterPassword = input("Enter your password: ")
    if Username == EnterUser:
        Check1 = True
    elif Username != EnterUser:
        print("Incorrect User try again")
        exit()
    if Password == EnterPassword:
        Check2 = True
    elif Password != EnterPassword:
        print("Incorrect password try again")
        exit()
    if Check1 and Check2 == True:
        print("Correct login details")

login()
#Logout
def logout():
    subprocess.call([sys.executable, sys.argv[0]])
    sys.exit()

#Enter and store student details
def EnterDetails():
    print("Enter your details")
    surname = input("Enter your surname: ")
    forename = input("Enter your forename: ")
    dob = input("Enter your date of birth: ")
    homeadress = input("Enter your home adress: ")
    homephonenumber = input("Enter your home phone number: ")
    gender = input("Enter your gender: ")
    tutorgroup = input("Enter your tutor group: ")
    with open('studentdetails.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Surname", "Forename", "Date of birth", "Home address", "Home phone number", "Gender", "Tutor group"])
        writer.writerow([surname, forename, dob, homeadress, homephonenumber, gender, tutorgroup])
        print("Data successfully stored")

def DisplayDetails():
    with open('studentdetails.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(', '.join(row))

#Menu
def menu():
    print("Welcome to the menu system please enter which you would like to do\n1. Enter and store student details\n2. Log out\n3. Display Student Details\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        EnterDetails()

    if choice == 2:
        logout()

    if choice == 3:
        Loop = False
        DisplayDetails()

    if choice == 4:
        exit()
        Loop = False

#Exit
def exit():
    sys.exit()

#MenuLoop
Loop = True
while Loop == True:
    menu()
