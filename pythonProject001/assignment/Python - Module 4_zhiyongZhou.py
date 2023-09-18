
import random
import math
# Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.
i = 1;
divisor = 3;
divisition = 3;
numList = [];
while (i <= 1000):
    if (i % divisor == 0):
        numList.append(i);
    i += 1;
print("numbers divisible by three: ", numList);

# Write a program that converts inches to centimeters until the user inputs a negative value.
# Then the program ends.
incheNum = float(input("input inches number(negative express end):"));
while (incheNum >= 0):
    centimeterNum = incheNum * 2.54;
    print("retult is:", centimeterNum, "cm");
    incheNum = float(input("input inches number(negative express end):"));
print("end");


# Write a program that asks the user to enter numbers until they enter an empty string to quit.
# Finally, the program prints out the smallest and largest number from the numbers it received.
numStr = input("enter numbers:");
numList = [];
if (numStr == ""):
    print("smallest number is: ", "unknow")
    print("largest number is: ", "unknow")
while (numStr != ""):
    num = float(numStr);
    if (len(numList) == 0):
        numList.append(num);
    else:
        if (num <= numList[len(numList) - 1]):
            numList.insert(len(numList) - 1, num);
        else:
            numList.append(num);
    numStr = input("enter numbers:");
print("smallest number is: ", numList[0]);
print("largest number is: ", numList[len(numList) - 1]);

# Write a game where the computer draws a random integer between 1 and 10.
# The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text: Too high, Too low or Correct.
# Notice that the computer must not change the number between guesses.
import random;

randomNum = random.randint(1, 10);
guessNum = input("please guess:");
while True:
    if (guessNum > randomNum):
        print("Too high")
        guessNum = input("please guess again:");
    elif (guessNum < randomNum):
        print("Too low")
        guessNum = input("please guess again:");
    else:
        print("Correct");
        break;

# Write a program that asks the user for a username and password.
# If either or both are incorrect, the program ask the user to enter the username and password again.
# This continues until the login information is correct or wrong credentials have been entered five times.
# If the information is correct, the program prints out Welcome.
# After five failed attempts the program prints out Access denied.
# The correct username is python and password rules.
username = input("please input username:");
password = input("please input password:");
correntUserName = "python";
correntPassword = "rules";
times = 1;
while (times <= 5 and (username != correntUserName or password != correntPassword)):
    print("enter the username and password again");
    username = input("please input username again:");
    password = input("please input password again:");
    if (username == correntUserName and password == correntPassword):
        print("Welcome");
    elif (times >= 5):
        print("Access denied");
    times += 1;

# Implement an algorithm for calculating an approximation for the value of pi (π).
# Let's assume that A is a unit circle. A unit circle has the radius of one and it is centered at the origin (0,0).
# Smallest possible square B is drawn around the unit circle so that circle A is completely inside the square.
# The corners of the square are now (-1,-1), (1, -1), (1, 1), and (-1, 1).
# If a large number of random points are scattered inside the square,
# the fraction of points that fall inside the circle A correlates with the fraction of the area of circle A compared to the area of square B:
# πr^2/4 = π*1^2/4 = π/4.
# This can be used as a simple method for calculating an approximation of the value of pi:
# Let's generate a large number of random points, such as one million, inside square B.
# Let N be the total number of random points. Each point inside the square is tested for whether it resides inside circle A.
# Let n be the total number of points that fall inside circle A.
# Now we have n/N≈π/4, and from that we get π≈4n/N. Write a program that asks the user how many random points to generate,
# and then calculates the approximate value of pi using the method explained above.
# At the end, the program prints out the approximation of pi to the user.
# (Notice that it is easy to test if a point falls inside circle A by testing if it fulfills the inequation x^2+y^2<1.).

# n (insider A circle)
N = int(input("random point all quantity: "));
# n (insider A circle)
n = 0;
for i in range(N):
    x = random.uniform(1, -1);
    y = random.uniform(1, -1);
    if (x ** 2 + y ** 2 < 1):
        n += 1;
piVal = (4 * n) / N
print(piVal)

