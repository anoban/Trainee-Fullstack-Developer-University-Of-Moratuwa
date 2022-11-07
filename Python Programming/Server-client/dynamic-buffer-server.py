import socket

# handling arbitrary sized messages from clients
# here the client is expected to inform the size of upcoming messages in advance to define buffer sizes

IP = "localhost"
port = 3345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, port))

STATIC_BUFF = 1024
MAX_CLIENTS = 5
server.listen(MAX_CLIENTS)
print("Python 3.10.4 server is listening................")

while True:
    connection, client_addr = server.accept()
    print("Server has just accepted a request from a client at address {}.{}".format(client_addr[0], client_addr[1]))
    # first message from client specifying the size of subsequent message to be expected
    client_pretext = connection.recv(STATIC_BUFF).decode("UTF-8")
    print("Client has specified that subsequent incoming messages must be expected with a buffer size {} bytes.".format(client_pretext))
    DYNAMIC_BUFF = int(client_pretext)    
    # receiving client messages with client specified buffer size    
    message = connection.recv(DYNAMIC_BUFF)
    print("Client at {}.{} said: {}".format(client_addr[0], client_addr[1], message.decode("UTF-8")))
    connection.send(bytes("Oh okay, got it. :)", "UTF-8"))

