import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Use localhost or 127.0.0.1 for connection
host = '127.0.0.1'
port = 65432  # Same port as used by the server

try:
    # Connection to the server
    client_socket.connect((host, port))

    # Receive message from the server
    message = client_socket.recv(1024).decode('utf-8')
    print(f"Server says: {message}")

    # Send a message to the server
    client_socket.send("Hello, Server!".encode('utf-8'))

except ConnectionRefusedError:
    print("Could not connect to the server. Make sure the server is running.")

finally:
    # Close the connection
    client_socket.close()
