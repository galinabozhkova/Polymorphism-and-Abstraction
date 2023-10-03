from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, refuel):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_quantity >= distance * (self.fuel_consumption + 0.9):
            self.fuel_consumption += 0.9
            self.fuel_quantity -= distance * self.fuel_consumption

    def refuel(self, refuel):
        self.fuel_quantity += refuel


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        if self.fuel_quantity >= distance * (self.fuel_consumption + 1.6):
            self.fuel_consumption += 1.6
            self.fuel_quantity -= distance * self.fuel_consumption

    def refuel(self, refuel):
        self.fuel_quantity += 0.95 * refuel
