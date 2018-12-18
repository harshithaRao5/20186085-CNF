import socket
def main():
	host = '127.0.0.1'
	port = 5500
	s = socket.socket()
	s.bind((host,port))
	s.listen(1)
	c, addr = s.accept()
	print("connection from: ",str(addr))
	while True:
		data = c.recv(1024).decode()
		if not data:
			break
		print("from connected user: ",str(data))
		data = str(data).upper()
		print("sending: ",str(data))
		c.send(data.encode())
	c.close()
main()