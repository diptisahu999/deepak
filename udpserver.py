# import socket
# import threading
# import sys
#
# socket_server=socket.socket()
# host_name=socket.gethostname()
# ip=socket.gethostbyname(host_name)
# port=8070
#
# if len(sys.argv) == 3:
#     # Get "IP address of Server" and also the "port number" from argument 1 and argument 2
#     ip = sys.argv[1]
#     port = int(sys.argv[2])
# else:
#     print("Run like : python3 server.py <arg1:server ip:this system IP 192.168.1.6> <arg2:server port:4444 >")
#     # exit(1)
#
# # Create a UDP socket
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# # Bind the socket to the porth
# server_address = (ip, port)
# s.bind(server_address)
# # print("Do Ctrl+c to exit the program !!")
#
# while True:
#     print("####### Server is listening #######")
#     data, address = s.recvfrom(4096)
#     print("\n\n 2. Server received: ", data.decode('utf-8'), "\n\n")
#     send_data = input("Type some text to send => ")
#     s.sendto(send_data.encode('utf-8'), address)
#     print("\n\n 1. Server sent : ", send_data,"\n\n")



import socket

s=socket.socket()

host='127.0.0.1'
port=8000
s.bind((host,port))
print("sdhgds hsdgsd")
s.listen(2)
conn,addr=s.accept()
print(addr,"as connected")
while 1:
    message=input(str("you:>>"))
    message=message.encode()
    conn.send(message)
    incoming_message=conn.recv(1024)
    incoming_message=incoming_message.decode()
    print(("clint:>>",incoming_message))
