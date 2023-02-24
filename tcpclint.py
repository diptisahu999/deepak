import socket
import sys
import time

# Creating the socket and accepting user input hostname
socket_server=socket.socket()
server_host=socket.gethostname()
ip=socket.gethostbyname(server_host)
s_port=8060

# Connection to the server
print("This is your IP address:",ip)
server_host=input("Enter friend's IP address:")
name=input("Enter your friend's name:")

socket_server.connect((server_host,s_port))

# Retrieving message from server
socket_server.send(name.encode())
server_name=socket_server.recv(1024)
server_name=server_name.decode()

print(server_name, "has joined...")
while True:
    message=socket_server.recv(1024).decode()
    print(server_name, ":", message)
    message=input("Me :")
    # lst2 = []
    # lst2 = [item for item in input("Enter the list items : ").split()]
    # print(lst2)
    # print(type(lst2))
    socket_server.send(message.encode())
    #socket_server.send(lst2.encode())