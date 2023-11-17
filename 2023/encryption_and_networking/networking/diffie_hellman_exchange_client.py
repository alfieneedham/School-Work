from send_and_receive import send, receive
from discrete_exponention import power
from random import randrange

range = ((1*(10**50)), (9*(10**59)))
port = 50007

def diffie_hellman_client():
    clientNum = randrange(range[0], range[1])
    prime = randrange(range[0], range[1])

    send(prime)

    print(prime)

diffie_hellman_client()

# python3 diffie_hellman_exchange_.py