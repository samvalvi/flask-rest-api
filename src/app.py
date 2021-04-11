from flask import Flask, jsonify, request
from product import products

app = Flask(__name__)

@app.route('/product', methods=['GET'])
def getproducts():
    return jsonify({"products list": products})


@app.route('/product/<string:product_name>', methods=['GET'])
def getproduct(product_name):
    productFound = [i for i in products if i['name'] == product_name]
    if len(productFound) > 0:
        return jsonify({"product": productFound})
    return jsonify({"message": "product not found"})


@app.route('/product', methods=['POST'])
def addproduct():
    new_product = {
        "name":request.json['name'], 
        "quantity":request.json['quantity'], 
        "price":request.json['price'],
    }
    products.append(new_product)
    return jsonify({"message": "New product added", "products": products})


@app.route('/product/<string:product_name>', methods=['PUT'])
def  updateproduct(product_name):
    update_product = [i for i in products if i['name'] == product_name]
    if len(update_product) > 0:
        update_product[0]['name'] = request.json['name'],
        update_product[0]['quantity'] = request.json['quantity'],
        update_product[0]['price'] = request.json['price']
        return jsonify({"message":"product updated", "products":products})
    return jsonify({"message": "product not found"})
    
    
@app.route('/product/<string:product_name>', methods=['DELETE'])
def deleteproduct(product_name):
    delete_product = [i for i in products if i['name'] == product_name]
    if len(delete_product) > 0:
        products.remove(delete_product[0])
        return jsonify({"message": "product deleted", "products":products})
    return jsonify({"message": "product not found"})   
    
    
if __name__ == '__main__':
    app.run(host="localhost", port=3000, debug=True)