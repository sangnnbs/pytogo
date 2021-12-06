# OOP Exercise 1: Create a Class with instance attributes
class Vehicle:
    
    color = 'white'
    
    def __init__(self,name , max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage
        self.name   = name

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

    def fare(self):
        return self.capacity * 100
    
myVehicle = Vehicle("Pres", 150, 19)


# OOP Exercise 2: Create a Vehicle class without any variables and methods
class Vehicle2:
    pass

# OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Bus(Vehicle):
    pass

# OOP Exercise 4: Class Inheritance

class Bus4(Vehicle):
    def seating_capacity(self):
        return super().seating_capacity(capacity=50)

# OOP Exercise 6: Class Inheritance

class Bus6(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

# OOP Exercise 7: Check type of an object

