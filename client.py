import socket
import server
class Server:
    def __init__(self, IP_Adrress, Port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect(("{}".format(IP_Adrress), Port))

        msg = self.s.recv(1024)
        print(msg.decode("utf-8"))

    def swap(self):
        server.recv(1024).decode("utf-8")  # recebe a posiço do oponente

        server.send(  # enviar atributo da minha posição no jogo)






