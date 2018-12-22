import socket
import threading

clientRunning = True
host = '127.0.0.1'  # The server's hostname or IP address
port = 6000        # The port used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
uname = input("User Name: ")
s.send(uname.encode())

def recieveMessage(sock):
    serverDown = False
    while clientRunning and (not serverDown):
        message = sock.recv(1024).decode()
        if message == "quit":
            serverDown = True
        print(message)
        print("Guess the number: ")

threading.Thread(target = recieveMessage, args = (s, )).start()

while clientRunning:
    inputdata = str(input())
    if inputdata == "quit":
        clientRunning = False
        s.send((uname + "-" + "quit").encode())
    else:
        s.send((uname + "-" + inputdata).encode())

