import mysql.connector
from geopy import distance

# database
connection = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='metropolia',
    user='root',
    password='123456',
    autocommit=True
);
cursor = connection.cursor();


def getSqlResult(sql):
    cursor.execute(sql);
    return cursor.fetchall();


# Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta.
# ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.
ICAO_code = input("input ICAO code: ");
sql = "select `name`, latitude_deg, longitude_deg from airport where ident = '" + ICAO_code + "'";
result = getSqlResult(sql);
if cursor.rowcount > 0:
    for row in result:
        print(f"airport name is {row[0]}, it location is {row[1]}, {row[2]}");

# Write a program that asks the user for the country code (for example FI) and prints the number of airports in that country by type.
# For Finland, for example, the result must be information about
# that there are 65 small airports, 15 heliports, etc.
countryCode = input("put country code: ");
sql = "select count(0), a.type from country c left join airport a on a.iso_country = c.iso_country where c.iso_country = '" + countryCode + "' GROUP BY a.type"
cursor.execute(sql);
result = cursor.fetchall();
str = "there are ";
if (cursor.rowcount > 0):
    for row in result:
        str = str + f"{row[0]} {row[1]}, ";
str = str + 'etc.';
print(str);

# Write a program that prompts the user for the ICAO codes of two airports.
# The program indicates the distance between the airports in kilometers.
# The calculation is based on the coordinates retrieved from the database.
# Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/.
# Install the library by choosing View / Tool Windows / Python Packages. Enter geopy in the search field and complete the installation.
ICAO_code_first = input("input ICAO code firstly: ") + "'";
ICAO_code_second = input("input ICAO code secondly: ") + "'";
sql = "select latitude_deg, longitude_deg, `name` from airport where ident = '";
sql_first = sql + ICAO_code_first;
sql_second = sql + ICAO_code_second;
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
    secondCountry = result_first[0][2];
print(f"{firstCountry} and {secondCountry} of distance is ", distance.distance(newport_ri, cleveland_oh).kilometers, "km");


cursor.close();
connection.close();
