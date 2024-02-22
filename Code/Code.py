import time
import sys
#Total 
total = 0

# Function to view cart
def view_cart():
    with open('cart.txt', 'r') as file:
        contents = file.read()
        print("Cart contents:")
        print(contents)

# Function tea
def buy_tea():
    global total
    print("""Tea\nSome of the allergies that this drink may trigger are:\nTree Nuts\nSoy\nDairy\nGluten""")
    print("The price for a tea is £1.50")
    buy_tea = input("Would you like to buy a tea?: ")
    if buy_tea.lower() == "yes":
        total += 1.50
        print("Tea added to cart")
        with open('cart.txt', 'a') as file:
            file.write("Tea - £1.50\n")

# Function for coffee
def buy_coffee():
    global total
    print("""Coffee\nSome of the allergies that this drink may trigger are:\nTree Nuts\nSoy\nDairy\nGluten""")
    print("The price for a Coffee is £2.50")
    buy_coffee = input("Would you like to buy a Coffee?: ")
    if buy_coffee.lower() == "yes":
        total += 2.50
        print("Coffee added to cart")
        with open('cart.txt', 'a') as file:
            file.write("Coffee - £2.50\n")
# Function to buy muffin
def buy_muffin():
    global total
    print("""Muffin\nSome of the allergies that this drink may trigger are:\nDairy\nGluten\nWheat protiens""")
    print("The price for a Muffin is £2.00")
    buy_coffee = input("Would you like to buy a Muffin?: ")
    if buy_coffee.lower() == "yes":
        total += 2
        print("Muffin added to cart")
        with open('cart.txt', 'a') as file:
            file.write("Muffin - £2.00\n")
#Function to buy French toast
def buy_toast():
    global total
    print("""French Toast\nSome of the allergies that this drink may trigger are:\nDairy\nGluten\nWheat protiens""")
    print("The price for French Toast is £5.00")
    buy_toast = input("Would you like to buy French toast?: ")
    if buy_toast.lower() == "yes":
        total += 5
        print("French Toast added to cart")
        with open('cart.txt', 'a') as file:
            file.write("French Toast - £5.00\n")
# Function to buy smoothie
def buy_smoothie():
    global total
    print("""Smoothie\nSome of the allergies that this drink may trigger are:\nApple\nPeach\nKiwi""")
    print("The price for a Smoothie is £2.00")
    buy_smoothie = input("Would you like to buy a Smoothie?: ")
    if buy_smoothie.lower() == "yes":
        total += 3
        print("Smoothie added to cart")
        with open('cart.txt', 'a') as file:
            file.write("Smoothie - £3.00\n")

#English menu
def english_menu():
    print("""Menu:
      Hot drinks
      1. Tea
      2. Coffee
      Food
      3. Muffin
      4. French toast
      Smoothies
      5. Fruit Smoothie""")
    choice = int(input("Enter your item number of choice: "))
    return choice

def add_item(choice): 
  if choice == 1:
      buy_tea()
  if choice == 2:
      buy_coffee()
  if choice == 3:
      buy_muffin()
  if choice == 4:
      buy_toast() 
  if choice == 5:
      buy_smoothie()
def checkout():
    print("Your total is", total)
    pay = str(input("Would you like to pay?: "))
    if pay.lower() == "yes":
        print("You have paid")
        sys.exit()
    else:
        print("You have chosen not to pay exiting system")
        sys.exit()
# Main menu function
def eng_menu():
    print("Welcome to the menu system please choose what you want to do")
    time.sleep(2)
    while True:
        print("1. Add item to cart\n2. View cart\n3. Exit program\n4. Checkout\nExiting the program will clear the cart!")
        menu_choice = int(input("Which one would you like to do?: "))

        if menu_choice == 1:
            item_choice = english_menu()
            add_item(item_choice)
        elif menu_choice == 2:
            view_cart()
            print("Your total is £", round(total, 2))
        elif menu_choice == 3:
            with open("cart.txt", 'w') as file:
                pass
            sys.exit()
        elif menu_choice == 4:
            checkout()
eng_menu()

