# Write a program that asks a fisher the length of a zander in centimeters.
# If the zander does not fulfill the size limit,
# the program instructs to release the fish back into the lake
# and notifies the user of how many centimeters below the size limit the caught fish was.
# A zander must be 42 centimeters or longer to meet the size limit.
print("please input fish size")
length = float(input("the length of a zander is(cm): "));
if (length < 42):
    print(f"let the fish back into the lake, it below the size limit :{42 - length} cm");

# Write a program that asks the user to enter the cabin class of a cruise ship
# and then prints out a written description according to the list below.
# You must use an if/elif/else structure in your solution.
# LUX: upper-deck cabin with a balcony.
# A: above the car deck, equipped with a window.
# B: windowless cabin above the car deck.
# C: windowless cabin below the car deck.
# If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class.
cabinClass = input("enter the cabin class of a cruise ship: ");
if (cabinClass == 'A'):
    print("above the car deck, equipped with a window");
elif (cabinClass == 'B'):
    print("windowless cabin above the car deck");
elif (cabinClass == 'C'):
    print("windowless cabin below the car deck");
else:
    print("error message: Invalid cabin class");

# Write a program that asks for the biological gender and hemoglobin value (g/l).
# The program the notifies the user if the hemoglobin value is low, normal or high.
# A normal hemoglobin value for adult females is between 117-155 g/l.
# A normal hemoglobin value for adult males is between 134-167 g/l.
gender = input("input your gender: (females/males)");
hemoglobin = float(input("input your hemoglobin value(g/l): "));
if (gender == "females"):
    if (hemoglobin < 117):
        print("he hemoglobin value is low");
    elif (hemoglobin > 155):
        print("he hemoglobin value is high");
    else:
        print("he hemoglobin value is normal");
elif (gender == "males"):
    if (hemoglobin < 134):
        print("he hemoglobin value is low");
    elif (hemoglobin > 167):
        print("he hemoglobin value is high");
    else:
        print("he hemoglobin value is normal");

# Write a program that asks the user to enter a year
# and notifies the user whether the input year is a leap year.
# A year is a leap year if it is divisible by four.
# However, years divisible by 100 are leap years only if they are also divisible by 400.
year = int(input("enter a year: "));
if((year % 4) == 0 and (year % 100) != 0) or (year % 400) == 0:
    print("the year is a leap year ");
else:
    print("the year is not a leap year ");
