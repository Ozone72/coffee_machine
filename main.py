MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

bank = {
    "coins":
        {
            "quarter": .25,
            "dime": .10,
            "nickel": .05,
            "penny": .01},
    "balance": 0
}


def coffee_machine():
    command = input("What would you like? (espresso/latte/cappuccino):")
    if command != "espresso" and command != "latte" and command != "cappuccino":
        if command != "off" and command != "report":
            print("Input is not recognized.  Try again")
            coffee_machine()
        elif command == "report":
            report()
        elif command == "off":
            exit()

    else:
        make_drink(command)


def report():
    for item in resources:
        print(f"{item.capitalize()}: {resources[item]}")
    print(f"Money: ${bank['balance']}")
    coffee_machine()


def make_drink(drink):
    drink_ingredients = {}
    for key, val in MENU[drink]["ingredients"].items():
        drink_ingredients[key] = val
    common_keys = set(drink_ingredients.keys()).intersection(set(set(resources.keys())))
    for key in common_keys:
        if drink_ingredients[key] > resources[key]:
            print(f"Sorry there is not enough {resources[key]}")
            coffee_machine()
    print(f"Please insert ${MENU[drink]['cost']}")
#     TODO Need to create a function that takes coins and adds up amount, compares to cost, either returns drink
#      or change, or not enough

#     TODO Adds coins to bank total
#     TODO Subtracts ingredients from resources dict
