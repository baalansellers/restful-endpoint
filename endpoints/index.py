import os, json
from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/echo", methods=['POST'])
def post_echo():
    return jsonify(request.get_json()), 200

@app.route("/queue", methods=['POST'])
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

@app.route("/queue", methods=['GET'])
def get_queue():
    if os.path.isfile('history.json'):
        with open('history.json', 'r') as f:
            return jsonify(json.load(f)), 200
    else:
        return jsonify(""), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=443, ssl_context=('/etc/letsencrypt/live/thesellers.house/fullchain.pem', '/etc/letsencrypt/live/thesellers.house/privkey.pem'))
