import random

# 1.Write a program that asks the user how many dice to roll.
# The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.
dicts = int(input("how many dict: "))
sumResult = 0;
for i in range(dicts):
    randomNum = random.randint(1, 6);
    sumResult = sumResult + randomNum;
print(sumResult);




# 2.Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.
list = [];
num = input("input number: ");
while(len(num.replace(" ","")) > 0):
    list.append(num);
    num = input("input number");
list.sort();
list.reverse();
if(len(list) > 0):
    print(list[:5]);
else:
    print("NULL")


# 3.Write a program that asks the user for an integer and tells if the number is a prime number.
# Prime numbers are number that are only divisible by one or the number itself.
# For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
# On the other hand, 21 is not a prime number as it is divisible by 3 and 7.
num = int(input("input integer: "));
if(num <= 1):
    print(f"{num} is not a prime number");
else:
    result = True;
    intNum = int(num)
    for i in range(intNum-1, 1, -1):
        # print(intNum,"  ",i)
        if(intNum % i == 0):
            result = False;
            break;
    if (result):
        print(f"{intNum} is a prime number");
    else:
        print(f"{intNum} is not a prime number");

# 4.Write a program that asks the user to enter the names of five cities one by on
# (use a for loop for reading the names) and stores them into a list structure.
# Finally, the program prints out the names of the cities one by one, one city per line,
# in the same order they were read as input. Use a for loop for asking the names and a for/in loop to iterate through the list.
cities = [];
for i in range(0,5,1):
    city = input(f"input city name of NO.{i}: ");
    cities.append(city);
for index, city in enumerate(cities):
    print(f"city name of NO.{index} is {city}")