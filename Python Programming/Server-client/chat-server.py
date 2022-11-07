# partly functional
# needs improvements

# a relay server that receives messages from one client and passes them to another client
# in both directions, functions like a chat application

import socket

IP = "localhost"
port = 3422
MAX_BUFF = 2048
MAX_CLIENTS = 3

chatServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
chatServer.bind((IP, port))
chatServer.listen(MAX_CLIENTS)
print("Python 3.10.4 server is listening....................")

while True:
    first_client = chatServer.accept()
    fc_connection, fc_addr = first_client
    print("A client at address {}:{} has just connected to the server!".format(fc_addr[0], fc_addr[1]))
    fc_text = fc_connection.recv(MAX_BUFF)

    second_client = chatServer.accept()
    sc_connection, sc_addr = second_client
    print("A client at address {}:{} has just connected to the server!".format(sc_addr[0], sc_addr[1]))
    sc_text = sc_connection.recv(MAX_BUFF)

    # relay messages
    fc_connection.send(sc_text)
    sc_connection.send(fc_text)



