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
    "water": [300, "ml"],
    "milk": [200, "ml"],
    "coffee": [100, "g"],
    "money": [0, "$"]
}


def get_menu():
    result = "/".join(MENU.keys())
    return result


def get_report():
    report = ""
    for key, value in resources.items():
        report += f'{key.capitalize()}: {value[0]}{value[1]}\n'
    return report


def check_resources(checked_resources: dict):
    not_enough = []
    for resource in checked_resources.keys():
        if resource in resources.keys():
            if checked_resources[resource] > resources[resource][0]:
                not_enough.append(resource)

    if not_enough:
        print(f"Sorry there is not enough {' and '.join(not_enough)}.")
        return False
    return True


def make_coffee(coffee_name):
    coffee = MENU[coffee_name]
    for ingredient, value in coffee['ingredients'].items():
        resources[ingredient][0] -= value


def get_money(price):
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    money_sum = quarters * 0.25 + dimes * 0.10 + nickles * 0.5 + pennies * 0.01
    if money_sum > price:
        print(f"Here is ${money_sum - price} in change.")
    resources["money"][0] += price
    return money_sum


def start_machine():
    in_progress = True
    while in_progress:
        answer = input(f"What would you like? ({get_menu()}): ")
        if answer == 'report':
            print(get_report())

        elif answer == 'exit':
            in_progress = False

        elif answer in MENU.keys():
            if check_resources(MENU[answer]['ingredients']):
                if get_money(MENU[answer]["cost"]) > MENU[answer]["cost"]:
                    make_coffee(answer)
                else:
                    print("Not enough money!")
        else:
            print('WTF!')


if __name__ == '__main__':
    start_machine()
