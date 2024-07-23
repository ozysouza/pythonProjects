from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
moneyMachine = MoneyMachine()

is_machine_on = True

while is_machine_on:
    coffee_type = input(f"What would you like? {menu.get_items()}: ").lower()
    if coffee_type == "report":
        coffeeMaker.report()
        moneyMachine.report()
    elif coffee_type == "off":
        is_machine_on = False
        print("Bye Bye!")
    else:
        drink = menu.find_drink(coffee_type)
        if coffeeMaker.is_resource_sufficient(drink) and moneyMachine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)


# from material import MENU, resources

# profit = 0
#
#
# def get_report():
#     """Returns the report with the amount for each material"""
#     global profit
#     qty_water = resources['water']
#     qty_milk = resources['milk']
#     qty_coffee = resources['coffee']
#     return f" Water: {qty_water}\n Milk: {qty_milk}\n Coffee: {qty_coffee}\n Profit: ${profit}"
#
#
# def check_resources(coffee_type):
#     """Get the ingredients required for the coffee type"""
#     required_ingredients = MENU[coffee_type]["ingredients"]
#
#     # Initialize a list to store insufficient ingredients
#     insufficient_ingredients = []
#
#     # Check if there are enough resources for each ingredient
#     for ingredient, amount in required_ingredients.items():
#         if resources.get(ingredient, 0) < amount:
#             insufficient_ingredients.append(ingredient)
#
#     # Check if there are enough resources for each ingredient
#     if insufficient_ingredients:
#         print(f"Not enough materials for {coffee_type}. Insufficient ingredients: {', '.join(insufficient_ingredients)}")
#         return False
#
#     print(f"Enough resources available to make {coffee_type}")
#     return True
#
#
# def update_resources(coffee_type):
#     required_ingredients = MENU[coffee_type]["ingredients"]
#
#     for ingredient, amount in required_ingredients.items():
#         resources[ingredient] -= amount
#
#
# def process_coins():
#     """Process the coins received by the user and return the change"""
#     print("Please insert coins.")
#     quarters = int(input("How manu quarters?: "))
#     dimes = int(input("How manu dimes?: "))
#     nickles = int(input("How manu nickles?: "))
#     pennies = int(input("How manu pennies?: "))
#     return float((quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01))
#
#
# def check_transaction(amount_received, coffee_type):
#     global profit
#     if amount_received >= MENU[coffee_type]["cost"]:
#         change = round(float(amount_received - MENU["cappuccino"]["cost"]), 2)
#     else:
#         return print("Sorry that's not enough money. Money refunded.")
#
#     profit += MENU[coffee_type]["cost"]
#     return print(f" Total Value received ${amount_received}\n Here is ${change} in change.\n"
#                  f"Here is your {coffee_type}. Enjoy!")
#
#
# def coffee_machine():
#     machine_power = True
#
#     while machine_power:
#         coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
#         if coffee_type == "report":
#             print(get_report())
#         elif coffee_type == "off":
#             machine_power = False
#             print("Bye Bye!")
#         elif check_resources(coffee_type):
#             amount_received = process_coins()
#             check_transaction(amount_received, coffee_type)
#             update_resources(coffee_type)
#
#
# coffee_machine()