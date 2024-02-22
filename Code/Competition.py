#Imports
import time as snooze
import sys

# User name collection
print("""To start please make a username. This must include:
• At least 1 Uppercase Letter
• At least 1 Number""")
snooze.sleep(2)

name = input("Enter your username: ")
snooze.sleep(1)
print("Username taken in for verification")
print("""////////////////
////////////////
////////////////
////////////////""")
snooze.sleep(2)
# Checking for Capital letter
if any(char.isupper() for char in name):
    Check1 = True
else:
    Check1 = False
    print("Your user doesnt not contain a capital letter")
    sys.exit()

#Checking for number
if any(char.isdigit() for char in name):
    Check2 = True
else:
    Check2 = False
    print("Your user doesnt not contain a number")
    sys.exit()

#Choose game
loop = True
while loop == True:
    if Check1 and Check1 == True:
        print("""Choose one of these games:
        • Chess
        • Billiards
        • Darts""")
        snooze.sleep(2)
        gamechosen = str(input("Enter one of those games: "))
    gamechosen = gamechosen.lower()
    if gamechosen in ["chess", "billiards", "darts"]:
        print("Game chosen successfully")
        loop = False
        sys.exit
    else:
        snooze.sleep(2)
        print("Invalid choice try again")
        loop = True

#Save to file
with open('Saved data.txt', 'a') as file:
    file.write(f'Username: {name}\n')
    file.write(f'Game chosen: {gamechosen}\n')
    file.close
