import socket
def main():
	host = '127.0.0.1'
	port = 5401
	s = socket.socket()
	s.connect((host, port))
	string1=s.recv(1024).decode()
	string2=s.recv(1024).decode()
	guess_num = s.recv(1024).decode()
	print("connecting to server...\n")
	print("connected\n")
	print(str(string1))
	print(str(string2))
	message = input("guess your number: ")
	while message!='q':
		s.send(message.encode())
		data=s.recv(1024).decode()
		print(str(data))
		if guess_num == message:
			break
		message = input("guess your number: ")
	s.close()

main()