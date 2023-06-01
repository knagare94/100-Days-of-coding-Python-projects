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

profit = 0


def coin():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    sum = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    if coffee_type == "espresso":
        if sum >= 1.5:
            change = round(sum - 1.5, 2)
            print(f"Here is {change} in change.")
            print("Here is your espresso ☕. Enjoy!")
            global profit
            profit += 1.5
        else:
            print("Sorry that's not enough money. Money refunded.")

    if coffee_type == "latte":
        if sum >= 2.5:
            change = round(sum - 2.5, 2)
            print(f"Here is {change} in change.")
            print("Here is your latte ☕. Enjoy!")
            profit += 2.5
        else:
            print("Sorry that's not enough money. Money refunded.")

    if coffee_type == "cappuccino":
        if sum >= 3.0:
            change = round(sum - 3.0, 2)
            print(f"Here is {change} in change.")
            print("Here is your cappuccino ☕. Enjoy!")
            profit += 3.0
        else:
            print("Sorry that's not enough money. Money refunded.")


def is_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]


is_on = True
while is_on:
    coffee_type = input("What would you like? (espresso/latte/cappuccino):")
    if coffee_type == "espresso" or coffee_type == "latte" or coffee_type == "cappuccino":
        drink = MENU[coffee_type]
        if is_resources(drink["ingredients"]):
            print("Please insert coin.")
            coin()
            make_coffee(coffee_type, drink["ingredients"])
    elif coffee_type == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif coffee_type == "off":
        is_on = False
    else:
        is_on = False




