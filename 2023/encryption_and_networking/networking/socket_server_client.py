import socket

# Echo server program
def host(exchangePort):
    
    hostIP = ''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((hostIP, exchangePort))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data: break
                return(data)

# Echo client program
def client(data, exchangePort):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', exchangePort))
        s.sendall(data)
        data = s.recv(1024)



def send(data, exchangePort):
    client(bytes(str(data), 'utf-8'), exchangePort)

def receive(exchangePort):
    return (host(exchangePort).decode('utf-8'))