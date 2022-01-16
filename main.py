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
def coins():
    """Returns total from inserted coins"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.1
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total
def resource_sufficient(order_ingredients):
    """Returns True when order can be made and False when ingrdients are sufficient"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
           print(f"Sorry there is not enough {item}.")
           return False
    return True
def transaction_successful(money_received,drink_cost):
     """Return True when payment is successful, or False if money is insufficient."""
     if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"Here is your change ${change} and {choice}")
        global profit
        profit += drink_cost
        return True
     else:
        print("Sorry that's not enough money, Money refunded.")
        return False
def make_coffee(order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {choice} ☕ ")
need_coffee = True
profit = 0
while need_coffee:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        need_coffee = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")
    else:
        drink = MENU[choice]
        if resource_sufficient(drink["ingredients"]):
            payment = coins()
            if transaction_successful(payment,drink['cost']):
                make_coffee(choice,drink['ingredients'])
