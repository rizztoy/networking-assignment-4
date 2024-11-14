"""
5) create a simulation of ftp using tc[
"""
import socket
import os

# Server Configuration
HOST = '0.0.0.0'
PORT = 2121

# Command Handlers
def list_files():
    files = os.listdir()
    return "\n".join(files) if files else "No files available."

def upload_file(conn, filename):
    print(f"Receiving file: {filename}")
    with open(filename, 'wb') as file:
        while True:
            data = conn.recv(1024)
            if data == b"END":
                print(f"Upload of {filename} completed.")
                break
            file.write(data)
    conn.send(b"UPLOAD_SUCCESS")

def download_file(conn, filename):
    if not os.path.exists(filename):
        conn.send(b"ERROR")
        return
    print(f"Saving downloaded file: {filename}")
    # Save the downloaded file in the server's directory
    with open(f"server_copy_{filename}", 'wb') as file:
        while True:
            data = conn.recv(1024)
            if data == b"END":
                break
            file.write(data)
    print(f"File {filename} saved to server as server_copy_{filename}")
    conn.send(b"DOWNLOAD_SUCCESS")

# Server Function
def start_ftp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"FTP Server listening on {HOST}:{PORT}...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connected by {addr}")
        conn.send(b"Welcome to FTP Server. Available commands: LIST, UPLOAD <filename>, DOWNLOAD <filename>, QUIT")

        while True:
            try:
                command = conn.recv(1024).decode().strip()
                if not command:
                    break

                if command == "LIST":
                    response = list_files()
                    conn.send(response.encode())

                elif command.startswith("UPLOAD"):
                    _, filename = command.split(maxsplit=1)
                    conn.send(b"READY")
                    upload_file(conn, filename)

                elif command.startswith("DOWNLOAD"):
                    _, filename = command.split(maxsplit=1)
                    download_file(conn, filename)

                elif command == "QUIT":
                    conn.send(b"Goodbye!")
                    conn.close()
                    print(f"Connection closed by {addr}")
                    break
                else:
                    conn.send(b"Invalid command.")
            except Exception as e:
                print(f"Error: {e}")
                conn.close()
                break

if __name__ == "__main__":
    start_ftp_server()

'''
output:
FTP Server listening on 0.0.0.0:2121...
Connected by ('192.168.212.38', 57361)
Receiving file: client.py
Upload of client.py completed.
Connection closed by ('192.168.212.38', 57361)
'''
