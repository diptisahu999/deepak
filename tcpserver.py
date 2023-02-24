import socket
import sys
import time

# Creating the sockets and retrieving host name
new_socket=socket.socket()
host_name=socket.gethostname()
s_ip=socket.gethostbyname(host_name)
port=8060

# Bind the host and port
new_socket.bind((host_name,port))
print("binding successful..")
print("This is your ip.",s_ip)

# Listening for connections
name=input("Enter your name:")
new_socket.listen(2)

# Accepting Incoming Connections
conn,addr=new_socket.accept()
print("Received connection from",addr[0])
print("Connection established. connection from",addr[0])

# Storing incoming connection data
client=(conn.recv(1024)).decode()
print(client + "has connected")
conn.send(name.encode())

# Delivering message
while True:
    message=input("Me :")
    # lst2 = []
    # lst2 = [item for item in input("Enter the list items : ").split()]
    # print(lst2)
    # print(type(lst2))
    conn.send(message.encode())
    message=conn.recv(1024)
    message=message.decode()
    print(client, ":", message)
    # conn.send(lst2.encode())
    # lst2 = conn.recv(1024)
    # message = lst2.decode()
    # print(client, ":", lst2)