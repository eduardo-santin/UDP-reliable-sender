Eduardo Santín
CCOM 4205
Project 2 - Proyecto Transport Layer - rdtclient
This project is a UDP client with the caviat that we add a header to it to make it more reliable like the TCP protocol.

The header additions were the following:
a sequence number
a checksum
and a payload length

To test this the professor has a set a server client that will send back an
acknowledgement number to the client and also mimicking packet loss and corruption
to test the reliability of the client.


Requirements:
1.python 3
2.text file with text inside of it, preferably divided by lines but not necessary

How to run:
1. Open a terminal and navigate to the directory where the files are located.

2. Run the command: python3 rtdclient.py \<txt file\> 

3. The program will run and send the text file to the server and the server will send back an acknowledgement number in the terminal.
