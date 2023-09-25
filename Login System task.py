#First name and surname collection
firstname = str(input("What is your first name?: "))
surname = str(input("What is your surname?: "))

#First 3 letters of surname collection
first = surname[0]
second = surname[1]
third = surname[2]
p1 = first + second + third

#First initial
initial = firstname[0]

#Length of surname
length = str(len(surname))

#Final user

user = p1 + initial + length
print ("Your username is",user)