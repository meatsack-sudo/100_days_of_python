from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

keep_going = True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


possible_drinks = menu.get_items()

# print(possible_drinks)

while keep_going:
    user_choice = input(f"What would you like? {menu.get_items()}: ")

    if user_choice.lower() == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_choice.lower() == "off":
        break

    #menu.find_drink(user_choice)
    drink = menu.find_drink(user_choice)

    if user_choice in ["espresso", "latte", "cappuccino"]:
        if coffee_maker.is_resource_sufficient(drink):
            print("Resources sufficient")
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)










# while keep_going:
#     user_choice = input("What would you like? (espresso/latte/cappuccino): ")

#     if user_choice.lower() == "off":
#         keep_going = False
#         break

#     if user_choice.lower() == "report":
#         print_report()

#     if user_choice.lower() in MENU.keys():
#         if check_resources(MENU[user_choice]["ingredients"]["water"], MENU[user_choice]["ingredients"]["milk"], MENU[user_choice]["ingredients"]["coffee"]):
#             reduce_resources(MENU[user_choice]["ingredients"]["water"], MENU[user_choice]["ingredients"]["milk"], MENU[user_choice]["ingredients"]["coffee"])
#             quarters, dimes, nickels, pennies = prompt_coins()
#             if float(count_coins(quarters, dimes, nickels, pennies)) >= MENU[user_choice]["cost"]:
#                 change = count_coins(quarters, dimes, nickels, pennies) - MENU[user_choice]["cost"]
#                 if change > 0.00:
#                     print(f"Here is {('${:,.2f}'.format(change))} in change.")
#                 current_money += MENU[user_choice]["cost"]
#             else:
#                 print("Sorry that's not enough money. Money refunded.")