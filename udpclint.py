# import socket
# import sys
#
# socket_server=socket.socket()
# server_host=socket.gethostname()
# ip=socket.gethostbyname(server_host)
# port=8070
# if len(sys.argv) == 3:
#     # Get "IP address of Server" and also the "port number" from argument 1 and argument 2
#     ip = sys.argv[1]
#     port = int(sys.argv[2])
# else:
#     print("Run like : python3 client.py <arg1 server ip 192.168.1.102> <arg2 server port 4444 >")
#
#
# # Create socket for server
# s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
# print("Do Ctrl+c to exit the program !!")
#
# # Let's send data through UDP protocol
# while True:
#     send_data = input("Type some text to send =>")
#     s.sendto(send_data.encode('utf-8'), (ip, port))
#     print("\n\n 1. Client Sent : ", send_data, "\n\n")
#     data, address = s.recvfrom(4096)
#     print("\n\n 2. Client received : ", data.decode('utf-8'), "\n\n")
# # close the socket
# s.close()



import socket

s=socket.socket()

host='127.0.0.1'
port=8000
try:
    s.connect((host,port))
    print("connected to server")
except:
    print("derdyrdi gytfy")
while 1:
    incoming_message=s.recv(1024)
    incoming_message=incoming_message.decode()
    print("server:>>",incoming_message)
    message=input(str("you:>>"))
    message=message.encode()
    s.send(message)