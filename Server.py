import socket

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Server is listening on {}:{}'.format(*server_address))

while True:
    # Wait for a connection
    print('Waiting for a connection...')
    client_socket, client_address = server_socket.accept()
    print('Connection from', client_address)

    # Receive and send back data
    data = client_socket.recv(1024)
    print('Received:', data.decode('utf-8'))
    client_socket.sendall(b'Thank you for connecting!')

    # Clean up the connection
    client_socket.close()
