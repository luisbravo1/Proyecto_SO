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

while True:
    mensaje = raw_input("Mensaje a enviar al servidor: ")
    
    if mensaje == "salir":
        break
    
    sock.sendall(mensaje)

    respuesta = sock.recv(256)
    
    print >>sys.stderr, 'cliente received "%s"' % respuesta


print >>sys.stderr, 'closing socket'
sock.close()

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))