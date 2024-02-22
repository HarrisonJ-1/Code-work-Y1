#loop
hearroar = True
while hearroar == True:
    #Asking about charcteristics
    roar = str(input("Did you hear roar?: "))
    if roar == "yes":
        spines = str(input("Does it have spines?: "))
        if spines == "yes":
            horns = str(input("Does it have horns?: "))
            if horns == "yes":
                print("It is a Triceratops you dont need to run")
                hearroar == False
            elif horns == "no":
                print("Its a Spinosaurus run")
                hearroar == False
        elif spines == "no":
            tall = str(input("Is it very tall?: "))
            if tall == "yes":
                print("It is a Brachiosaurus no need to run")
                hearroar == False
            if tall == "no":
                smallhands = str(input("Does it have small hands?: "))
                if smallhands == "yes":
                    print("Its a T-rex run")
                    hearroar == False
                elif smallhands == "no":
                    boneytail = str(input("Does it have a boney club tail?"))
                    if boneytail == "yes":
                        print("You dont need to run its an Ankylosaurus.")
                        hearroar == False
                    elif boneytail == "no":
                        print("Its a velocoraptor run")
                        hearroar == False
    elif roar == "no":
        print("You dont need to run")
        hearroar == False
    else:
        print("Invalid response")

    