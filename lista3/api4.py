#Crie uma API para gerenciar produtos de um e-commerce, permitindo adicionar, listar, atualizar estoque, deletar produtos e gerenciar um carrinho de compras.
#Obs: Utilize arquivos (txt ou JSON) para simular cada operação de persistência de dados
from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

products_file = 'lista3/products.json'
cart_file = 'lista3/cart.json'

def load_products():
    if os.path.exists(products_file):
        with open(products_file, 'r') as file:
            return json.load(file)
    else:
        return []
    
def load_cart():
    if os.path.exists(cart_file):
        with open(cart_file, 'r') as file:
            return json.load(file)
    else:
        return []
    
def save_products(products):
    with open(products_file, 'w') as file:
        json.dump(products, file, indent=2)
        
def save_cart(cart):
    with open(cart_file, 'w') as file:
        json.dump(cart, file, indent=2)
        
@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()
    products = load_products()
    
    product_id = len(products) + 1
    
    new_product = {
        'id': product_id,
        'name': data['name'],
        'price': data['price'],
        'stock': data['stock']
    }
    
    products.append(new_product)
    save_products(products)
    
    return jsonify(new_product), 201

@app.route('/products', methods=['GET'])
def get_products():
    products = load_products()
    return jsonify(products)


@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    cart = load_cart()
    products = load_products()
    
    product = next((p for p in products if p['id'] == data['product_id']), None)
    
    if product:
        cart.append(product)
        save_cart(cart)
        return jsonify(cart), 201
    else:
        return jsonify({'error': 'Produto não encontrado'}), 404
    
@app.route('/cart', methods=['GET'])
def get_cart():
    cart = load_cart()
    return jsonify(cart)

@app.route('/products/<int:product_id>', methods=['PATCH'])
def update_product(product_id):
    data = request.get_json()
    products = load_products()
    product_index = next((i for i, p in enumerate(products) if p['id'] == product_id), None)
    
    if product_index is not None:
        if 'stock' in data:
            products[product_index]['stock'] = data['stock']
        save_products(products)
        return jsonify(products[product_index])
    else:
        return jsonify({'error': 'Produto não encontrado'}), 404
    
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    products = load_products()
    product_index = next((i for i, p in enumerate(products) if p['id'] == product_id), None)
    
    if product_index is not None:
        deleted_product = products.pop(product_index)
        save_products(products)
        return jsonify(deleted_product)
    else:
        return jsonify({'error': 'Produto não encontrado'}), 404
    
@app.route('/cart/<int:product_id>', methods=['DELETE'])
def remove_from_cart(product_id):
    cart = load_cart()
    product_index = next((i for i, p in enumerate(cart) if p['id'] == product_id), None)
    
    if product_index is not None:
        deleted_product = cart.pop(product_index)
        save_cart(cart)
        return jsonify(deleted_product)
    else:
        return jsonify({'error': 'Produto não encontrado'}), 404
    
    
    
if __name__ == '__main__':
    app.run(debug=True, host='localhost')
    
