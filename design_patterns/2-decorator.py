#!/usr/bin/env python3
"""
2-decorator.py: Implementing CaramelDecorator
for the coffee shop system.
"""

from abc import ABC, abstractmethod


class Beverage(ABC):
    """Abstract base class for beverages."""

    @abstractmethod
    def cost(self) -> int:
        pass

    @abstractmethod
    def description(self) -> str:
        pass


class Coffee(Beverage):
    """Base coffee beverage."""

    def cost(self) -> int:
        return 50

    def description(self) -> str:
        return "Coffee"


class BeverageDecorator(Beverage):
    """Base decorator for beverages."""

    def __init__(self, inner: Beverage):
        self._inner = inner


class MilkDecorator(BeverageDecorator):
    """Adds milk to a beverage."""

    def cost(self) -> int:
        return self._inner.cost() + 10

    def description(self) -> str:
        return self._inner.description() + " + milk"


class SugarDecorator(BeverageDecorator):
    """Adds sugar to a beverage."""

    def cost(self) -> int:
        return self._inner.cost() + 5

    def description(self) -> str:
        return self._inner.description() + " + sugar"


class CaramelDecorator(BeverageDecorator):
    """Adds caramel to a beverage."""

    def cost(self) -> int:
        return self._inner.cost() + 15

    def description(self) -> str:
        return self._inner.description() + " + caramel"


def main():
    beverage1 = MilkDecorator(Coffee())
    print(
        f"{beverage1.description()} "
        f"{beverage1.cost()}"
    )

    beverage2 = MilkDecorator(
        SugarDecorator(Coffee())
    )
    print(
        f"{beverage2.description()} "
        f"{beverage2.cost()}"
    )

    beverage3 = CaramelDecorator(
        MilkDecorator(
            SugarDecorator(Coffee())
        )
    )
    print(
        f"{beverage3.description()} "
        f"{beverage3.cost()}"
    )


if __name__ == "__main__":
    main()
