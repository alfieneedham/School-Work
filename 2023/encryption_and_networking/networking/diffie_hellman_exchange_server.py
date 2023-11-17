from send_and_receive import send, receive
from discrete_exponention import power
from random import randrange

range = ((1*(10**50)), (9*(10**59)))
port = 50007

def diffie_hellman_host():
    serverNum = randrange(range[0], range[1])

    prime = receive()

    print(prime)

diffie_hellman_host()