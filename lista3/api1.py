#Crie uma API que aceite dois números e realize operações básicas de uma calculadora (adição, subtração, multiplicação e divisão).
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bem-vindo à API da lista 3!'


@app.route('/calc', methods=['GET'])
def calc():
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    op = request.args.get('op')

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)