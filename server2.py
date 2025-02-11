import socket
import string
import time

s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s_sock.bind(('localhost', 8002))

while True:
    s_sock.listen(5) # become a server socket, maximum 5 connections

    con, addr = s_sock.accept()
    buf = con.recv(64)
    print(f"Connection from port {str(con.getsockname()[1])}\nmsg : {buf}")
    reply = "hi there"
    con.send(reply.encode())
    con.close()

    time.sleep(3)

    c_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_sock.connect(('localhost', 8000))
    msg = "Hello from server 2!"
    e_msg = msg.encode()

    c_sock.send(e_msg)
    reply1 = c_sock.recv(64)
    c_sock.close

