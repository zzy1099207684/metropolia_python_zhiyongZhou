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


class Building:
    def __init__(self, bottomFloorNum, topFloorNum,numberOfElevators):
        self.numberOfElevators = numberOfElevators;
        self.elevators = [];
        for i in range(numberOfElevators):
            self.elevators.append(Elevator(bottomFloorNum, topFloorNum));


    def run_elevator(self, numberOfTheElevator, destinationFloor):
        print(f"U choose No.{numberOfTheElevator} elevator");
        ele = self.elevators[numberOfTheElevator-1];
        ele.go_to_floor(destinationFloor);


    # Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all elevators to the bottom floor.
    # Continue the main program by causing a fire alarm in your building.
    def fire_alarm(self):
        print("\nfire alarm, all elevators to the bottom floor! ! !")
        numberOfTheElevator = len(self.elevators)
        for i in range(numberOfTheElevator):
            ele = self.elevators[i];
            ele.go_to_floor(ele.bottomFloorNum);
        print(f"elevators No.{i+1} have arrived the bottom floor! ! !")


if (__name__ == "__main__"):
    build = Building(1, 10, 2);
    build.run_elevator(1, 3);
    build.run_elevator(2, 9);
    time.sleep(1)
    build.fire_alarm();