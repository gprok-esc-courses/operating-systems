from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import os

class ChatClient:
    def __init__(self, port) -> None:
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(('127.0.0.1', port))

    def start(self):
        name = input("Give your usename:")
        self.client_socket.send(str.encode(name))
        message = self.client_socket.recv(1024).decode('utf-8')
        print(message)
        th = Thread(target=self.client_thread)
        th.start()

        while True:
            message = input("What's up? ")
            self.client_socket.send(str.encode(message))
            if message == "EXIT":
                print("Bye ...")
                os._exit(0)

    def client_thread(self):
        while True:
            message = self.client_socket.recv(1024).decode('utf-8')
            print(message)


if __name__ == '__main__':
    client = ChatClient(5002)
    client.start()