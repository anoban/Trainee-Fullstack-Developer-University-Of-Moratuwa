# Python's socket module to build a server socket instance
import socket

# port number must be a 4 digit integer
# this port number must be vacant & not occupied by any application instances in our local machine
port = 9999

# we specify the IP to be local lost since we are communicating between 2 applications running on the same machine!
# one can leave this a blank string i.e IP = ""; which will make the port accessible via all possible IP addresses of the local 
# machine
IP = "localhost"

# creating a socket instance names "server"
# AF_INET specifies a IPv4 type socket
# SOCK_STREAM specifies a TCP type socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# assigns the server instance a IP and port number!
# here the IP is identical to the IP of local machine!
server.bind((IP, port))

# server will que a maximum of max_clients when multiple simultaneous requests are received from different clients
# this server instance will refuse to connect if the incoming requests are higher than the max_clients parameter!
max_clients = 20
server.listen(max_clients)

print("Listening...........")

# an infinite loop
while True:
    connection, client_addr = server.accept()
    # server.connect() method generates a tuple of a connection object & clients end point address!
    # these are unpacked here and captured as variables connection & client_addr
    print("A clinet at address {} is connected".format(client_addr))
    # send a message to the connected client
    # data is communicated as binaries, therefore an apt encoding must be provided to decode the received data at client endpoint!
    # since we are sending a string, we pass the encoding param as UTF-8
    # UTF-8 encoding allows sending any unicode characters to be sent via the connection!
    connection.send(bytes("Hello there client!, this is a Python 3.10.4 srever!", "UTF-8"))
