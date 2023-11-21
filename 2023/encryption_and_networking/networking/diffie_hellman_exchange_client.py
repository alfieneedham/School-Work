from socket_server_client import send, receive
from discrete_exponention import power
from random import randrange

range = ((1*(10**50)), (9*(10**59)))

def diffie_hellman_client():
    exchangePort = 50002

    privateNum = randrange(range[0], range[1])
    modNum = randrange(range[0], range[1])

    if modNum % 2 == 0:
        modNum += 1

    send(modNum, 50006)
    #exchangePort += 1
    print(modNum)

    shareNum = (2^privateNum)%modNum

    send(shareNum, 50007)
    #exchangePort += 1
    print(shareNum)

    receivedNum = int(receive(50008))
    #exchangePort += 1
    print(receivedNum)
    


diffie_hellman_client()

# python3 diffie_hellman_exchange_.py