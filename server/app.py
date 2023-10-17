#!/usr/bin/env python3

from flask import Flask

app = Flask(__name)

# Index view
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string view
@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # Print the string to the console
    return f'<p>{param}</p>'  # Display the string in the web browser

# Count view
@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(i) for i in range(1, param + 1))
    return f'<pre>{numbers}</pre>'

# Math view
@app.route('/math/<float:num1><operation><float:num2>')
def math(num1, operation, num2):
    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return "Division by zero is not allowed."
        result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            return "Modulo by zero is not allowed."
        result = num1 % num2
    else:
        return "Invalid operation."

    return f'Result: {num1} {operation} {num2} = {result}'

if __name__ == '__main__':
    app.run(port=5555)

