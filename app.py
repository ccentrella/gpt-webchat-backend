from flask import Flask
from flask_cors import CORS
import json

app = Flask(__name__)

CORS(app, origins=['http://localhost:*'])

@app.get('/health')
def index():
    return {
        'message': 'API working correctly'
    }

@app.route('/chats')
def get_chats():
    with open('chats.json', 'r') as file:
        return json.load(file)

@app.route('/conversations')
def get_conversations():
    with open('conversations.json', 'r') as file:
        return json.load(file)

if __name__ == '__main__':
    app.run(debug=True, port=5001)