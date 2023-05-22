#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:string_to_print>')
def print_string(string_to_print):
    print(string_to_print)
    return string_to_print

@app.route('/count/<int:my_number>')
def count(my_number):
    mystr = ''
    for i in range(my_number):
        mystr.append(f'{i}\n')
    return mystr


@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    return num1, operation, num2

if __name__ == '__main__':
    app.run(port=5555, debug=True)
