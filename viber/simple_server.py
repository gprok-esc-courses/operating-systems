from socket import socket, AF_INET, SOCK_STREAM

server_socket = socket(AF_INET, SOCK_STREAM)

server_socket.bind(('127.0.0.1', 5001))
server_socket.listen()
message = b"Welcome!"
print("Server started")

while True:
    conn, addr = server_socket.accept()
    print(addr, "connected")
    conn.send(message)

    

