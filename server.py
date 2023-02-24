# import socket
#
# localIP = "127.0.0.1"
# localPort = 20001
# bufferSize = 1024
# msgFromServer = "Hello UDP Client"
# bytesToSend = str.encode(msgFromServer)
# # Create a datagram socket
# UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# # Bind to address and ip
# UDPServerSocket.bind((localIP, localPort))
# print("UDP server up and listening")
# # Listen for incoming datagrams
# while (True):
#     bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
#     message = bytesAddressPair[0]
#     address = bytesAddressPair[1]
#
#     clientMsg = "Message from Client:{}".format(message)
#     clientIP = "Client IP Address:{}".format(address)
#
#     print(clientMsg)
#     print(clientIP)
#     # Sending a reply to client
#     UDPServerSocket.sendto(bytesToSend, address)


# import socket
#
# ip="127.0.0.1"
# port=5001
#
#
# msg=b"hello world"
# print(f'sending {msg} to {ip}:{port}')
# sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# sock.sendto(msg,(ip,port))


import socket
import threading
import os

s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM )
s.bind(("192.168.1.58",2223))
print("\t\t\t====>  UDP CHAT APP  <=====")
print("==============================================")
nm = input("ENTER YOUR NAME : ")
print("\nType 'quit' to exit.")

ip,port = input("Enter IP address and Port number: ").split()

def send():
    while True:
        ms = input(">> ")
        if ms == "quit":
            os._exit(1)
        sm = "{}  : {}".format(nm,ms)
        s.sendto(sm.encode() , (ip,int(port)))

def rec():
    while True:
        msg = s.recvfrom(1024)
        print("\t\t\t\t >> " +  msg[0].decode()  )
        print(">> ")
x1 = threading.Thread( target = send )
x2 = threading.Thread( target = rec )

x1.start()
x2.start()