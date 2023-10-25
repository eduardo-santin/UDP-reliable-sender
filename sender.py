from socket import *
import sys

debug = 1
host_name = 'lagrange.ccom.uprrp.edu'
port_number = 4205

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# check if the connection was successful


if len(sys.argv) <= 1:
	print('Usage: python3 sender.py <filename>')
	sys.exit(0)

# Open the file and read the message content
with open(sys.argv[1], 'r') as file:
    message = file.read()

# print message 
# if debug:
#     print('Message to send:')
#     print(message)
#     print(type(message))
    
#     # send message to server
#     clientSocket.sendto(message.encode(), (host_name, port_number))
#     print('Message sent to server')
#     # see what the server sends back
#     modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
#     print('Message received from server')
#     print(modifiedMessage.decode())
#     # close the socket
#     clientSocket.close()



