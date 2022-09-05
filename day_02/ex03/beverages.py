#!/usr/local/bin/python3

class HotBeverage:
    def __init__(self) -> None:
        self.name = "hot beverage"
        self.price = 0.30

    def description(self) -> str:
        return "Just some hot water ina cup"

    def __str__(self) -> str:
        return "name : " + self.name + \
               "\nprice : " + \
               "{0:.2f}".format(self.price) + \
               "\ndescription : " + self.description()


class Coffee(HotBeverage):
    def __init__(self) -> None:
        super().__init__()
        self.name = "coffee"
        self.price = 0.40

    def description(self) -> str:
        return "A coffee to stay awake."


class Tea(HotBeverage):
    def __init__(self) -> None:
        super().__init__()
        self.name = "tea"
        self.price = 0.30


class Chocolate(HotBeverage):
    def __init__(self) -> None:
        super().__init__()
        self.name = "chocolate"
        self.price = 0.50

    def description(self) -> str:
        return "Chocolate, sweet chocolate..."


class Cappuccino(HotBeverage):
    def __init__(self) -> None:
        super().__init__()
        self.name = "cappuccino"
        self.price = 0.45

    def description(self) -> str:
        return "Un po’ di Italia nella sua tazza!"
