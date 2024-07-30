from bson import ObjectId
from flask import Flask, jsonify, request
from database import collection
from models.produto import Produto


app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/cadastrar", methods = ["POST"])
def cadastroProduto():
    data = request.json
    name = data.get("name")
    price = data.get("price")
    quantity = data.get("quantity")

    produto = Produto(name=name,price=price, quantity=quantity)
    collection.insert_one(produto.to_dict()).inserted_id
    return jsonify({"message": "produto adicionado com sucesso"})

@app.route("/deletar/<string:id>", methods = ["DELETE"])
def apagar(id):
    collection.delete_one({'_id': ObjectId(id)})
    return jsonify({"message": "produto apagado com sucesso"})
    
@app.route('/buscar/<string:id>', methods = ['GET'])
def buscarUm(id):
    produto = collection.find_one({'_id': ObjectId(id)})
    return jsonify({
                "_id": str(produto['_id']),
                "name": produto.get('name'),
                "quantity": produto.get('quantity'),
                "price": produto.get('price')
            })

@app.route('/buscar', methods = ['GET'])
def buscar():
    produtos = collection.find()
    produtos_list = []
    
    for produto in produtos:
        produto['_id'] = str(produto['_id'])
        produtos_list.append(produto)
        
    return jsonify(produtos_list)
    
@app.route('/atualizar/<string:id>', methods = ['POST'])
def atualizar(id):
    produto = collection.find_one({'_id': ObjectId(id)})
    data = request.json
    
    update_fields = {}
    if 'name' in data:
        update_fields['name'] = data['name']
    if 'quantity' in data:
        update_fields['quantity'] = data['quantity']
    if 'price' in data:
        update_fields['price'] = data['price']
    if not update_fields:
        return jsonify({"error": "Nenhum campo para atualizar"}), 400
    
    collection.update_one({'_id': ObjectId(id)}, {'$set': update_fields})
    return jsonify({"message": "Produto atualizado com sucesso"})
    

if __name__ == "__main__":
    app.run(debug=True)

