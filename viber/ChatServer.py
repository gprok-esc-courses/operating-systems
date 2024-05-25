from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

class Connection:
    def __init__(self, conn, addr) -> None:
        self.conn = conn
        self.addr = addr
        self.name = None
        self.active = True


class ChatServer:
    def __init__(self) -> None:
        self.clients = []
        self.port = 5002
        self.server_socket = socket(AF_INET, SOCK_STREAM)
        self.server_socket.bind(('127.0.0.1', self.port))
        self.server_socket.listen()
        print("Server started on", self.port)

    def start(self):
        while True:
            print("Waiting for connection ...")
            conn, addr = self.server_socket.accept()
            print(addr, "connected")
            client = Connection(conn, addr)
            self.clients.append(client)
            th = Thread(target=self.client_thred, args=(client,))
            th.start()

    def broadcast(self, message, client_name):
        for client in self.clients:
            if client.name is not None and client.name != client_name and client.active:
                message = client_name + ": " + message
                client.conn.send(str.encode(message))

    def client_thred(self, client):
        name = client.conn.recv(1024).decode('utf-8')
        client.name = name
        message = "Welcome " + name
        client.conn.send(str.encode(message))
        while True:
            message = client.conn.recv(1024).decode('utf-8')
            if message == 'EXIT':
                message = "I'm leaving, bye!"
            # store in log file
            self.broadcast(message, client.name)
            client.active = False
            return



if __name__ == '__main__':
    server = ChatServer()
    server.start()
