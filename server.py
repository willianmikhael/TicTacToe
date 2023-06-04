import socket
import random
import client
class Server:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((socket.gethostname(), 1234))
        self.s.listen()

    def connect(self):
        self.clientsocket, address = self.s.accept()
        print(f"Connection from {address} has been established!")
        self.clientsocket.send(bytes("Welcome to the server!", "utf-8"))

    def swap(self):
        self.players = ["recive", "send"]
        random.choice(self.players)

        if self.players == "send":
            client.send()  # enviar atributo da minha posição no jogo
        else:
            client.recv(1024).decode("utf-8")  # recebe a posiço do oponente
            self.clientsocket.send(bytes("You Start! Good Luck!", "utf-8"))


    def run(self):
        self.connect()
        self.swap()