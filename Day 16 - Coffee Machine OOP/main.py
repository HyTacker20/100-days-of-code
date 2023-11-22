from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


class CoffeeMachine:
    def __init__(self):
        self.menu = Menu()
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()

    def start(self):
        in_progress = True
        while in_progress:
            answer = input(f"What would you like? ({self.menu.get_items()}): ")
            if answer == 'report':
                self.coffee_maker.report()
                self.money_machine.report()

            elif answer == 'exit':
                in_progress = False

            elif self.menu.find_drink(answer):
                drink = self.menu.find_drink(answer)
                if self.coffee_maker.is_resource_sufficient(drink):
                    self.coffee_maker.make_coffee(drink) if self.money_machine.make_payment(drink.cost) else None
            else:
                print('WTF!')


if __name__ == '__main__':
    coffee_machine = CoffeeMachine()
    coffee_machine.start()

