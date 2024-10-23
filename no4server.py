# -*- coding: utf-8 -*-
"""
4) Create a TCP Encryption Application
"""

import socket

def encrypt(text, shift):
    encrypted = ''.join(chr((ord(char) + shift) % 256) for char in text)
    return encrypted

def decrypt(text, shift):
    decrypted = ''.join(chr((ord(char) - shift) % 256) for char in text)
    return decrypted

def start_server():
    shift = 3  # Shift for Caesar cipher
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))  # Listen on all interfaces
    server_socket.listen(1)
    print("Server is listening on port 12345...")
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr} has been established!")
    while True:
        encrypted_data = client_socket.recv(1024).decode()
        if not encrypted_data:
            print("Connection closed by client.")
            break
        # Decrypt the received message
        decrypted_data = decrypt(encrypted_data, shift)
        print(f"Received (decrypted): {decrypted_data}")

        # Optionally, echo back the decrypted message (encrypted)
        encrypted_response = encrypt(decrypted_data, shift)
        client_socket.sendall(encrypted_response.encode())

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
 
'''
logic :: 
Custom Encryption (Caesar Cipher):

The encrypt function shifts each character by a fixed number of positions (in this case, 3) in the ASCII table.
The decrypt function reverses this operation.
'''
    
'''
output
Server is listening on port 12345...
Connection from ('172.16.116.14', 52099) has been established!
Received (decrypted): hii
Received (decrypted): how have you been
Received (decrypted): was it a good day
Connection closed by client.
'''