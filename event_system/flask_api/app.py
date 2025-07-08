from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests for frontend fetch()

SUMMARY_FILE = os.path.join(os.path.dirname(__file__), 'summary.json')

@app.route('/summary', methods=['POST'])
def receive_summary():
    data = request.json
    with open(SUMMARY_FILE, 'w') as f:
        json.dump(data, f)
    return {'status': 'Summary saved'}, 200

@app.route('/summary', methods=['GET'])
def get_summary():
    if not os.path.exists(SUMMARY_FILE):
        return jsonify({'status': 'No summary yet'}), 404
    with open(SUMMARY_FILE, 'r') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    # Bind to 0.0.0.0 and use port 10000 for Render
    app.run(host='0.0.0.0', port=10000)
