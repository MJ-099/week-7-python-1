class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# List of vehicles
vehicles = [Car(), Plane(), Boat()]

# Demonstrate polymorphism: same method, different behavior
for vehicle in vehicles:
    vehicle.move()
