# -*- coding: utf-8 -*-
"""
4) Create a TCP Encryption Application
"""

import socket

def encrypt(text, shift):
    encrypted = ''.join(chr((ord(char) + shift) % 256) for char in text)
    '''
    for char in text:
        ecr=''.join(chr(ord(char)+3)%256)
    '''  
    return encrypted
def start_client():
    shift = 3  # Shift for Caesar cipher
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = '172.16.116.14'  # Replace with the server's IP address
    client_socket.connect((server_ip, 12345))

    while True:
        message = input("Enter message to send (type 'exit' to quit): ")
        if message.lower() == 'exit':
            break

        # Encrypt the message before sending
        encrypted_message = encrypt(message, shift)
        client_socket.sendall(encrypted_message.encode())

        # Receive the encrypted response from the server
        encrypted_response = client_socket.recv(1024).decode()
        print(f"Server replied (decrypted): {encrypted_response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
'''
output
Enter message to send (type 'exit' to quit): hii
Server replied (decrypted): kll
Enter message to send (type 'exit' to quit): how have you been
Server replied (decrypted): krz#kdyh#|rx#ehhq
Enter message to send (type 'exit' to quit): was it a good day
Server replied (decrypted): zdv#lw#d#jrrg#gd|
Enter message to send (type 'exit' to quit): exit
'''