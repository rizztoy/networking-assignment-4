"""
6) Clients sends a string, Server calculates Hash value and replies back to Client using TCP
"""

import socket

def main():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 65432)
    client_socket.connect(server_address)

    try:
        message = input("Enter a string to hash: ")
        
        # Send data
        client_socket.sendall(message.encode())

        # Receive response
        hash_value = client_socket.recv(1024).decode()
        print("Received Hash:", hash_value)
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
'''
output

Enter a string to hash: hii hello haha 
Received Hash: 6da4a195e6fd1a0ec789e37bc8b5d77326db222f998ca251456b328fbcecb2e4
'''