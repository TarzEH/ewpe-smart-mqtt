import argparse
import base64
import sys
import json
import socket
import io  # Import io module
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from flask import Flask, request, jsonify
from functions import *

app = Flask(__name__)

@app.route('/search_devices', methods=['POST'])
def search_devices_endpoint():
    try:
        broadcast = request.json['broadcast']
        # Capture the output of the function
        output = capture_output(search_devices, broadcast)
        # Print the captured output
        print(output)
        return jsonify({'message': 'Devices searched successfully', 'response': output}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/get_param', methods=['POST'])
def get_param_endpoint():
    try:
        device_id = request.json['device_id']
        key = request.json['key']
        client = request.json['client']
        params = request.json.get('params', [])
        # Capture the output of the function
        output = capture_output(get_param, device_id, key, client, params)
        # Print the captured output
        print(output)
        return jsonify({'message': 'Parameters retrieved successfully', 'response': output}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/set_param', methods=['POST'])
def set_param_endpoint():
    try:
        device_id = request.json['device_id']
        key = request.json['key']
        client = request.json['client']
        params = request.json.get('params', "")
        # Capture the output of the function
        output = capture_output(set_param, device_id, key, client, params)
        # Print the captured output
        print(output)
        return jsonify({'message': 'Parameters set successfully', 'response': output}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def capture_output(func, *args, **kwargs):
    # Capture printed output to a StringIO object
    captured_output = io.StringIO()
    sys.stdout = captured_output

    try:
        result = func(*args, **kwargs)
        # Get the captured output
        output = captured_output.getvalue()
        return output
    finally:
        # Reset sys.stdout to its original value
        sys.stdout = sys.__stdout__

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000)
