class Car:
    def __init__(self, make: str, model: str, year: int, max_speed: int, fuel_level=100, fuel_capacity=100) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.fuel_level = fuel_level
        self.fuel_capacity = fuel_capacity
    
    def __str__(self) -> str:
        return "this is Car object"
        
    def drive_car(self):
        pass
    
    def stop_car(self):
        pass
    
    def caculate_fuel(self, distance):
        pass
    
    def add_fuel(self, amount):
        pass