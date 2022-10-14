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


def espresso(water_machine, coffee_machine, money_machine):
    espresso_cup = MENU['espresso']
    new_water_value = water_machine - espresso_cup['ingredients']['water']
    new_coffee_value = coffee_machine - espresso_cup['ingredients']['coffee']
    new_money = money_machine + espresso_cup['cost']
    return new_water_value, new_coffee_value, new_money


def latte(water_machine, coffee_machine, milk_machine, money_machine):
    latte_cup = MENU['latte']
    new_water_value = water_machine - latte_cup['ingredients']['water']
    new_milk_value = milk_machine - latte_cup['ingredients']['milk']
    new_coffee_value = coffee_machine - latte_cup['ingredients']['coffee']
    new_money = money_machine + latte_cup['cost']
    return new_water_value,  new_milk_value, new_coffee_value, new_money


def cappuccino(water_machine, coffee_machine, milk_machine, money_machine):
    cappuccino_cup = MENU['cappuccino']
    new_water_value = water_machine - cappuccino_cup['ingredients']['water']
    new_milk_value = milk_machine - cappuccino_cup['ingredients']['milk']
    new_coffee_value = coffee_machine - cappuccino_cup['ingredients']['coffee']
    new_money = money_machine + cappuccino_cup['cost']
    return new_water_value,  new_milk_value, new_coffee_value, new_money


def report():
    print(f"Water: {water}")
    print(f"Milk: {milk}")
    print(f"Coffee: {coffee}")
    print(f"Money: {money}")


def refund():
    new_water = 300
    new_milk = 200
    new_coffee = 100
    return new_water, new_milk, new_coffee


def check_money():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01


water = 300
milk = 200
coffee = 100
money = 0
machine_on = True

while machine_on:
    user_input = input("What would yoy like? (espresso/latte/cappuccino): ").lower()
    if user_input == 'espresso':
        if water < 50:
            print("Not enough water, please type refund.")
            continue
        elif coffee < 18:
            print("Not enough coffee, please type refund.")
            continue
        paid = check_money()
        espresso_cost = MENU['espresso']['cost']
        exchange = round(paid-espresso_cost, 2)
        if exchange < 0:
            print("You don't have enough money.")
            continue
        print(f"Here's your exchange: {exchange}")
        water, coffee, money = espresso(water, coffee, money)
        print("Here's your espresso☕, enjoy")
    elif user_input == 'latte':
        if water < 200:
            print("Not enough water, please type refund.")
            continue
        elif coffee < 24:
            print("Not enough coffee, please type refund.")
            continue
        elif milk < 150:
            print("Not enough milk, please type refund.")
            continue
        paid = check_money()
        latte_cost = MENU['latte']['cost']
        exchange = round(paid - latte_cost, 2)
        if exchange < 0:
            print("You don't have enough money.")
            continue
        print(f"Here's your exchange: {exchange}")
        water, milk, coffee, money = latte(water, coffee, milk, money)
        print("Here's your latte☕, enjoy")
    elif user_input == 'cappuccino':
        if water < 250:
            print("Not enough water, please type refund.")
            continue
        elif coffee < 24:
            print("Not enough coffee, please type refund.")
            continue
        elif milk < 100:
            print("Not enough milk, please type refund.")
            continue
        paid = check_money()
        cappuccino_cost = MENU['espresso']['cost']
        exchange = round(paid - cappuccino_cost, 2)
        if exchange < 0:
            print("You don't have enough money.")
            continue
        print(f"Here's your exchange: {exchange}")
        water, milk, coffee, money = cappuccino(water, coffee, milk, money)
        print("Here's your cappuccino☕, enjoy")
    elif user_input == 'report':
        report()
    elif user_input == 'off':
        print("The machine has stopped.")
        machine_on = False
        break
    elif user_input == 'refund':
        water, milk, coffee = refund()
        print("Machine has been refunded.")
    else:
        print("Please insert valid order.")
