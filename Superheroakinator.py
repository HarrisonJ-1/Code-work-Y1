heroes = ["Superman", "Batman", "Spiderman", "Hulk", "Iron man", "Thor"]
iswhite = str(input("Is your character white?: "))
if iswhite == "yes":
    superpowers = str(input("Does your character have superpowers?: "))
    if superpowers == "yes":
        cape = str(input("Does your character wear a cape?: "))
        if cape == "yes":
            hammer = str(input("Does your character use a hammer?: "))
            if hammer == "yes":
                print("Your character is",heroes[5])
            else:
                print("Your character is",heroes[0])  
        elif cape == "no":
            print("Your character is",heroes[2])    
    elif superpowers == "no":
        primarycolour = str(input("Is your characters main colour red?: "))
        if primarycolour == "yes":
            rich = str(input("Is your character rich?: "))
            if rich == "yes":
                print("Your character is",heroes[4])
            
        elif primarycolour == "no":
            print("Your character is",heroes[1])
    else:
        print("Invalid answer please enter yes or no")

elif iswhite == "no":
    print("Your character is the",heroes[3])

else:
    print("Invalid answer please enter yes or no")