from flask import Flask
from flask_pymongo import PyMongo
from datasets.products_data import sample_products

app=Flask(__name__)
app.config['MONGO_URI']='mongodb://localhost:27017/MVC'
mongo=PyMongo(app)

with app.app_context():
    products=mongo.db.products #creates a collection named 'products'
    #Collection is always chosen like mongo.db.<collection_name>.
    products.delete_many({})
    products.insert_many(sample_products)
    print('Data inserted successfully!')