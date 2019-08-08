import subprocess
import os
import socket
from _thread import start_new_thread
import threading

def threaded(c, addr):
	while True:
		data = c.recv(1024)

		output=subprocess.Popen(['arp', addr],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
		stdout,stderr = output.communicate()
		prt = str(stdout)
		print(prt)

		if not data:
			print('Bye')

			break

		data = data[::-1]

		c.send(prt.encode('ascii'))
	c.close()


def Main():
	host = ""

	port = 12335
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((host, port))
	print("socket binded to post", port)

	s.listen(5)
	print("socket is listening")

	while True:

		c, addr = s.accept()

		print('Connected to :', addr[0], ':', addr[1])

		start_new_thread(threaded, (c,addr[0]),)
	s.close()


if __name__ == '__main__':
	Main()
