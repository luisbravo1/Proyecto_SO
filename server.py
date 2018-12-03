import socket
import sys
import time
from datetime import datetime
from Process import *
from CPU_class import *
from LRU import *
from tabulate import tabulate

pid = 1

LRU_instance = LRUCache(4)
CPU = CPU(1,1)

timestamp = 0
Cola_de_Listos = ""
tmp = 0


def incrementTimestamp(time):
	global timestamp
	timestamp += time


def create(val):
	global pid
	global tmp
	P = Process(pid,str(pid),val)
	if (CPU.get_process() == None):
		CPU.add(P)
		tmp = P.key
	else:
		LRU_instance.insertItem(P)
	#print("<" + str(timestamp) + "> process " + str(pid) + " created size:" + str(val))
	pid = pid + 1
	print_cache(LRU_instance)


def print_cache(cache):
	global Cola_de_Listos
	output = ""
	for i, item in enumerate(cache.item_list):
		output = output + str(item.key) + " "
	Cola_de_Listos = output

#from tabulate import tabulate

quantum = 1.0
quantum_add = 1
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


try:
	connection, client_address = initConnection()
	print >>sys.stderr, 'connection from', client_address

    # Receive the data
	while True:


		data = connection.recv(256)
		#print >>sys.stderr, 'server received "%s"' % data
		if data:
			#print >>sys.stderr, 'sending answer back to the client'

			connection.sendall('process created')
		else:
			print >>sys.stderr, 'no data from', client_address
			connection.close()
			sys.exit()

		incrementTimestamp(0.001)
		#else:
			#CPU.run()

		command = data
		comment = None
		parameters = []
		commentSplit = []

		if "//" in command:
			commentSplit = data.split("//")
			command = commentSplit[0]
			comment = commentSplit[1]
		if " " in  command:
			parameters = commentSplit[0].split(" ")
			command = parameters[0]
		print(" ")

		#Create %s, size in pages
		if command == "Create":
			#connection.sendall("<" + str(timestamp) + "> process " + str(pid) + " created size:" + str(parameters[1]))
			create(parameters[1])
		#Quantum
		if command == "Quantum":
			#connection.sendall("<" + str(timestamp) + "> quantum end")
			P1 = CPU.quantum_end()
			P = LRU_instance.getItem()
			LRU_instance.removeItem(P)
			CPU.add(P)
			if (not P1 == None):
				LRU_instance.insertItem(P1)
				timestamp = quantum * quantum_add
				quantum_add = quantum_add + 1
		if command == "QuantumV":
			quantum = int(parameters[1])
		if command == "Fin":
			P = LRU_instance.findItem(int(parameters[1]))
			if (not P == None):
				LRU_instance.removeItem(P)
			elif (CPU.get_process().key == int(parameters[1])):
				P1 = CPU.quantum_end()
				P = LRU_instance.getItem()
				LRU_instance.removeItem(P)
				CPU.add(P)
			#connection.sendall("<" + str(timestamp) + "> Proceso " + str(parameters[1]) + " terminado")
		#Address
		if command == "Address":
			address(command, parameters[1], parameters[2])
		#Fin
		#End

		if (not CPU.get_process() == None):
			tmp = CPU.get_process().key
		print_cache(LRU_instance)
		print tabulate([['Comando','timestamp','Cola de listos','CPU'],[(command + " " + parameters[1]),timestamp,Cola_de_Listos,tmp]], headers='firstrow',tablefmt='orgtbl')



finally:
     # Clean up the connection
	print >>sys.stderr, 'se fue al finally'


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
