"""
5) create a simulation of ftp using udp
"""
import socket
import os

# Client Configuration
HOST = input("Enter server IP address: ")
PORT = 2121

def list_files(conn):
    response = conn.recv(4096).decode()
    print("Files on server:\n", response)

def create_and_upload_file(conn, filename):
    print(f"Creating new file: {filename}")
    content = input("Enter content for the new file:\n")
    with open(filename, 'w') as file:
        file.write(content)
    print(f"File {filename} created locally.")

    # Proceed with upload
    upload_file(conn, filename)

def upload_file(conn, filename):
    if not os.path.exists(filename):
        create_choice = input(f"File {filename} does not exist. Create a new file and upload it? (yes/no): ").strip().lower()
        if create_choice == 'yes':
            create_and_upload_file(conn, filename)
        else:
            print("Upload cancelled.")
        return

    conn.sendall(f"UPLOAD {filename}".encode())
    # Wait for the server to be ready
    if conn.recv(1024) != b"READY":
        print("Server not ready for upload.")
        return

    with open(filename, 'rb') as file:
        while (data := file.read(1024)):
            conn.send(data)
    conn.send(b"END")
    response = conn.recv(1024)
    if response == b"UPLOAD_SUCCESS":
        print(f"Uploaded {filename} successfully.")

def download_file(conn, filename):
    conn.sendall(f"DOWNLOAD {filename}".encode())
    data = conn.recv(1024)

    if data == b"ERROR":
        print("File not found on the server.")
        return

    print(f"Downloading and saving file as server_copy_{filename}")
    # Save the file on the server's side after receiving
    conn.sendall(b"READY")
    with open(f"server_copy_{filename}", 'wb') as file:
        while data != b"END":
            file.write(data)
            data = conn.recv(1024)
    print(f"Downloaded and saved file as server_copy_{filename}")

# Client Function
def start_ftp_client():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((HOST, PORT))
        welcome_message = client_socket.recv(1024).decode()
        print(welcome_message)

        while True:
            command = input("ftp> ").strip()

            if command == "LIST":
                client_socket.send(command.encode())
                list_files(client_socket)

            elif command.startswith("UPLOAD"):
                _, filename = command.split(maxsplit=1)
                upload_file(client_socket, filename)

            elif command.startswith("DOWNLOAD"):
                _, filename = command.split(maxsplit=1)
                download_file(client_socket, filename)

            elif command == "QUIT":
                client_socket.send(command.encode())
                print("Exiting FTP client.")
                break
            else:
                print("Invalid command.")

        client_socket.close()
    except Exception as e:
        print(f"Connection error: {e}")

if __name__ == "__main__":
    start_ftp_client()
'''
output
Enter server IP address: 192.168.212.38
Welcome to FTP Server. Available commands: LIST, UPLOAD <filename>, DOWNLOAD <filename>, QUIT
ftp> LIST
Files on server:
 a.py
no1client.py
no1server.py
no2client.py
no2server.py
no3client.py
no3server.py
no4client.py
no4server.py
no5client.py
no5server.py
no6.server.py
no6client.py
ftp> download client.py
Invalid command.
ftp> DOWNLOAD client.py
File not found on the server.
ftp> upload client.py
Invalid command.
ftp> UPLOAD client.py
File client.py does not exist. Create a new file and upload it? (yes/no): yes
Creating new file: client.py
Enter content for the new file:
my name is gayyyyy
File client.py created locally.
Uploaded client.py successfully.
ftp> LIST
Files on server:
 a.py
client.py
no1client.py
no1server.py
no2client.py
no2server.py
no3client.py
no3server.py
no4client.py
no4server.py
no5client.py
no5server.py
no6.server.py
no6client.py
ftp> QUIT
Exiting FTP client.
'''
