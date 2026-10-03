#!/usr/bin/env python3
"""
0-factory.py: Extending a vehicle factory registry with Scooter.
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):
    """Abstract base class for all vehicles."""

    @abstractmethod
    def mode(self) -> str:
        """Return the mode of transportation."""
        pass


class Bus(Vehicle):
    def mode(self) -> str:
        return "road"


class Train(Vehicle):
    def mode(self) -> str:
        return "rails"


class Bike(Vehicle):
    def mode(self) -> str:
        return "lane"


class Scooter(Vehicle):
    def mode(self) -> str:
        return "scooter_lane"


class VehicleFactory:
    """A factory that manages vehicle creation via a dynamic registry."""

    def __init__(self):
        self._registry = {}

    def register_kind(self, name: str, cls):
        """Registers a new vehicle class under a given string key."""
        self._registry[name] = cls

    def create(self, kind: str) -> Vehicle:
        """Creates an instance of the requested vehicle kind from the registry."""
        if kind not in self._registry:
            raise ValueError(f"Unknown vehicle kind: {kind}")
        return self._registry[kind]()


def main():
    factory = VehicleFactory()

    # Registering default types
    factory.register_kind("bus", Bus)
    factory.register_kind("train", Train)
    factory.register_kind("bike", Bike)

    # Registering the new scooter type as requested
    factory.register_kind("scooter", Scooter)

    # Testing the factory outputs
    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
