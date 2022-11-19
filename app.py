import os
from flask import Flask, render_template, request
from calculator import Calculator

app = Flask(__name__)


@app.route("/")
def create_calc():
    return render_template('webcalc.html')


@app.route('/', methods=['POST'])
def calculate():
    c = Calculator()
    v1 = request.form.get("v1", type=int)
    v2 = request.form.get("v2", type=int)
    operation = request.form.get("operation")
    if (operation == 'Add'):
        result = c.addition(v1, v2)
    elif (operation == 'Subtract'):
        result = c.subtraction(v1, v2)
    elif (operation == 'Multiply'):
        result = c.multiplication(v1, v2)
    elif (operation == 'Divide'):
        result = c.division(v1, v2)
    elif (operation == 'Modulo'):
        result = c.modulo(v1, v2)
    elif (operation == 'Power'):
        result = c.power(v1, v2)
    else:
        result = 0
    return render_template('webcalc.html', computation=result)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)))
