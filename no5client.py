"""
5) create a simulation of ftp using udp
"""

import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_ip = '172.16.116.14'  # Replace with the server's IP address
    server_address = (server_ip, 12345)

    filename = input("Enter the name of the file to request: ")
    client_socket.sendto(filename.encode(), server_address)

    with open(f"received_{filename}", 'wb') as f:
        while True:
            data, _ = client_socket.recvfrom(1024)  # Receive data
            if not data:
                break
            f.write(data)
            print(f"Received {len(data)} bytes.")

    print(f"File {filename} has been received.")
    client_socket.close()

if __name__ == "__main__":
    start_client()

'''
output
Enter the name of the file to request: hiii.txt
Received 113 bytes.
'''