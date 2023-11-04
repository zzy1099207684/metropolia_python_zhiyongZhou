import time
# Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
# The elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor.
# If you make elevator h for example the method call h.go_to_floor(5), the method calls either the floor_up or floor_down methods as many times as it needs to get to the fifth floor.
# The methods run the elevator one floor up or down and tell what floor the elevator is after each move.
# Test the class by creating an elevator in the main program, tell it to move to a floor of your choice and then back to the bottom floor.
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
                print(f"the elevator arrived target floor");

#main
if (__name__ == "__main__"):
    elevator = Elevator(1,10);
    elevator.go_to_floor(5);
    elevator.go_to_floor(1)
