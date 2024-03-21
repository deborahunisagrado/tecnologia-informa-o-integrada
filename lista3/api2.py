#Crie uma API para cadastro de usuários, permitindo a inclusão, consulta, atualização e exclusão de usuários.
#Obs: Utilize arquivos (txt ou JSON) para simular cada operação de persistência de dados.
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
users_file = 'lista3/users.json'

def load_users():
    if os.path.exists(users_file):
        with open(users_file, 'r') as file:
            return json.load(file)
    else:
        return []

def save_users(users):
    with open(users_file, 'w') as file:
        json.dump(users, file, indent=2)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    users = load_users()

    # Gera um ID único
    user_id = len(users) + 1

    new_user = {
        'id': user_id,
        'name': data['name'],
        'email': data['email']
    }

    users.append(new_user)
    save_users(users)

    return jsonify(new_user), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = load_users()
    return json.dumps(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    users = load_users()
    user = next((u for u in users if u['id'] == user_id), None)

    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'Usuário não encontrado'}), 404

@app.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    data = request.get_json()
    users = load_users()
    user_index = next((i for i, u in enumerate(users) if u['id'] == user_id), None)

    if user_index is not None:
        if 'name' in data:
            users[user_index]['name'] = data['name'] 
        if 'email' in data:
            users[user_index]['email'] = data['email']
        save_users(users)
        return jsonify(users[user_index])
    else:
        return jsonify({'error': 'Usuário não encontrado'}), 404

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    users = load_users()
    user_index = next((i for i, u in enumerate(users) if u['id'] == user_id), None)

    if user_index is not None:
        deleted_user = users.pop(user_index)
        save_users(users)
        return jsonify(deleted_user)
    else:
        return jsonify({'error': 'Usuário não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True, host="localhost")
