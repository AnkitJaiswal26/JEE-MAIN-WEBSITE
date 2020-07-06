from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from ilp.models import *

client = MongoClient("mongodb+srv://AnkitJaiswal:Ankit@mocktest.o67jp.mongodb.net/<dbname>?retryWrites=true&w=majority")

mock_test = client.get_database("MockTest")
user_collection = mock_test.get_collection("users")

def save_user(username, email, password):
    user_collection.insert_one({ '_id' : username, 'email' : email, 'password' : password })

def get_user(username):
    user_data = user_collection.find_one({ '_id' : username })
    return user_data
    ##return User(user_data['_id'] , user_data['email'], user_data['password']) if user_data else None

def get_User(username):
    user_data = user_collection.find_one({ '_id' : username })
    return User(user_data['_id'] , user_data['email'], user_data['password']) if user_data else None
    