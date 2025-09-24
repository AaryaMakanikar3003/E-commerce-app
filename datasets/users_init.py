from flask import Flask
from flask_pymongo import PyMongo
from datasets.users_data import sample_users

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/MVC'
mongo = PyMongo(app)

with app.app_context():
    users = mongo.db.users  # creates a 'users' collection
    users.delete_many({})   # clear existing data
    users.insert_many(sample_users)
    print("Users inserted successfully!")
