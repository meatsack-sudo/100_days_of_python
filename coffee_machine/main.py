MENU = {
    "espresso": {
        "ingredients": {
            "milk": 0,
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

# TODO: #1 Print a report of all of the coffee machine resources.

def print_report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {('${:,.2f}'.format(current_money))}")


# TODO: #2 Check resources and make sure there's enough for the drink

def check_resources(water=int, milk=int, coffee=int):
    if water <= resources["water"]:

        if milk <= resources["milk"]:

            if coffee <= resources["coffee"]:
                return True
            
            else:
                print("Not enough coffee")
        else:
            print("Not enough milk.")
    else:
        print(f"Not enough water.")


# TODO: #3 Process coins

def count_coins(quarters=int, dimes=int, nickels=int, pennies=int):
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * .01)
    return float(('{:,.2f}'.format(total)))

#print(count_coins(4, 4, 4, 4))

def prompt_coins():
    quarters = int(input("Insert quarters: "))
    dimes = int(input("Insert dimes: "))
    nickels = int(input("Insert nickels: "))
    pennies = int(input("Insert pennies: "))
    return(quarters, dimes, nickels, pennies)

# TODO: #4 Check that the transaction was successfuly

#if check_resources(water, milk, coffee):

def reduce_resources(water, milk, coffee):
    resources["water"] -= water
    resources["milk"] -= milk
    resources["coffee"] -= coffee

# TODO: #5 Make coffee

current_money = 0

keep_going = True

while keep_going:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice.lower() == "off":
        keep_going = False
        break

    if user_choice.lower() == "report":
        print_report()

    if user_choice.lower() in MENU.keys():
        if check_resources(MENU[user_choice]["ingredients"]["water"], MENU[user_choice]["ingredients"]["milk"], MENU[user_choice]["ingredients"]["coffee"]):
            reduce_resources(MENU[user_choice]["ingredients"]["water"], MENU[user_choice]["ingredients"]["milk"], MENU[user_choice]["ingredients"]["coffee"])
            quarters, dimes, nickels, pennies = prompt_coins()
            if float(count_coins(quarters, dimes, nickels, pennies)) >= MENU[user_choice]["cost"]:
                change = count_coins(quarters, dimes, nickels, pennies) - MENU[user_choice]["cost"]
                if change > 0.00:
                    print(f"Here is {('${:,.2f}'.format(change))} in change.")
                current_money += MENU[user_choice]["cost"]
            else:
                print("Sorry that's not enough money. Money refunded.")
  


