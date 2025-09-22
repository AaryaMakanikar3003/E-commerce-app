from flask import Flask
from flask_pymongo import PyMongo
from datasets.customers_data import sample_customers

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/MVC'
mongo = PyMongo(app)

with app.app_context():
    customers = mongo.db.customers  # creates a collection named 'customers'
    customers.delete_many({})       # clear old data
    customers.insert_many(sample_customers)
    print('Customer data inserted successfully!')
