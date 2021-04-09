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
    new_product = request.json()
    return jsonify(new_product)


if __name__ == '__main__':
    app.run(debug=True, port=4000)