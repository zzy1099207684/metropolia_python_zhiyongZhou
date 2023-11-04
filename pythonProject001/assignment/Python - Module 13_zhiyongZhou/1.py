import flask

# Implement a Flask backend service that tells whether a number received as a parameter is a prime number or not.
# Use the prior prime number exercise as a starting point.
# For example, a GET request for number 31 is given as: http://127.0.0.1:5000/prime_number/31.
# The response must be in the format of {"Number":31, "isPrime":true}.
app = flask.Flask(__name__);

@app.route("/prime_number/<num>")
def isprime(num):
    num = int(num);
    show = {};
    show["Number"] = num;
    if (num <= 1):
        return "invalid enter, please start from 2";
    else:
        result = True;
        for i in range(num - 1, 1, -1):
            if (num % i == 0):
                result = False;
                break;
        show["isPrime"] = result;
        return show;

if __name__ == '__main__':
    app.run('0.0.0.0',port=80)



