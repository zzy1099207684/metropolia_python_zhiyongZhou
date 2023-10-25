# Write a program that asks the user for a number of a month and then prints out the corresponding season
# (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program.
# We can define each season to last three months, December being the first month of winter.
winter = [12,1,2];
spring = [3,4,5];
summer = [6,7,8];
autumn = [9,10,11];
month = int(input("input month number: "));
if(month in winter): print("winter");
elif(month in spring): print("spring");
elif(month in summer): print("summer");
elif(month in autumn): print("autumn");
else:print("invalid");




# Write a program that asks the user to enter names until he/she enters an empty string.
# After each name is read the program either prints out New name or Existing name depending on whether the name was entered
# for the first time. Finally, the program lists out the input names one by one, one below another in any order.
# Use the set data structure to store the names.
name = input("input name: ");
sets = set();
while(len(name) > 0):
    name = input("input name: ");
    if (name in sets):
        print("Existing name");
    else:
        print("New name");
        sets.add(name);

for i in sets:
    print(i);



# Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport,
# fetch the information of an existing airport or quit. If the user chooses to enter a new airport,
# the program asks the user to enter the ICAO code and name of the airport.
# If the user chooses to fetch airport information instead,
# the program asks for the ICAO code of the airport and prints out the corresponding name.
# If the user chooses to quit, the program execution ends.
# The user can choose a new option as many times they want until they choose to quit.
# (The ICAO code is an identifier that is unique to each airport. For example,
# the ICAO code of Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.)
choose = input("1. fetch the information of airport;\n"
                   "2. new airport;\n"
                   "3. quit \n");
airports = {};
while(choose != '3' and len(choose.strip()) > 0):
    if(choose == '2'):
        ICAD = input("input ICAD: ");
        name = input("input airport name: ");
        airports[ICAD] = name;

    elif(choose == '1'):
        ICAD = input("input ICAD: ");
        print(airports.get(ICAD));
    choose = input("1. fetch the information of airport;\n"
                   "2. new airport;\n"
                   "3. quit \n");
print('end');