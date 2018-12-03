import socket
import sys
import time
from Process import *
from CPU_class import *
from LRU import *

pd = 1
LRU_instance = LRUCache(4)
CPU = CPU(1,0.2)

def create(val):
	P = Process(1,"1",val)
	LRU_instance.insertItem(P)


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Then bind() is used to associate the socket with the server address. In this case, the address is localhost, referring to the current server, and the port number is 10000.

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

#Calling listen() puts the socket into server mode, and accept() waits for an incoming connection.

# Listen for incoming connections
sock.listen(1)


# Wait for a connection
print >>sys.stderr, 'waiting for a connection'
connection, client_address = sock.accept()

#accept() returns an open connection between the server and client, along with the address of the client. The connection is actually a different socket on another port (assigned by the kernel). Data is read from the connection with recv() and transmitted with sendall().

try:
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
		if command == "Create":
			create(parameters[1])


finally:
     # Clean up the connection
	print >>sys.stderr, 'se fue al finally'
	connection.close()

#When communication with a client is finished, the connection needs to be cleaned up using close(). This example uses a try:finally block to ensure that close() is always called, even in the event of an error.


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
