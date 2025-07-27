from flask import Flask, request
from flask_cors import CORS
import json
from openai import OpenAI
import os
from dotenv import load_dotenv

app = Flask(__name__)
CORS(app, origins=['http://localhost:*'])
load_dotenv()

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

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

@app.post('/gpt')
def get_response():
    prompt = request.json['prompt']
    model = request.json['model']
    
    response = client.responses.create(
        model={model},
        input={prompt}
    )

    return response;


if __name__ == '__main__':
    app.run(debug=True, port=5001)