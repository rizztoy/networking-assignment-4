"""
6) Clients sends a string, Server calculates Hash value and replies back to Client using TCP
"""

import socket
import hashlib

def calculate_hash(data):
    # Use SHA-256 hash function
    hash_object = hashlib.sha256(data.encode())
    return hash_object.hexdigest()

def main():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 65432)
    server_socket.bind(server_address)

    # Listen for incoming connections
    server_socket.listen(1)
    print("Server is listening on port", server_address[1])

    while True:
        connection, client_address = server_socket.accept()
        try:
            print("Connection from", client_address)
            data = connection.recv(1024).decode()
            print("Received:", data)

            # Calculate hash
            hash_value = calculate_hash(data)
            print("Calculated Hash:", hash_value)

            # Send the hash value back to the client
            connection.sendall(hash_value.encode())
        finally:
            connection.close()

if __name__ == "__main__":
    main()

'''
output

Server is listening on port 65432
Connection from ('127.0.0.1', 11305)
Received: yanu you make me feel living
Calculated Hash: ab0882e2a183ffcc20885f72348f45f398566569c8ff2ad38a7be31a436d2804
Connection from ('127.0.0.1', 11319)
Received: hii hello haha 
Calculated Hash: 6da4a195e6fd1a0ec789e37bc8b5d77326db222f998ca251456b328fbcecb2e4
'''