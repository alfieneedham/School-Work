import socket

# Echo server program
def host():
    
    hostIP = ''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((hostIP, 50008))
        s.listen(1)
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data: break
                return(data)

if __name__=="__main__":
    pass