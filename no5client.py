"""
5) create a simulation of ftp using udp
"""
import socket

def start_ftp_client(host='127.0.0.1', port=2121):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f'Connected to FTP server at {host}:{port}')

        while True:
            command = input("Enter command (UPLOAD filename content, DOWNLOAD filename, QUIT): ")
            client_socket.sendall(command.encode())

            if command.startswith('UPLOAD'):
                _, filename, *content = command.split()
                content_string = ' '.join(content)
                print(f'Sending {filename} with content: {content_string}')

            elif command.startswith('DOWNLOAD'):
                _, filename = command.split()
                response = client_socket.recv(1024).decode()
                if response.startswith('EXISTS'):
                    content = response.split(' ', 1)[1]
                    print(f'Downloaded {filename} with content: {content}')
                else:
                    print(f'File {filename} not found on server.')

            elif command == 'QUIT':
                print('Disconnecting from server.')
                break

if __name__ == "__main__":
    start_ftp_client()



"""
Connected to FTP server at 127.0.0.1:2121
Enter command (UPLOAD filename content, DOWNLOAD filename, QUIT): UPLOAD ftp.txt FTP, or File Transfer Protocol, is a standard network protocol used to transfer files between a client and a server on a 
computer network.
Sending ftp.txt with content: FTP, or File Transfer Protocol, is a standard network protocol used to transfer files between a client and a server on a computer network.
Enter command (UPLOAD filename content, DOWNLOAD filename, QUIT): DOWNLOAD ftp.txt
Downloaded ftp.txt with content: FTP, or File Transfer Protocol, is a standard network protocol used to transfer files between a client and a server on a computer network.
Enter command (UPLOAD filename content, DOWNLOAD filename, QUIT): QUIT
Disconnecting from server.
"""
