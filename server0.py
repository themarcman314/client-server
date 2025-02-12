import socket
import string
import time

class Node:
    current_leader:int
    counter:int
    id:int
    port:int
    consensus:bool


max_id = 0
max_port = 7999
#def propose():
    #send

#def propose_send():
    #check propose
        # if oks > n/2
        # consensus_send(counter,id,value)

def createNode()->Node:
    new_node:Node = Node()
    current_leader:Node = None
    counter:int = 0
    id:int = max_id+1
    port:int = max_port+1
    consensus:bool = False


def helper_send(destination_port:int, round_counter:int, value:int):
    c_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c_sock.connect('localhost', destination_port)

    msg = str(round_counter) + " " + str(value)

    c_sock.send(msg.encode())
    reply = c_sock.recv(64).decode()
    c_sock.close()
    if reply == "ok":
        return True
    return False
    
#def proposal_send(round_counter:int, sender_id:int, value:int):


# consensus send
    #def c_send(n_sending:Node,value:int):
    #    c_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #    c_sock.connect(('localhost', ))
    #
    #    c_sock.send("Hello from server 0!".encode())
    #    #reply1 = c_sock.recv(64)
    #    c_sock.close()




def main():
    new_node = createNode()

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
        helper_send(8001, 1, 1234)
#def helper_send(destination_port:int, round_counter:int, value:int):

if __name__ == "__main__":
    main()
