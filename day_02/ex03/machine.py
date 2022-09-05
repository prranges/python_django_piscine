#!/usr/local/bin/python3

import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino


class CoffeeMachine:
    def __init__(self) -> None:
        self.cups_to_serv = 10

    class EmptyCup(HotBeverage):
        def __init__(self) -> None:
            super().__init__()
            self.name = "empty cup"
            self.price = 0.90

        def description(self) -> str:
            return "An empty cup?! Gimme my money back!"

    class BrokenMachineException(Exception):
        def __init__(self) -> None:
            super().__init__("This coffee machine has to be repaired.")

    def repair(self) -> None:
        self.cups_to_serv = 10

    def serve(self, beverage: HotBeverage()) -> HotBeverage():
        if self.cups_to_serv:
            self.cups_to_serv -= 1
            if not random.randint(0, 7):
                return CoffeeMachine.EmptyCup()
            return beverage()
        else:
            raise CoffeeMachine.BrokenMachineException


def main():
    coffee_machine = CoffeeMachine()
    beverages = [Coffee, Tea, Chocolate, Cappuccino]
    for i in range(25):
        try:
            print(coffee_machine.serve(random.choice(beverages)))
        except CoffeeMachine.BrokenMachineException as e:
            print(e)
            coffee_machine.repair()


if __name__ == '__main__':
    main()
