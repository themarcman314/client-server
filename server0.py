import socket
import string
import time

s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s_sock.bind(('localhost', 8000))

while True:
    s_sock.listen(5) # become a server socket, maximum 5 connections

    con, addr = s_sock.accept()

    print(f"Connection from port {str(con.getsockname()[1])}\nmsg : {con.recv(64).decode()}")
    con.send("Hi there !".encode())
    con.close()

    time.sleep(3)

    c_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_sock.connect(('localhost', 8001))

    c_sock.send("Hello from server 0!".encode())
    #reply1 = c_sock.recv(64)
    c_sock.close()


