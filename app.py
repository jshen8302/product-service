from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Melon", "price": 0.75, "quantity": 128},
    {"id": 2, "name": "Banana", "price": 0.3, "quantity": 2},
    {"id": 3, "name": "Peach", "price": 1.5, "quantity": 6}
]

# Retreve a list of available grocery products including names, prices, and quantites in stovk
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify({"products": products})

# Endpoint to get details of a product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = next((product for product in products if product["id"] == product_id), None)
    if product:
        return jsonify({"product": product})
    return jsonify({"error": "Product not found"}), 404

# Endpoint to add a new grocery product
@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.get_json()
    new_product['id'] = len(products) + 1  # Assign a new ID
    products.append(new_product)
    return jsonify({"message": "Product added successfully", "product": new_product}), 201

if __name__ == '__main__':
    app.run(debug=True)
