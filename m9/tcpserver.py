import socket
import threading
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = "127.0.0.1"
port = 6000
serverRunning = True
clients = {}
s.bind((ip, port))
s.listen()
number = -1

def generateRandom(uname, client):
    clientConnected = True
    keys = clients.keys()
    print("Server Guessed Number: ", number)

    while clientConnected:
        message = client.recv(1024).decode()
        if "-" in message:
            guessedNum = message.split("-")[1]
        else:
            guessedNum = "-1"
        if guessedNum == "quit":
            clientConnected = False
            clients.pop(uname)
            client.send("Your connection is closed.".encode())
            print(uname + " connection closed.")
        elif guessedNum == "list":
            names_list = ""
            for each_client in keys:
                names_list = names_list + "\n" + each_client
            client.send(("\nList of connected clients: \n" + names_list + "\n").encode())
        else:
            guessedNum = int(guessedNum)
            print(uname + " guessed " + str(guessedNum))
            if(guessedNum < number):
                client.send("Guessed Number is less.".encode())
            elif(guessedNum > number):
                client.send("Guessed Number is greater.".encode())
            else:
                for each_client in keys:
                    if uname == each_client:
                        client.send("Guessed Number is Correct.".encode())
                        client.send("You are the winner.".encode())
                        # client.send("quit".encode())
                    else:
                        clients[each_client].send((uname + " won the match.").encode())
                        # clients[each_client].send(("quit").encode())

print("Server is running, waiting for connections.")
while serverRunning:
    client, address = s.accept()
    uname = client.recv(1024).decode()
    client.send(("Connected.. to " + ip).encode())
    if "-" in uname:
        print("Connected to user: ", uname.split("-")[0])
    else:
        print("Connected to user: ", uname)
    if number == -1:
        print("Game Starting.")
        number = random.randint(1,50)
    if(client not in clients):
        clients[uname] = client
        threading.Thread(target = generateRandom, args = (uname, client, )).start()
