from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, joining_year):
        self.name = name
        self.joining_year = joining_year

    def years_on_platform(self):
        return 2025 - self.joining_year

    @abstractmethod
    def get_role(self):
        pass

    def display(self):
        print(f"Name: {self.name}")
        print(f"Role: {self.get_role()}")
        print(f"Years on Platform: {self.years_on_platform()}")
        print()


class Customer(User):
    def get_role(self):
        return "Customer"


class Vendor(User):
    def get_role(self):
        return "Vendor"


customer1 = Customer("Rahna", 2020)
vendor1 = Vendor("Rasana", 2018)

customer1.display()
vendor1.display()