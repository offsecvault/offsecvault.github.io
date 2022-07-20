
#!/bin/python3

# we are going to work with sockets

import socket

HOST = "127.0.0.1"
PORT = 7777

con = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_NET means for IPv4 and the SOCK_STREAM is a port
con.connect((HOST,PORT))
print("DONE")

