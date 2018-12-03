import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# Connect the socket to the port where the server is listening
server_address = ('localhost', 10002)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

# After the connection is established, data can be sent through the socket with sendall() and received with recv(), just as in the server.

messages = ['Create 2048 //', 'Create 3072 // ', 'Create 5000 //','QuantumV 2 //','Quantum //','Create 1024 //','Quantum //','Fin 1 //']
try:

      # Send data
    for m in messages:
		print >>sys.stderr, 'client sending "%s"' % m
		sock.sendall(m)

		# Look for the response

		respuesta = sock.recv(256)

		print >>sys.stderr, 'client received "%s"' % respuesta

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))