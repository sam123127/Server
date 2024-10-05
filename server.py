import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get local machine name (hostname)
host = socket.gethostname()
port = 12345  # Reserve a port for the service.

# Bind to the port
server_socket.bind((host, port))

# Start listening for connections
server_socket.listen(5)

print(f"Server started at {host} on port {port}. Waiting for connections...")

while True:
    # Establish a connection with the client
    client_socket, addr = server_socket.accept()
    print(f"Got connection from {addr}")

    # Send a message to the client
    message = 'Thank you for connecting!'
    client_socket.send(message.encode('utf-8'))

    # Receive message from the client
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received from client: {data}")

    # Close the connection
    client_socket.close()
