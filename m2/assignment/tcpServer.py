import socket
import random
def main():
	host = '127.0.0.1'
	port = 5401
	s=socket.socket()
	s.bind((host,port))
	s.listen(1)
	c,addr=s.accept()
	print("connection received from: "+str(addr))
	string1="welcome to guess my number"
	string2="think of a number between 1 and 100"
	c.send(string1.encode())
	c.send(string2.encode())
	guess_num = random.randint(1,101)
	c.send(str(guess_num).encode())
	count = 0
	while True:
		data = c.recv(1024).decode()
		print("Guess: ",str(data))
		if int(data)>guess_num:
			count += 1
			string = "your number is greater than the guess number"
			c.send(string.encode())
		elif int(data)<guess_num:
			count += 1
			string = "your number is lesser than the guess number"
			c.send(string.encode())
		elif int(data) == guess_num:
			count += 1
			c.send("correct, the number of guesses are: ",count)
	c.close()
main()