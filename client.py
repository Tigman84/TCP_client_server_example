import socket

# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the server's address and port
server_address = ('localhost', 12345)
client_socket.connect(server_address)

try:
    # Send data
    message = 'Hello, TCP Server!'
    print('Sending:', message)
    client_socket.sendall(message.encode('utf-8'))

    # Receive response
    data = client_socket.recv(1024)
    print('Received:', data.decode('utf-8'))

finally:
    # Clean up the connection
    client_socket.close()
