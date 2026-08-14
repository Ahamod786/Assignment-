import socket

TCP_PORT = 5000
IP_ADDR = '127.0.0.1'

BUF_SIZE = 1024

MSG = "Hello"



k = socket.socket (socket.AF_INET, socket.SOCK_STREAM)

k.connect((IP_ADDR, TCP_PORT))
print("Clint has sent connection request")

k.send(MSG.encode())

data = k.recv(BUF_SIZE)

print(data.decode())

k.close

