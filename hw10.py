from abc import ABC, abstractmethod

# Abstract Base Class
class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year

    # Concrete method
    def account_age(self):
        return 2025 - self.account_year

    # Abstract method
    @abstractmethod
    def get_role(self):
        pass


# Admin subclass
class Admin(User):
    def get_role(self):
        return "Admin"

    def __str__(self):
        return f"{self.name} is an Admin user with an account age of {self.account_age()} years."


# Guest subclass
class Guest(User):
    def get_role(self):
        return "Guest"

    def __str__(self):
        return f"{self.name} is a Guest user with an account age of {self.account_age()} years."


# Creating objects
admin_user = Admin("Alice", 2020)
guest_user = Guest("Bob", 2023)

# Printing role, account age, and object message
print("Admin Role:", admin_user.get_role())
print("Admin Account Age:", admin_user.account_age(), "years")
print(admin_user)

print()

print("Guest Role:", guest_user.get_role())
print("Guest Account Age:", guest_user.account_age(), "years")
print(guest_user)