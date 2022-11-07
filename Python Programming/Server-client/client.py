import socket

port = 9999
IP = "localhost"

# create a socket instance named client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, port))

# when client.connect() method is called the client instance create a socket that will open any one of the available ports
# to connect to the specified server endpoint!

# maximum byte size for received messages
max_buff = 1024
message = client.recv(max_buff)

# terminate the connection
client.close()

# print the received message to the terminal
# decodes the message via the UTF-8 protocol!
print(message.decode("UTF-8"))
