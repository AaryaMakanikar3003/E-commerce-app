from flask import Flask
from flask_pymongo import PyMongo
from controllers.products import products_bp
from controllers.customers import customers_bp
from controllers.orders import orders_bp
from controllers.auth import auth_bp
import os

app=Flask(__name__)
app.secret_key=os.urandom(24)

app.config["MONGO_URI"] = "mongodb://localhost:27017/MVC"
mongo = PyMongo(app)
app.mongo = mongo   # so controllers can use current_app.mongo

app.register_blueprint(products_bp)
app.register_blueprint(customers_bp)
app.register_blueprint(orders_bp)
app.register_blueprint(auth_bp)

# app.add_url_rule('/products', view_func=products, methods=['GET'])

if __name__=='__main__':
    app.run(debug=True)