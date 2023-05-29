#Imports resources and menu from the menu.py file
from menu import MENU, resources


def print_supplies(resources, cash):
    """Prints the remaining resources to the console"""
    water_left = resources['water']
    milk_left = resources['milk']
    coffee_left = resources['coffee']
    print(f"Water: {water_left}ml\nMilk: {milk_left}ml\nCoffee: {coffee_left}g\nMoney: ${cash}")

def check_resources(resources_left, resources_required):
    """Subtracts resources from the total. If resources are insufficient, ends program."""
    for element in resources_left:
        if element in resources_required:
            if resources_left[element] >= resources_required[element]:
                resources_left[element] -= resources_required[element]
            else:
                print(f"Sorry, there is not enough {element}.")
                return False
    return resources_left

def process_coins():
    """Prompts user to insert coins and calculates the sum."""
    money = 0
    coins = {'quarters': 0.25, 'dimes': 0.10, 'nickles': 0.05, 'pennies': 0.01}
    print("Please insert coins.")

    for coin in coins:
        money += (int(input(f"How many {coin}?: "))) * (coins[coin])
    return money

def operate_coffee_machine():
    """Operates the coffee_machine and keeps track of profit and resources."""
    total_money = 0
    global resources
    while True:
        # Either attempts to order one of three choices of drink, switches the coffee machine off, or reports supplies
        # remaining.
        coffee_machine_action = input('What would you like? (espresso/latte/cappuccino): ')
        if coffee_machine_action == 'off':
            return
        elif coffee_machine_action == 'report':
            print_supplies(resources, total_money)
        else:
            resources = check_resources(resources, MENU[coffee_machine_action]['ingredients'])
            if resources == False:
                return
            price_of_beverage = MENU[coffee_machine_action]['cost']
            money = process_coins()
            if money < price_of_beverage:
                print("Sorry, that's not enough money. Money refunded.")
                for key in MENU[coffee_machine_action]['ingredients']:
                    resources[key] += MENU[coffee_machine_action]['ingredients'][key]
            else:
                total_money += price_of_beverage
                change = round(money - price_of_beverage, 2)
                if change > 0:
                    print(f'Here is ${change} in change.')
                print(f'Here is your {coffee_machine_action}. Enjoy!')


operate_coffee_machine()











# TODO: 1. Print report of all coffee machine resources DONE

# TODO: 2. Check if resources are sufficient? DONE

# TODO: 3. Process coins. DONE

# TODO: 4. Check if transaction is successful? DONE

# TODO: 5. Make coffee. DONE