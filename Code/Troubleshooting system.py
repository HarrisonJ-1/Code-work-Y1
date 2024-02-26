#Imports
import sys
import time

#Invalid answer funciton
def invalid():
    print("Invalid answer")
    sys.exit


#Welcome message
print('Welcome to the support chatbot I will help you find a soultion onto the problem of the device. Please only answer using \"yes\" or \"no\"')
#Checking for battery problem.
charged = str(input("Is the phone charged: "))
if charged == "no":
    battery = str(input("Does it charge?: "))
    if battery == "yes":
        print("Charge it and and restart the program")
        sys.exit
    elif battery == "no":
        print("Problem with the phone battery take it to the nearest repair shop")
    else:
        invalid()
elif charged == "yes":
    #Checking for height damage
    height = str(input("Did you drop the phone from a height?: "))
    if height == "yes":
        damaged = str(input("Does it look damaged?: "))
        if damaged == "no":
            print("Take it to the nearest repair shop and have them check the internal components")
        elif damaged == "yes":
            print("Take it to the nearest repair store and have them deal with the damages")
        else:
            invalid()
    elif height == "no":
        #Checking for water damage 
        water = str(input("Did you drop your phone in water?: "))
        if water == "yes":
            print("Leave it in rice for 1-2 days")
        elif water == "no":
            print("Problem not found take it to the nearest repair shop to have people test it")
    else:
        invalid()
else:
    invalid()