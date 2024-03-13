from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

livros = 'livros.json'

def carrgar_livros():
    if os.path.exists(livros):
        with open (livros, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    else:
        return []

def salvar_livros(livros):
    with open(livros, 'w', encoding='utf-8') as arquivo:
        json.dump(livros, arquivo, indent=2)

@app.route('/')
def index():
    return 'Bem-vindo à API de livros!' 

#consultar todos
@app.route('/livros', methods=['GET'])
def obter_livros():
    livros = carrgar_livros()
    return jsonify(livros)

#consultar id
@app.route('/livros/<int:id>', methods=['GET'])
def obter_livro_id(id):
    livros = carrgar_livros()
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        else:
            return jsonify({'error': 'Livro nao encontrado'}), 404
        
@app.route('/livros/<int:id>', methods=['PUT']) 
def editar_livros(id):
    data = request.get_json()
    livros = carrgar_livros()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(data)
            return jsonify(livros[indice])
    
@app.route('/livros', methods=['POST'])
def adicionar_livro():
    data = request.get_json()
    livros = carrgar_livros()
    
    id = len(livros) + 1
    
    novo_livro = {
        'id': id,
        'titulo': data['titulo'],
        'autor': data['autor'],
        'ano': data['ano']
    }
    
    livros.append(novo_livro)
    salvar_livros(livros)
    
    return jsonify(novo_livro), 201

@app.route('/livros/<int:id>', methods=['DELETE'])
def deletar_livro(id):
    livros = carrgar_livros()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
            salvar_livros(livros)
            return jsonify({'mensagem': 'Livro removido com sucesso!'})
    return jsonify({'error': 'Livro nao encontrado'}), 404
        

app.run(port=5000, host='localhost', debug=True)
