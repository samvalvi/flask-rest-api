from flask import Flask, jsonify
from product import products

app = Flask(__name__)

@app.route('/products', methods=['GET'])
def getproducts():
    return jsonify({"products list": product})


@app.route('/products/<string:product_name>', methods=['GET'])
def getproduct(product_name):
    productFound = [i for i in products if i['name'] == product_name]
    if len(productFound) > 0:
        return jsonify({"product": productFound})
    return jsonify({"message": "product not found"})


if __name__ == '__main__':
    app.run(debug=True, port=5000)