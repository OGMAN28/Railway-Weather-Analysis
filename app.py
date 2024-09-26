from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB Atlas connection string
# mongo_uri = os.getenv('MONGODB_URI', 'your_connection_string_here')  # replace with your connection string
# client = MongoClient(mongo_uri)
# db = client['your_database_name']  # replace with your database name

@app.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Hello'})


if __name__ == '__main__':
    app.run(debug=True)
