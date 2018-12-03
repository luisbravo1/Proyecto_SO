import socket
import sys
import time
from Process import *
from CPU_class import *
from LRU import *

pd = 1
LRU_instance = LRUCache(4)
CPU = CPU(1,0.2)

def create(pid, val):
	P = Process(pid,"1",val/pageSize)
	LRU_instance.insertItem(P)

def address(pid, desplazamiento):



#from tabulate import tabulate

quantum = 1.0
realMemory = 3
swapMemory = 4
pageSize = 1.0
pageSizeB = pageSize * 1024.0
#timestamp = 0.0
delta = quantum
pid = 0

def initConnection():
	# Create a TCP/IP socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	#Then bind() is used to associate the socket with the server address. In this case, the address is
	#localhost, referring to the current server, and the port number is 10000.

	# Bind the socket to the port
	server_address = ('localhost', 10002)
	print >>sys.stderr, 'starting up on %s port %s' % server_address
	sock.bind(server_address)

	#Calling listen() puts the socket into server mode, and accept() waits for an incoming connection.

	# Listen for incoming connections
	sock.listen(1)


	# Wait for a connection
	print >>sys.stderr, 'waiting for a connection'

	#accept() returns an open connection between the server and client, along with the address of the client.
	#The connection is actually a different socket on another port (assigned by the kernel).
	#Data is read from the connection with recv() and transmitted with sendall().
	return sock.accept()

def incrementTimestamp(time):
	global timestamp
	timestamp += time


try:
	connection, client_address = initConnection()
	print >>sys.stderr, 'connection from', client_address

    # Receive the data
	while True:
		data = connection.recv(256)
		print >>sys.stderr, 'server received "%s"' % data
		if data:
			print >>sys.stderr, 'sending answer back to the client'

			connection.sendall('process created')
		else:
			print >>sys.stderr, 'no data from', client_address
			connection.close()
			sys.exit()


		if (CPU.finished and not LRU_instance.isEmpty()):
			P = LRU_instance.getItem()
			LRU_instance.removeItem(P)
			CPU.add(P)
		else:
			CPU.run()

		command = data
		comment = None
		parameters = []

		if "//" in command:
			commentSplit = data.split("//")
			command = commentSplit[0]
			comment = commentSplit[1]
		if " " in  command:
			parameters = commentSplit[0].split(" ")
			command = parameters[0]

		incrementTimestamp(0.001)

		#Create %s, size in pages
		if command == "Create":
			create(pid+1, parameters[1])
		#Quantum
		if command == "Quantum":
			print("Quantum")
		#Address
		if command == "Address":
			address(parameters[1], parameters[2])
		#Fin
		#End




finally:
     # Clean up the connection
	print >>sys.stderr, 'se fue al finally'


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
