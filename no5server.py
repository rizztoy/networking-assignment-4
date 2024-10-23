"""
5) create a simulation of ftp using udp
"""


import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', 12345))  # Listen on port 12345
    print("Server is listening on port 12345...")

    while True:
        request, client_address = server_socket.recvfrom(1024)
        filename = request.decode()
        print(f"Request for file: {filename} from {client_address}")

        try:
            with open(filename, 'rb') as f:
                while (data := f.read(1024)):  # Read file in chunks
                    server_socket.sendto(data, client_address)
            print(f"File {filename} sent to {client_address}.")
        except FileNotFoundError:
            error_message = f"File {filename} not found."
            server_socket.sendto(error_message.encode(), client_address)

if __name__ == "__main__":
    start_server()


'''
output

Server is listening on port 12345...
Request for file: hiii.txt from ('172.16.116.14', 56855)
File hiii.txt sent to ('172.16.116.14', 56855).
'''