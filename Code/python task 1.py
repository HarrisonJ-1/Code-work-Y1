
iscar = input("Has a car hit the sensor?: ")

if iscar == "yes":
    numberplate = int(input("What was the cars numberplate?: "))
    distance = int(input("How far apart are the sensors in miles?: "))
    sensor2 = int(input("How long did it take for them to hit the second sensor in seconds?: "))


elif iscar == "Yes":
    numberplate = input("What was the cars numberplate?: ")
    distance = input("How far apart are the sensors?: ")
    sensor2 = input("How long did it take for them to hit the second sensor?: ")


else:
    print("Ok")

#Working out mph

mph = distance / sensor2

print("The speed is", mph ,"mph")