from flask import Flask, jsonify, request
from products import products

app = Flask(__name__)

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong"})

@app.route('/products' , methods=['GET'])
def getProducts():
    return jsonify({"product": products, "message": "Lista de productos"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
    
    productsFound = [product for product in products if product['name'] == product_name]
    if (len(productsFound)) > 0 :
        return jsonify({"Product": productsFound[0]})
    return jsonify({"Message": "Product not found"})

@app.route('/products', methods=['POST'])
def addproduct():
    new_product = {
        "name": request.json['name'],
        "prince": request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(new_product)
    return jsonify({"Message": "Product added successfully", "product": products}) 
@app.route('/products/<string:product_name>', methods=['PUT'])
def editProduct(product_name):
    productFound = [product for product in products if product['name'] == product_name]
    if (len(productFound)) > 0:

        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({
            "message": "product updated successfully",
            "product": productFound[0]
        })

    return jsonify({"message": "Product not found"})

@app.route('/products/<string:product_name>', methods=['DELETE'])
def deleteProduct(product_name):
    productsFound = [product for product in products if product['name'] == product_name]
    if len(productsFound) > 0:
        products.remove(productsFound[0])
        return jsonify({
            "message": "Product deleted successfully",
            "products" : products
        })
    return jsonify({"message": "Product not found"})
if __name__ == '__main__':
    app.run(debug=True)