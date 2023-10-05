import argparse
import base64
import sys
import json
import socket
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from flask import Flask, request, jsonify
from functions import *

app = Flask(__name__)

@app.route('/search_devices', methods=['POST'])
def search_devices_endpoint():
    try:
        broadcast = request.json['broadcast']
        search_devices(broadcast)
        return jsonify({'message': 'Devices searched successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_param', methods=['POST'])
def get_param_endpoint():
    try:
        device_id = request.json['device_id']
        key = request.json['key']
        client = request.json['client']
        params = request.json.get('params', [])
        get_param(device_id, key, client, params)
        return jsonify({'message': 'Parameters retrieved successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/set_param', methods=['POST'])
def set_param_endpoint():
    try:
        device_id = request.json['device_id']
        key = request.json['key']
        client = request.json['client']
        params = request.json.get('params', "")
        set_param(device_id, key, client, params)
        return jsonify({'message': 'Parameters set successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000)
