import socket

IP = "localhost"
port = 9900

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, port))
MAX_BUFF = 1024
MAX_CLIENTS = 10
server.listen(MAX_CLIENTS)

while True:
    connection, client_addr = server.accept()
    print("Connected to a client at address {}".format(client_addr))
    message = connection.recv(MAX_BUFF)
    print("Client at address {} said {}".format(client_addr, message.decode("UTF-8")))
    connection.send(bytes(message.decode("UTF-8"), "UTF-8"))
    # or simply connection.send(message) why decode an then encode? 
