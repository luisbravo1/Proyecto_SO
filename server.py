import socket
import sys
import time

#from tabulate import tabulate

quantum = 1.0
realMemory = 3
swapMemory = 4
pageSize = 1
#timestamp = 0.0
delta = quantum

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
		if data == "":
			print >>sys.stderr, 'no data from', client_address
			connection.close()
			sys.exit()
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
			create(parameters[1])
		#Quantum
		if command == "Quantum":
			print("Quantum")
		#Address
		if command == "Address":
			address(command, parameters[1], parameters[2])
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
