import socket

clientsocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket1.connect(('localhost', 8000))

clientsocket1.send("Hello World!".encode())
print(f"Server replied : {clientsocket1.recv(64).decode()}")
