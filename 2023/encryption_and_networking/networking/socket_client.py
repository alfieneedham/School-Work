import socket

# Echo client program
def client(data):

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('127.0.0.1', 50008))
        s.sendall(data)
        data = s.recv(1024)

if __name__=="__main__":
    pass