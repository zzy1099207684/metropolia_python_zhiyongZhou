import time
class Elevator:
    def __init__(self,bottomFloorNum, topFloorNum):
        self.bottomFloorNum = bottomFloorNum;
        self.topFloorNum = topFloorNum;
        self.elevatorCurrentFloor = bottomFloorNum;

    def go_to_floor(self, targetNum):
        if(targetNum > self.topFloorNum and targetNum < self.bottomFloorNum):
            print("invalid put");
            return;
        if (self.elevatorCurrentFloor < targetNum):
            self.floor_up(targetNum);
        elif(self.elevatorCurrentFloor > targetNum):
            self.floor_down(targetNum);
        self.elevatorCurrentFloor = targetNum;

    def floor_up(self,targetNum):
        for i in range(self.elevatorCurrentFloor, targetNum+1, 1):
            time.sleep(1);
            print(f"the elevator in: {i} floor now");
            if (i == targetNum):
                print(f"the elevator arrived target floor");

    def floor_down(self, targetNum):
        for i in range(self.elevatorCurrentFloor, targetNum-1, -1):
            time.sleep(1);
            print(f"the elevator in: {i} floor now");
            if (i == targetNum):
                self.elevatorCurrentFloor = i;
                print(f"the elevator arrived target floor {i}");


# Extend the previous program by creating a Building class.
# The initializer parameters for the class are the numbers of the bottom and top floors and the number of elevators in the building.
# When a building is created, the building creates the required number of elevators. The list of elevators is stored as a property of the building.
# Write a method called run_elevator that accepts the number of the elevator and the destination floor as its parameters.
# In the main program, write the statements for creating a new building and running the elevators of the building.
class Building:
    def __init__(self, bottomFloorNum, topFloorNum,numberOfElevators):
        self.numberOfElevators = numberOfElevators;
        self.elevators = [];
        for i in range(numberOfElevators):
            self.elevators.append(Elevator(bottomFloorNum, topFloorNum));


    def run_elevator(self, numberOfTheElevator, destinationFloor):
        print(f"U choose No.{numberOfTheElevator} elevator")
        ele = self.elevators[numberOfTheElevator-1]
        ele.go_to_floor(destinationFloor);




if (__name__ == "__main__"):
    build = Building(1,10,2);
    build.run_elevator(1, 3);
    build.run_elevator(2, 9);