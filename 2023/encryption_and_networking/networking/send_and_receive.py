from socket_client import client
from socket_server import host

def send(data):
    client(bytes(str(data), 'utf-8'))

def receive():
    return (host().decode('utf-8'))