import random
class Car:
    def __init__(self, registrationNumber, maximumSpeed):
        self.registrationNumber = registrationNumber;
        self.maximumSpeed = maximumSpeed;
        self.currentSpeed = 0;
        self.travelledDistance = 0;

    def accerelate(self, changeOfSpeed):
        self.currentSpeed = self.currentSpeed + changeOfSpeed
        if(self.currentSpeed > self.maximumSpeed):
            self.currentSpeed = self.maximumSpeed;
        elif(self.currentSpeed < 0):
            self.currentSpeed = 0;
        return self.currentSpeed;

    def drive(self, time):
        self.travelledDistance +=(self.currentSpeed * time)
        return self.travelledDistance;
# Extend the previosly written Car class by adding two subclasses: ElectricCar and GasolineCar.
# Electric cars have the capacity of the battery in kilowatt-hours as their property.
# Gasoline cars have the volume of the tank in liters as their property. Write initializers for the subclasses.
# For example, the initializer of electric cars receives the registration number, maximum speed and battery capacity as its parameter.
# It calls the initializer of the base class to set the first two properties and then sets its capacity.
# Write a main program where you create one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l).
# Select speeds for both cars, make them drive for three hours and print out the values of their kilometer counters.
class ElectricCar(Car):
    def __init__(self, registrationNumber, maximumSpeed, batteryCapacity):
            super().__init__(registrationNumber, maximumSpeed);
            self.batteryCapacity = batteryCapacity;

class GasolineCar(Car):
    def __init__(self, registrationNumber, maximumSpeed, tankVolume):
        super().__init__(registrationNumber, maximumSpeed);
        self.tankVolume = tankVolume;

if __name__ == '__main__':
    eCar = ElectricCar('ABC-15', 180, 52.5);
    gCar = GasolineCar('ACD-123', 165, 32.3);
    eCar.accerelate(random.randint(0,180));
    gCar.accerelate(random.randint(0,165));
    print(eCar.drive(3));
    print(gCar.drive(3));
