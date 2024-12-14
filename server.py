import socket
import threading
import os

HOST = '0.0.0.0'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)
print("SERVER IS UP AND RUNNIN")

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message.startswith('IMAGE:'):
                image_name = message.split(':', 1)[1]
                image_data = client.recv(1024 * 1024)
                for c in clients:
                    if c != client:
                        c.send(f'IMAGE:{image_name}'.encode('utf-8'))
                        c.send(image_data)
            elif message == '/clear':
                broadcast('CLEAR_CHAT'.encode('utf-8'))
            else:
                broadcast(message.encode('utf-8'))
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        client.send('NICKNAME'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        print(f"Nickname of the client is {nickname}")
        broadcast(f'{nickname} joined the chat'.encode('utf-8'))
        client.send('Welcome to the chat'.encode('utf-8'))
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
