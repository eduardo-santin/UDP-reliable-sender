# import reliablePacket
from sys import argv
from socket import *
from struct import pack


# adress and port number assigned by professor
addr = ('lagrange.ccom.uprrp.edu', 4206)

debug = 0

def gen_checksum(seq, plen, bdata):

	checksum = int(seq) + int(plen) + sum(bdata)
	return checksum

def pack_header(seq, checksum, plen):
	pack_seq = pack('B', seq)
	pack_sum = pack('I', checksum)
	pack_len = pack('H', plen)

	return pack_seq + pack_sum + pack_len

def gen_packet(header, payload):
	
	return header + payload

# make sure user added text file
if len(argv) != 2:
	print("Argument error, please provide necessary arguemnts")
	print("Usage: python3 sender.py <filename>")
	exit(1)


# open file and read data as ascii
file = open(argv[1], 'r')

# create udp socket
client_sock = socket(AF_INET, SOCK_DGRAM)

# create acknowledge number variable 
# its updated inside the loop
ack_num = 0


# create reliable packet
for idx, line in enumerate(file):

	# generate necessary info for packet generation
	data = line
	data_len = len(data)
	seq_num = idx
	byte_data = bytes(data, 'ascii')


	# create checksum
	checksum = gen_checksum(seq_num, data_len, byte_data)

	# create header
	header = pack_header(seq_num, checksum, data_len)

	# create packet
	reliable_packet = gen_packet(header, byte_data)


	while True:
		# send packet
		client_sock.sendto(reliable_packet, addr)


		if debug:
			print('this is my data payload:', byte_data)
			print('this is my data payaload sum:', sum(byte_data))
			print('this is my data length:', data_len)
			print('this is my sequence number:', seq_num)
			print('this is my checksum:', checksum)
			print('this is my header:', header)
			print('this is my packet:', reliable_packet)
			print('-------------------------------------------------------------------------------------\n\n')

		try:
			client_sock.settimeout(3)
			r_pkt = client_sock.recvfrom(1024)
			client_sock.settimeout(None) 
			ack_num = int.from_bytes(r_pkt[0], 'big')

			# case for seq number 4 due to a bug in the server
			# the ack will send 6 instead of 5
			if seq_num == ack_num - 2:
				if debug:
					print("ACK number is 6, changing to 5")
				ack_num = 5

			# print out ack number
			print("ACK: ", ack_num)
			print('-------------------------------------------------------------------------------------\n\n')


			# if ack matches sequence number then break out of loop
			if ack_num == (seq_num+1):
				break

			# if the possible ack mismatch then resend packet
			else:
				print('ACK number does not match sequence number, resending packet')
				print('-------------------------------------------------------------------------------------\n\n')
				continue
			
			

		except timeout:
			print('Timeout with packet with sequence number:', seq_num, "\n")
			print('Resending packet')
			print('\n\n')
			packet_loss_flag = 1
print("All packets recieved, file has been sent successfully, closing connection...")