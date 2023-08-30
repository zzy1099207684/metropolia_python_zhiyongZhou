import math
import random

# Write a program that asks your name and then greets you by your name: Examples:
# If you enter Viivi as your name, the program will greet you with Hello, Viivi!.
# If you enter Ahmed as your name, the program will greet you with Hello, Ahmed!.
name = input("what's your name?\n");
print(f"hello, {name}\n");

# Write a program that asks the user for the radius of a circle and the prints out the area of the circle.
radius = float(input("input radius of a circle please: \n"));
area = math.pi * radius ** 2;
print(f"the area of the circle is: {round(area, 3)}\n");

# Write a program that asks the user for the length and width of a rectangle.
# The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides.
length = float(input("input length please: "));
width = float(input("input width please: "));
rec_perimeter = 2 * length + 2 * width;
print(f"perimeter is {round(rec_perimeter, 3)}");
rec_area = length * width;
print(f"rec_area is {round(rec_area, 3)}\n");

# Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.
num_one = int(input("input numberOne: "));
num_two = int(input("input numberTwo: "));
num_three = int(input("input numberThree: "));
sum = num_one + num_two + num_three;
product = num_one * num_two * num_three;
average = (num_one + num_two + num_three) / 3;
print(f"sum is {sum}");
print(f"product is {product}");
print(f"average is {round(average, 3)}\n");

# Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti).
# The program converts the input to full kilograms and grams and outputs the result to the user:
# One talent is 20 pounds.
# One pound is 32 lots.
# One lot is 13,3 grams.
talent = float(input("please input talent number: "));
talentToKg = talent * 20 * 32 * 13.3 / 1000;
talentToG = talent * 20 * 32 * 13.3;
print(f"talent to kilograms is {round(talentToKg, 3)}KG, \ntalent to grams is {round(talentToG, 3)}G");

pounds = float(input("please input pounds number: "));
poundsToKg = pounds * 32 * 13.3 / 1000;
poundsToG = pounds * 32 * 13.3;
print(f"pounds to kilograms is {round(poundsToKg, 3)}KG, \npounds to grams is {round(poundsToG, 3)}G");

lots = float(input("please input lots number: "));
lotsToKg = lots * 13.3 / 1000;
lotsToG = lots * 13.3;
print(f"lots to kilograms is {round(lotsToKg, 3)}KG, \nlots to grams is {round(lotsToG, 3)}G\n");

# Write a program that draws two random combinations of numbers for a combination lock:
# a 3-digit code where each number is between 0 and 9.
# a 4-digit code where each number is between 1 and 6.
listZeroToNine = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
listOneToSix = [1, 2, 3, 4, 5, 6];
three_digit_code = random.sample(listZeroToNine, 3);
print(f"a 3-digit code is {three_digit_code}");

four_digit_code = random.sample(listOneToSix, 4);
print(f"a 4-digit code is {four_digit_code}");
