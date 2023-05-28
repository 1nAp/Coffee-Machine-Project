#Imports resources and menu from the menu.py file
from menu import MENU, resources
import sys


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
                sys.exit()
    return resources_left










def operate_coffee_machine():
    money = 0
    price_of_beverage = 0
    global resources
    run_machine = True
    while run_machine:
        coffee_machine_action = input('What would you like? (espresso/latte/cappuccino): ')
        if coffee_machine_action == 'off':
            return
        elif coffee_machine_action == 'report':
            print_supplies(resources, money)
        else:
            resources = check_resources(resources, MENU[coffee_machine_action]['ingredients'])
            price_of_beverage = MENU[coffee_machine_action]['cost']














operate_coffee_machine()











# TODO: 1. Print report of all coffee machine resources

# TODO: 2. Check if resources are sufficient?

# TODO: 3. Process coins.

# TODO: 4. Check if transaction is successful?

# TODO: 5. Make coffee.