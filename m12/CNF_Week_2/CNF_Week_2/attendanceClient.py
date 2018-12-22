import socket
import threading
s=socket.socket()
ip="10.2.136.27"
port=5900
s.connect((ip,port))
clientRunning = True
while clientRunning:
    inputdata = str(input())
    if inputdata == "quit":
        clientRunning = False
        s.send(("quit").encode())

threading.Thread(target = recieveMessage, args = (s, )).start()
message = input("MARK-ATTENDANCE ")
s.send(message.encode())
def recieveMessage(sock):
    serverDown = False
    while clientRunning and (not serverDown):
        message = sock.recv(1024).decode()
        if message == "ATTENDANCESUCCESS":
            serverDown = True
        elif message.startswith("SECRET-QUESTION"):
            answer = input()
            s.send(answer.encode())
