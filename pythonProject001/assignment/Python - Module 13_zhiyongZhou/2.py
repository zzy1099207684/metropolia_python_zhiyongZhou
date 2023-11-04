import mysql.connector
import flask

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


# Implement a backend service that gets the ICAO code of an airport and then returns the name and location of the airport in JSON format.
# The information is fetched from the airport database used on this course.
# For example, the GET request for EFHK would be: http://127.0.0.1:5000/airport/EFHK.
# The response must be in the format of: {"ICAO":"EFHK", "Name":"Helsinki-Vantaa Airport", "Location":"Helsinki"}.
app = flask.Flask(__name__);

@app.route("/airport/<ICAO_code>")
def isprime(ICAO_code):
    show = {};
    sql = f"SELECT ident as ICAO,`name`,municipality  FROM airport where ident = '{ICAO_code}'";
    result_first = getSqlResult(sql);
    show["ICAO"] = result_first[0][0];
    show["Name"] = result_first[0][1]
    show["Location"] = result_first[0][2]
    return show;

if __name__ == '__main__':
    app.run('0.0.0.0')