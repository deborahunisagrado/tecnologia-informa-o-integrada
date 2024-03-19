#Crie uma API para gerenciar uma lista de tarefas, permitindo adicionar, listar, marcar como concluída e excluir tarefas.
#Obs: Utilize arquivos (txt ou JSON) para simular cada operação de persistência de dados.
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)
tasks_file = 'lista3/tasks.json'

def load_tasks():
    if os.path.exists(tasks_file):
        with open(tasks_file, 'r') as file:
            return json.load(file)
    else:
        return []
    

def save_tasks(tasks):
    with open(tasks_file, 'w') as file:
        json.dump(tasks, file, indent=2)
        
        
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    tasks = load_tasks()
    
    task_id = len(tasks) + 1
    
    new_task = {
        'id': task_id,
        'description': data['description'],
        'done': False
    }
    
    tasks.append(new_task)
    save_tasks(tasks)
    
    return jsonify(new_task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['PATCH'])
def update_task(task_id):
    data = request.get_json()
    tasks = load_tasks()
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if task:
        task['done'] = data['done']
        save_tasks(tasks)
        return jsonify(task)
    else:
        return jsonify({'error': 'Tarefa não encontrada'}), 404
    
    
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    task = next((t for t in tasks if t['id'] == task_id), None)
    
    if task:
        tasks.remove(task)
        save_tasks(tasks)
        return jsonify({'message': 'Tarefa removida com sucesso'})
    else:
        return jsonify({'error': 'Tarefa não encontrada'}), 404
    
if __name__ == '__main__':
    app.run(debug=True, host='localhost')