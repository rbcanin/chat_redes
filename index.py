import socketio

# Cria uma instância do cliente Socket.IO
sio = socketio.Client()

# Define as funções de evento para conexão, desconexão e mensagens
@sio.event
def connect():
    print('Conectado ao servidor')

@sio.event
def disconnect():
    print('Desconectado do servidor')

@sio.on('send_message')
def on_message(data):
    print(f'Nova mensagem: {data}')

# Conecta ao servidor Socket.IO
sio.connect('http://localhost:3030')

# Loop para enviar mensagens do terminal
try:
    while True:
        message = input('Digite uma mensagem: ')
        sio.emit('send_message', message)
except KeyboardInterrupt:
    print('Desconectando...')
    sio.disconnect()
