import socket

IP = "localhost"
port = 3345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, port))
MAX_BUFF = 1024
PREP_BUFF = str(input("Specify the size of messages! Must be an integer value!"))

client.send(bytes(PREP_BUFF, "UTF-8"))
client.send(bytes("Hey there! Server!, This is a text message below the size, {} bytes!".format(PREP_BUFF), "UTF-8"))
reply = client.recv(MAX_BUFF)
client.close()
print("Server replied: {}".format(reply.decode("UTF-8")))

