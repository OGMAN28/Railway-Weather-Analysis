from flask import Flask, jsonify, request
from pymongo import MongoClient
import os

app = Flask(__name__)

# MongoDB Atlas Connection
MONGO_URI = os.getenv('MONGODB_URI')
client = MongoClient(MONGO_URI)
db = client['weather_info'] 

@app.route('/', methods=['GET'])
def home():
    # 
    return jsonify({'message': 'Hello'})

@app.route('/esp32/upload', methods=['POST'])
def esp32_upload():
    # Upload the received data to Mongodb Atlas
    req_data = request.get_json()
    db.info.insert_one(req_data)
    return jsonify({'message': 'Upload Successful'})

if __name__ == '__main__':
    app.run(debug=True)
