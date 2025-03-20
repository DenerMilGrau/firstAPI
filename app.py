from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/<nome>')
def index2(nome):
    return f'Hello World! Olá {nome}'

@app.route('/soma/<num1>+<num2>')
def soma(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2
        return str(result)
    except ValueError:
        return 'erro'

@app.route('/sub/<num1>-<num2>')
def sub(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 - num2
        return str(result)
    except ValueError:
        return 'erro'

@app.route('/mult/<num1>x<num2>')
def mult(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 * num2
        return str(result)
    except ValueError:
        return 'erro'

@app.route('/div/<num1>/<num2>')
def div(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
        if num1 != 0 and num2 != 0:
            result = num1 / num2
            return str(result)
        else:
            return 'divisao com 0? -.-'
    except ValueError:
        return 'erro'

if __name__ == '__main__':
    app.run(debug=True)