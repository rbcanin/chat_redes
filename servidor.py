from flask import Flask, request, jsonify
from flask_socketio import SocketIO, send, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

messages = []

@app.route('/', methods=['GET'])
def index():
    return 'Server is running', 200

@socketio.on('connect')
def handle_connect():
    print('---------------------------------------------')
    print('a user connected: ' + request.sid)
    for message in messages:
        emit('send_message', message)
    print('---------------------------------------------')

@socketio.on('disconnect')
def handle_disconnect():
    print('user disconnected: ' + request.sid)
    print('---------------------------------------------')

@socketio.on('send_message')
def handle_send_message(msg):
    messages.append(msg)
    emit('send_message', msg, broadcast=True)

if __name__ == '__main__':
    port = 3030 # Default port, you can change it as needed
    socketio.run(app, host="0.0.0.0", port=port)
    print(f'Server is running: {port}')