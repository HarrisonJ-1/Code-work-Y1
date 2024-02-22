#Inputs and Outputs
print ("What is your name?")

firstname = input()

print ("Hello,",firstname)

print ("What is your surname?")

surname = input()

print ("Your surname is",surname)

#Combining the first name and surname
print ("Hello,",firstname,surname)

#Displaying the initials 
print("Your initials are:",firstname[0],surname[0])

#Concatinating the two names
fullname = firstname +" "+ surname
print ("Your full name is",fullname)


#Upper case surname
upsurname = surname.upper() + " " + firstname
print(upsurname) 

#Letters in surname

sletters = len(surname)
print("There are",sletters,"Letters in your surname")

