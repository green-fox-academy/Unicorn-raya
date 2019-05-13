# Petrol Station
# Create Station and Car classes
# Station
# gas_amount
# refill(car) -> decreases the gasAmount by the capacity of the car and increases the cars gas_amount
# Car
# gas_amount
# capacity
# create constructor for Car where:
# initialize gas_amount -> 0
# initialize capacity -> 100

class Station(object):
    def __init__(self):
        self.gas_amount = 100000

    def refill(self,car,gas_amount):
        self.gas_amount -= gas_amount
        car.add_gas(gas_amount)

    def get_station_gasAmount(self):
        print(f'current stataion gas amount is: {self.gas_amount}')


class Car(object):
    def __init__(self,gas_amount = 0,capacity = 100):
        self.gas_amount = gas_amount
        self.capacity = capacity

    def add_gas(self,gas_amount):
        self.gas_amount += gas_amount
    
    def get_gas(self):
        print(f"current gas amount is: {self.gas_amount}")
    

station = Station()
car = Car()

station.get_station_gasAmount()
car.get_gas()   
station = Station()
car = Car()
station.refill(car,100)
station.get_station_gasAmount()
car.get_gas()



