# orders_init.py
from flask import Flask
from flask_pymongo import PyMongo
from datasets.orders_data import sample_orders  # make sure this path is correct

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/MVC'
mongo = PyMongo(app)

with app.app_context():
    orders = mongo.db.orders  # creates a collection named 'orders'
    orders.delete_many({})
    orders.insert_many(sample_orders)
    print('Orders data inserted successfully!')
