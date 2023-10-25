import math
import random
# 1.Write a function that returns a random dice roll between 1 and 6.
# The function should not have any parameters. Write a main program that rolls the dice until the result is 6.
# The main program should print out the result of each roll.
def roll():
    return random.randint(1,6);
#main
num = 0;
while(num != 6):
    num = roll();
    print(num);



# 2.Modify the function above so that it gets the number of sides on the dice as a parameter.
# With the modified function you can for example roll a 21-sided role-playing dice.
# The difference to the last exercise is that the dice rolling in the main program continues
# until the program gets the maximum number on the dice, which is asked from the user at the beginning.
def rollNfs(sides):
    return random.randint(1, sides);
#main
num = 0;
sides = 21
while(num != sides):
    num = rollNfs(sides);
    print(num);









# 3.Write a function that gets the quantity of gasoline in American gallons and returns the number converted to litres.
# Write a main program that asks for a volume in gallons from the user and converts the value to liters.
# The conversion must be done by using the function.
# Conversions continue until the user inputs a negative value.
def gallonToLitre(gallon):
    return gallon*3.78541;
#main
gallon = float(input("input a gallons number: "));
print(gallonToLitre(gallon),"litres");




# 4.Write a function that gets a list of integers as a parameter.
# The function returns the sum of all the numbers in the list.
# For testing, write a main program where you create a list, call the function, and print out the value it returned.
def sumNumbers(numbers):
    return sum(numbers);
#main
nums = [1,2,3];
print(sumNumbers(nums));



# 5.Write a function that gets a list of integers as a parameter.
# The function returns a second list that is otherwise the same as the original list except that all uneven numbers have been removed.
# For testing, write a main program where you create a list,
# call the function, and then print out both the original as well as the cut-down list.
def removeUnevenNumber(numbers):
    return [i for i in numbers if i % 2 == 0];
#main
nums = [1,2,3,4,5,6,7,8];
print(removeUnevenNumber(nums));



# 6.Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in euros.
# The function calculates and returns the unit price of the pizza per square meter.
# The main program asks the user to enter the diameter and price of two pizzas
# and tells the user which pizza provides better value for money (which of them has a lower unit price).
# You must use the function you wrote for calculating the unit prices.
def getPizzaUnitPriceArea(diamiter, price):
    return math.sqrt(math.pi*(diamiter/2))/price;
#main
firstDiamiter = float(input("input first pizza diamiter: "));
firstPrice = float(input("input first pizza price: "));
secDiamiter = float(input("input second pizza diamiter: "));
secPrice = float(input("input second pizza price: "));
firstUnitPriceArea = getPizzaUnitPriceArea(firstDiamiter,firstPrice)
secUnitPriceArea = getPizzaUnitPriceArea(secDiamiter,secPrice)
print("choose","first pizza" if firstUnitPriceArea > secUnitPriceArea else "second pizza")

