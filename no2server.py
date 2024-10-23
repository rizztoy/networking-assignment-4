# -*- coding: utf-8 -*-
"""
2) Create a TCP client server program where the client sends a string, server converts to upper case
and replies
"""

import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # Listen on all interfaces
    server_socket.listen(1)
    print("Server is listening on port 12345...")

    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr} has been established!")

    while True:
        data = client_socket.recv(1024).decode()
        if not data or data.lower() == 'exit':
            print("Connection closed by client.")
            break
        print(f"Received from client: {data}")
        data=data.upper()
        client_socket.sendall(data.encode())  # Echo back the received message

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
'''
OUTPUT
Server is listening on port 12345...
Connection from ('172.16.116.14', 51741) has been established!
Received from client: yanu sweet
Received from client: my bestie omg :3
Connection closed by client.
'''
