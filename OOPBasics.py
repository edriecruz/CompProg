class Vehicle:
    def __init__(self, make, model, year):
        self._make = make  
        self._model = model
        self._year = year
    
    def display_info(self):
        return f"{self._year} {self._make} {self._model}"
    
    def start_engine(self):
        raise NotImplementedError("Subclasses must implement this method") 

class SchoolBus(Vehicle):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year)
        self.__capacity = capacity
    
    def start_engine(self):
        return "Bus engine started with a loud roar!"
    
    def get_capacity(self):
        return self.__capacity

bus = SchoolBus("Blue Bird", "All American", 2020, 72)
print(isinstance(bus, Vehicle))