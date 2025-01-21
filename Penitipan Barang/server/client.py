from flask import Flask, jsonify, request
from server.server import StorageDatabase

app = Flask(__name__)
db = StorageDatabase()

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({"stored_items": db.get_all_items()})

@app.route('/taken-items', methods=['GET'])
def get_taken_items():
    return jsonify({"taken_items": db.get_taken_items()})

@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.json
    db.add_item(new_item)
    return jsonify({"message": "Barang berhasil dititipkan!", "item": new_item}), 201

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    updated_data = request.json
    updated_item = db.update_item(item_id, updated_data)
    if updated_item:
        return jsonify({"message": "Barang berhasil diperbarui!", "item": updated_item})
    return jsonify({"message": "Barang tidak ditemukan!"}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    db.delete_item(item_id)
    return jsonify({"message": "Barang berhasil dihapus!"})

@app.route('/items/take/<int:item_id>', methods=['POST'])
def take_item(item_id):
    item = db.take_item(item_id)
    if item:
        return jsonify({"message": "Barang berhasil diambil!", "item": item})
    return jsonify({"message": "Barang tidak ditemukan!"}), 404

if __name__ == '__main__':
    app.run(debug=True)
