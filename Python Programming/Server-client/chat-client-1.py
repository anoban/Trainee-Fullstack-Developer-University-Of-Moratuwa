import socket

IP = "localhost"
port = 3422
MAX_BUFF = 2048

cclient1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cclient1.connect((IP, port))

print("This is a terminal based minimal chat application built using Python 3.10.4, leveraging the TCP/IP protocol!")
print("Enter your message here!>")
print("Type X and enter to exit!")

while True:
    message = str(input())
    if message != "X":
        cclient1.send(bytes(message, "UTF-8"))
        reply = cclient1.recv(MAX_BUFF).decode("UTF-8")
        print(reply)
    elif message == "X":
        cclient1.close()
        print("Connection terminated!")
        print("Exiting application...................")
        break