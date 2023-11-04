import random
import tabulate


class Car:
    def __init__(self, registrationNumber, maximumSpeed):
        self.registrationNumber = registrationNumber;
        self.maximumSpeed = maximumSpeed;
        self.currentSpeed = 0;
        self.travelledDistance = 0;

    # 2.
    # Extend the program by adding an accerelate method into the new class.
    # The method should receive the change of speed (km/h) as a parameter.
    # If the change is negative, the car reduces speed.
    # The method must change the value of the speed property of the object.
    # The speed of the car must stay below the set maximum and cannot be less than zero.
    # Extend the main program so that the speed of the car is first increased by +30 km/h,
    # then +70 km/h and finally +50 km/h. Then print out the current speed of the car.
    # Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed.
    # The travelled distance does not have to be updated yet.
    def accerelate(self, changeOfSpeed):
        self.currentSpeed = self.currentSpeed + changeOfSpeed
        if(self.currentSpeed > self.maximumSpeed):
            self.currentSpeed = self.maximumSpeed;
        elif(self.currentSpeed < 0):
            self.currentSpeed = 0;
        return self.currentSpeed;

    # 3.
    # Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
    # The method increases the travelled distance by how much the car has travelled in constant speed in the given time.
    # Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h.
    # Method call car.drive(1.5) increases the travelled distance to 2090 km.
    def drive(self, time):
        self.travelledDistance +=(self.currentSpeed * time)
        return self.travelledDistance;




# 1.
# Write a Car class that has the following properties: registration number, maximum speed, current speed and travelled distance.
# Add a class initializer that sets the first two of the properties based on parameter values.
# The current speed and travelled distance of a new car must be automatically set to zero.
# Write a main program where you create a new car (registration number ABC-123, maximum speed 142 km/h).
# Finally, print out all the properties of the new car.

car = Car('ABC-123', 142)
print("registrationNumber: ",car.registrationNumber,'\n',"maximumSpeed: ",car.maximumSpeed,'\n',"currentSpeed: ",car.currentSpeed,'\n'"travelledDistance: ",car.travelledDistance)

# 2.
# Extend the main program so that the speed of the car is first increased by +30 km/h,
# then +70 km/h and finally +50 km/h. Then print out the current speed of the car.
# Finally, use the emergency brake by forcing a -200 km/h change on the speed and then print out the final speed.
# The travelled distance does not have to be updated yet.
if (__name__ == "__main__"):
    car.accerelate(30);
    car.accerelate(70);
    car.accerelate(50);
    print("\ncurrentSpeed: ",car.currentSpeed);
    car.accerelate(-200);
    print("final speed: ",car.currentSpeed);

# 3.
# Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h.
# Method call car.drive(1.5) increases the travelled distance to 2090 km.
if (__name__ == "__main__"):
    car.accerelate(60);
    car.travelledDistance = 2000;
    travelledDistance = car.drive(1.5);
    print(f"travelled distance: {travelledDistance}\n");

# 4.
# Now we will program a car race. The travelled distance of a new car is initialized as zero.
# At the beginning of the main program, create a list that consists of 10 car objects created using a loop.
# The maximum speed of each new car is a random value between 100 km/h and 200 km/h.
# The registration numbers are created as follows: "ABC-1", "ABC-2" and so on.
# Now the race begins. One per every hour of the race, the following operations are performed:
    #The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This is done using the accerelate method.
    #Each car is made to drive for one hour. This is done with the drive method.
# The race continues until one of the cars has advanced at least 10,000 kilometers.
# Finally, the properties of each car are printed out formatted into a clear table.
if (__name__ == "__main__"):
    carList = [];
    for i in range(10):
        carList.append(Car(f"ABC-{i}", random.randint(100, 200)));

    advanced = 0;
    while (advanced < 10000):
        for i in carList:
            i.accerelate(random.randint(-10, 15));
            i.drive(1);
            if(i.travelledDistance >= advanced):
                advanced = i.travelledDistance;

    datas = [];
    headers = ["registrationNumber","maximumSpeed","currentSpeed","travelledDistance"]
    for i in carList:
        datas.append([i.registrationNumber, i.maximumSpeed, i.currentSpeed, i.travelledDistance]);
    table = tabulate.tabulate(datas, headers, tablefmt="pretty");
    print(table);





