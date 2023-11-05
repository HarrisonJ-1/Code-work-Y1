#Getting Student info
def studentgrade():
    name = input("Enter student name: ")
    mark = int(input("Enter student's mark: "))
    grade = totalgrade(mark)
    inputfile(name, mark, grade)

 #Caclulating grade       
def totalgrade(mark):
    if 80 <= mark <= 100:
        return 'A*'
    elif 70 <= mark < 80:
        return 'A'
    elif 60 <= mark < 70:
        return 'B'
    elif 50 <= mark < 60:
        return 'C'
    elif 40 <= mark < 50:
        return 'D'
    else:
        return 'You have failed score below 40'

#Inputting data into file
def inputfile(name, mark, grade):
    with open('student_grades.txt', 'a') as file:
        file.write(f"Name: {name}, Mark: {mark}, Grade: {grade} ")
    print("Details successfully saved to file.")

# Viewing File
def viewfile():
    try:
        with open('student_grades.txt', 'r') as file:
            data = file.read()
            if not data:
                print("No data found in the file. Please input some.")
            else:
                print(data)
    except FileNotFoundError:
        print("No data found in the file. Please input some.")

#Clearing File
def clear():
    with open('student_grades.txt', 'w') as file:
        file.write("")
    print("File cleared successfully.")

#Loop
while True:
    print("1. Input a grade")
    print("2. View details in the file")
    print("3. Clear the file")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        studentgrade()
    elif choice == '2':
        viewfile()
    elif choice == '3':
        clear()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")