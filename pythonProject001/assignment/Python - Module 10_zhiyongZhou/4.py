import random
import tabulate
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
# This exercise continues the previous car race exercise from the last exercise set.
# Write a Race class that has the following properties: name, distance in kilometers and a list of cars participating in the race.
# The class has an initializer that receives the name, kilometers, and car list as parameters and sets their values to the corresponding properties in the class.
# The class has the following methods:
    # hour_passes, which performs the operations done once per hour in the original exercise: generates a random change of speed for each car and calls their drive method.
    # print_status, which prints out the current information of each car as a clear, formatted table.
class Race:
    def __init__(self, name, kilometers, carList):
        self.name = name;
        self.kilometers = kilometers;
        self.carList = carList;
        self.advanced = 0;

    def hour_passes(self):
        for i in self.carList:
            i.accerelate(random.randint(-10, 15));
            i.drive(1);
            if (i.travelledDistance >= self.advanced):
                self.advanced = i.travelledDistance;

    def print_status(self):
        datas = [];
        headers = ["registrationNumber", "maximumSpeed", "currentSpeed", "travelledDistance"]
        for i in self.carList:
            datas.append([i.registrationNumber, i.maximumSpeed, i.currentSpeed, i.travelledDistance]);
        table = tabulate.tabulate(datas, headers, tablefmt="pretty");
        print(table);

    def race_finished(self):
        if(self.advanced >= self.kilometers):
            return True;


# Write a main program that creates an 8000-kilometer race called Grand Demolition Derby.
# The new race is given a list of ten cars similarly to the earlier exercise.
# The main program simulates the progressing of the race by calling the hour_passes in a loop,
# after which it uses the race_finished method to check if the race has finished.
# The current status is printed out using the print_status method every ten hours and then once more at the end of the race.
if __name__ == '__main__':
    carList =[];
    for i in range(10):
        carList.append(Car(f"ABC-{i+1}", random.randint(100, 200)))

    GrandDemolitionDerby = Race('ABC',8000,carList);
    hours = 0;
    while (GrandDemolitionDerby.advanced < GrandDemolitionDerby.kilometers):
        GrandDemolitionDerby.hour_passes();
        hours += 1;
        # The current status is printed out using the print_status method every ten hours and then once more at the end of the race.
        if (hours == 10):
            GrandDemolitionDerby.print_status();
            hours = 0;
        elif(GrandDemolitionDerby.race_finished()):
            print("the race is end 👇")
            GrandDemolitionDerby.print_status();
            break;


