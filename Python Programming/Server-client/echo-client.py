import socket

IP = "localhost"
port = 9900

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, port))

MAX_BUFF = 1024
message = "Hello there!"

client.send(bytes(message, "UTF-8"))
reply = client.recv(MAX_BUFF)
client.close()
print("Server replied {}".format(reply.decode("UTF-8")))