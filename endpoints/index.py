import os, json
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/gimme", methods=['POST'])
def add_something():
    if os.path.isfile('history.json'):
        with open('history.json', 'r') as f:
            hist = json.load(f)
            hist.append(request.get_json())
        with open('history.json', 'w') as f:
            json.dump(hist,f)
    else:
        hist = [{'beginning': 'ofFile'}]
        hist.append(request.get_json())
        with open('history.json', 'w') as f:
            json.dump(hist,f)
    return jsonify(hist), 200