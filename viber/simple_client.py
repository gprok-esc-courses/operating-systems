from socket import socket, AF_INET, SOCK_STREAM

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect(('127.0.0.1', 5001))

data = client_socket.recv(1024)

print(data)