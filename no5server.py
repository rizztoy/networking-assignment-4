"""
5) create a simulation of ftp using udp
"""
import socket

def start_ftp_server(host='127.0.0.1', port=2121):
    files = {}

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f'Server is listening on {host}:{port}')

        while True:
            conn, addr = server_socket.accept()
            with conn:
                print(f'Connected by {addr}')
                while True:
                    command = conn.recv(1024).decode()
                    if not command:
                        break

                    print(f'Received command: {command}')
                    if command.startswith('UPLOAD'):
                        _, filename, *content = command.split()
                        content_string = ' '.join(content)
                        files[filename] = content_string
                        print(f'Uploaded {filename} with content: {content_string}')

                    elif command.startswith('DOWNLOAD'):
                        _, filename = command.split()
                        if filename in files:
                            print(f'Downloading {filename}...')
                            conn.sendall(f'EXISTS {files[filename]}'.encode())
                        else:
                            conn.sendall(b'NOTFOUND')

                    elif command == 'QUIT':
                        print('Client disconnected.')
                        break

if __name__ == "__main__":
    start_ftp_server()
    