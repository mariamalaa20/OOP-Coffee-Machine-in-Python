from info import MENU
from info import resources
want_coffee = True
machine_money = 0

water_tracker = resources['water']
coffee_tracker = resources['coffee']
milk_tracker = resources['milk']

def check_resources(ingredients):
    """Check if the machine has enough resources for the drink."""
    if water_tracker < ingredients['water']:
        print("Sorry, there is not enough water.")
        return False
    if coffee_tracker < ingredients['coffee']:
        print("Sorry, there is not enough coffee.")
        return False
    if 'milk' in ingredients and milk_tracker < ingredients['milk']:
        print("Sorry, there is not enough milk.")
        return False
    return True

def calculating_coins():
    """Process the coin input and return the total money paid."""
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    return quarters * 0.25 + dimes * 0.10+ nickles * 0.05+ pennies * 0.01

def make_coffee(drink, ingredients):
    """Deduct the resources used to make the drink."""
    global water_tracker, coffee_tracker, milk_tracker
    water_tracker -= ingredients['water']
    coffee_tracker -= ingredients['coffee']
    if 'milk' in ingredients:
        milk_tracker -= ingredients['milk']
    print(f"Enjoy your {drink}☕!")

while want_coffee:
    ques1 = input("what wold you like? (espresso/latte/cappuccino): ").lower()

    if ques1 == "report":
        print(f"Water: {water_tracker}ml")
        print(f"Milk: {milk_tracker}ml")
        print(f"Coffee: {coffee_tracker}g")
        print(f"Money: ${machine_money}")


    elif ques1 in MENU:

        drink = MENU[ques1]
        ingredients = drink['ingredients']

        if check_resources(ingredients):
            money_paid = calculating_coins()
            cost = drink['cost']
            if money_paid >= cost:
                change = round(money_paid - cost, 2)
                machine_money += cost
                if change > 0:
                    print(f"Here is ${change} in change.")
                make_coffee(ques1, ingredients)
            else:
                print("Sorry, that's not enough money. Money refunded.")



    elif ques1 == "off":
                print("Machine turned off.")
                want_coffee = False

    else:
        print("Invalid selection.")

