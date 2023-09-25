#Information collecting
name = str(input("What is your name?: "))
network = str(input("What is your mobile phone network?: "))
minutes = int(input("How many minutes have you used this month?: "))
texts = int(input("How many texts have you sent this month?: "))

#Multiplying and Calculating total
tminutes = minutes * 0.10
ttexts = texts * 0.05
total = tminutes + ttexts
VAT = total * 0.20
totalwvat = total + VAT

#Displaying
print("Your total bill without VAT is £",total,)
print("Your total with VAT is £",totalwvat)