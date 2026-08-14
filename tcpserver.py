import socket

TCP_PORT = 5000
IP_ADDR = '127.0.0.1'
BUF_SIZE = 1024



k = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
print("Server has created a socket")

k.bind((IP_ADDR, TCP_PORT))
print("Server has bound successfully")
k.listen(1)
print("Server is waiting for client connection")
con, addr = k.accept()

print ('Connection Address is: ' , addr)

msg = "Hello, I am server, nice to meet you".encode()

data = con.recv(BUF_SIZE)
print(data)

print ("Received data", data.decode())
con.send(msg)

con.close()



