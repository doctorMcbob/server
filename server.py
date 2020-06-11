"""
server
"""
import socket
import select

from controller import resolve

CONNECTION_LIST = []
RECV_BUFFER = 4096
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(("10.0.0.143", PORT))
server_socket.listen(10)

CONNECTION_LIST.append(server_socket)

print("opened on port " + str(PORT))

while True:
    read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])

    for sock in read_sockets:
        #New connection
        if sock == server_socket:
            sockfd, addr = server_socket.accept()
            CONNECTION_LIST.append(sockfd)
            print("Client " + str(addr) + " connected")
        #Some incoming message from a client
        else:
            # Data recieved from client, process it
            try:
                data = sock.recv(RECV_BUFFER)
                # Echo data
                if data:
                    try:
                        resolve(data.decode("utf-8"))
                        print('here')
                        sock.send("OK ... " + data)
                    except:
                        sock.send("FAILED ... " + data)
            # Disconnected, remove from list
            except:
                print("Client " + str(addr) + " is offline")
                sock.close()
                CONNECTION_LIST.remove(sock)
                continue

server_socket.close()
