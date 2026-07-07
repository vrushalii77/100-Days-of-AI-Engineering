# Show important things and hide implementation details.
# Think about a car.
# You know:
# Start
# Brake
# Accelerate

# You don't know:
# Engine timing
# Fuel injection
# Piston movement

# This is abstraction.

from abc import ABC, abstractmethod
class Vehical(ABC):

    @abstractmethod
    def start(self):
       pass
class Car:
    def start(self):
        print("Bike has started")
c1 = Car()
c1.start()