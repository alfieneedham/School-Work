from socket_server_client import send, receive
from discrete_exponention import power
from random import randrange

range = ((1*(10**50)), (9*(10**59)))

def diffie_hellman_host():
    exchangePort = 50002

    privateNum = randrange(range[0], range[1])

    modNum = int(receive(50006))
    #exchangePort += 1
    print(modNum)

    shareNum = (2^privateNum)%modNum

    receivedNum = int(receive(50007))
    #exchangePort += 1
    print(receivedNum)

    send(shareNum, 50008)
    #exchangePort += 1
    print(shareNum)



diffie_hellman_host()