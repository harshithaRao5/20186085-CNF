import socket
def main():
	host = '127.0.0.1'
	port = 5501
	server = ('127.0.0.1',5500)
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.bind((host,port))
	message = input("->")
	while message!='q':
		s.sendto(message.encode(), server)
		data, addr=s.recvfrom(1024)
		print("Received from server:",str(data.decode()))
		message = input("->")
	s.close()
main()