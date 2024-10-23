# -*- coding: utf-8 -*-
"""
2) Create a TCP client server program where the client sends a string, server converts to upper case
and replies
"""
import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = '172.16.116.14'  # Replace with the server's IP address
    client_socket.connect((server_ip, 12345))  # Connect to server's IP
    
    while True:
        message = input("Enter message to send (type 'exit' to quit): ")
        client_socket.sendall(message.encode())  # Send the message to the server
        if message.lower() == 'exit':
            break
        response = client_socket.recv(1024).decode()  # Receive response from the server
        print(f"Server replied: {response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
'''
OUTPUT
Enter message to send (type 'exit' to quit): yanu sweet
Server replied: YANU SWEET
Enter message to send (type 'exit' to quit): my bestie omg :3
Server replied: MY BESTIE OMG :3
Enter message to send (type 'exit' to quit): exit
'''
