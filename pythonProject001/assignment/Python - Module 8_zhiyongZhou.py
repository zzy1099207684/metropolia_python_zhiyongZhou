import mysql.connector
from geopy import distance

# database
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='123456',
    autocommit=True
);
cursor = connection.cursor();


def getSqlResult(sql):
    cursor.execute(sql);
    return cursor.fetchall();


# Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name
# and location (town) from the airport database used on this course.
# The ICAO codes are stored in the ident column of the airport table.
ICAO_code = input("input ICAO code: ");
sql = "select `name`, municipality from airport where ident = '" + ICAO_code + "'";
result = getSqlResult(sql);
if cursor.rowcount > 0:
    for row in result:
        print(f"airport name is {row[0]}, it location is {row[1]}");


# Write a program that asks the user to enter the area code (for example FI)
# and prints out the airports located in that country ordered by airport type.
# For example, Finland has 65 small airports, 15 helicopter airports and so on.
countryCode = input("put country code: ");
sql = "select count(0), a.type from country c left join airport a on a.iso_country = c.iso_country where c.iso_country = '" + countryCode + "' GROUP BY a.type"
cursor.execute(sql);
result = cursor.fetchall();
str = "there are ";
if (cursor.rowcount > 0):
    for row in result:
        str = str + f"{row[0]} {row[1]}, ";
str = str + 'and so on';
print(str);



# Write a program that asks the user to enter the ICAO codes of two airports.
# The program prints out the distance between the two airports in kilometers.
# The calculation is based on the airport coordinates fetched from the database.
# Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/.
# Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE,
# write geopy into the search field and finish the installation.
ICAO_code_first = input("input ICAO code firstly: ") + "'";
ICAO_code_second = input("input ICAO code secondly: ") + "'";
sql = "select latitude_deg, longitude_deg, `name` from airport where ident = '";
sql_first = sql + ICAO_code_first;
sql_second = sql + ICAO_code_second;
firstCountry = '';
secondCountry = '';
# default
newport_ri = (0, 0);
cleveland_oh = (0, 0);
result_first = getSqlResult(sql_first);
# one ident - one data
if (len(result_first) > 0):
    newport_ri = (result_first[0][0], result_first[0][1]);
    firstCountry = result_first[0][2];
result_second = getSqlResult(sql_second);
if (len(result_second) > 0):
    cleveland_oh = (result_second[0][0], result_second[0][1]);
    secondCountry = result_second[0][2];
print(f"{firstCountry} and {secondCountry} of distance is ", distance.distance(newport_ri, cleveland_oh).kilometers, "km");


cursor.close();
connection.close();
