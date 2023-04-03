#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:string>')
def print_string(string):
    print(string)
    return f'{string}'

@app.route('/count/<int:integer>')
def count(integer):
    count = ''
    for i in range(integer):
        count += f'{i}\n'
    return count

@app.route('/math/<int:num1><operation><int:num2>')
def math(num1,num2,operation):
    if operation == '+':
        return f'{num1 + num2}'
    elif operation == '-':
        return f'{num1 - num2}'
    elif operation == '*':
        return f'{num1 * num2}'
    elif operation == 'div':
        return f'{num1 / num2}'
    elif operation == '%':
        return f'{num1 % num2}'
    else:
        return 'Please use valid operation'

if __name__ == '__main__':
    app.run(port=5555, debug=True)
