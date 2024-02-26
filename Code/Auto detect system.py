#Users problem
problem = str(input("Please enter the problem with your device: ")).lower()

#General filter
general = ["broken", "not working"]
if any(word in problem for word in general):
   print("Too general of a description try again being more specific.")
#Battery Problems
battery = ["battery", "charging"]
if any(word in problem for word in battery):
   print("The problem is your battery take it to a repair shop and tell them.")
#Broken display
display = ["cracked", "smashed", "black"]
if any(word in problem for word in display):
   print("The problem is your display take it to a repairshop to get it fixed.")
#Dropped in water
water = ["water", "wet"]
if any(word in problem for word in water):
   print("The problem is your phone is filled with water leave it in rice for 1-2 days if it still doesnt work take it to a repair shop.")
#Dropped from a height
height = ["dropped", "fall", "fell", "height"]
if any(word in problem for word in height):
   print("We have detected a possible fall damage take it to a repair shop.")
