#Crie uma API que aceite dois números e realize operações básicas de uma calculadora (adição, subtração, multiplicação e divisão).
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
arquivo_usuarios = 'usuarios.json'

def load_usuarios():
    if os.path.exists(arquivo_usuarios):
        with open(arquivo_usuarios, 'r') as file:
            return json.load(file)
    else:
        return []

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
        if num2 == 0:
            result = 'Erro: divisão por zero'
    return jsonify({'result': result})

#Crie uma API para cadastro de usuários, permitindo a inclusão, consulta, atualização e exclusão de usuários.
#Obs: Utilize arquivos (txt ou JSON) para simular cada operação de persistência de dados.
@app.route('/usuarios', methods=['GET'])
def get_usuarios():
    users = load_usuarios()
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)