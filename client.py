import socket

clientsocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket1.connect(('localhost', 8000))

#clientsocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#clientsocket2.connect(('localhost', 8001))

#clientsocket3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#clientsocket3.connect(('localhost', 8002))

msg = "Hello World!"
e_msg = msg.encode()

clientsocket1.send(e_msg)
reply1 = clientsocket1.recv(64)

#clientsocket2.send(e_msg)
#reply2 = clientsocket2.recv(64)

#clientsocket3.send(e_msg)
#reply3 = clientsocket3.recv(64)

print(f"Server replied : {reply1}")
#print(f"Server replied : {reply2}")
#print(f"Server replied : {reply3}")
