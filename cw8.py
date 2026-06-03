class Vehicle:
    def __init__(self, vehicle_id, base_rate):
        self._vehicle_id = vehicle_id
        self._base_rate = base_rate

    def display_details(self):
        print("Vehicle ID:", self._vehicle_id)
        print("Base Rate:", self._base_rate)

    def rental_charge(self):
        return 0.0


class Car(Vehicle):
    def __init__(self, vehicle_id, base_rate, num_seats):
        self._vehicle_id = vehicle_id
        self._base_rate = base_rate
        self.num_seats = num_seats

    def rental_charge(self):
        return self._base_rate * self.num_seats


car = Car("CAR001", 100.0, 4)

class Bike(Vehicle):
    def __init__(self, vehicle_id, base_rate, bike_type):
        self._vehicle_id = vehicle_id
        self._base_rate = base_rate
        self.bike_type = bike_type

    def rental_charge(self):
        return self._base_rate * 0.5


def calculate_rental(vehicle):
    return vehicle.rental_charge()

bike = Bike("BIKE001", 100.0, "Scooter")

print("Car Details")
car.display_details()
print("Number of Seats:", car.num_seats)
print("Rental Charge:", calculate_rental(car))

print("Bike Details")
bike.display_details()
print("Bike Type:", bike.bike_type)
print("Rental Charge:", calculate_rental(bike))