import socket
import threading


class Serveur:
    def __init__(self, hote, port):
        self.hote = hote
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.hote, self.port))
        self.clients = []
        self.pseudos = []


    def diffusion(self, message):
        for client in self.clients:
            client.send(message)


    def gerer_client(self, client):
        while True:
            try:
                message = client.recv(1024)
                self.diffusion(message)
            except Exception as e:
                print(f"Erreur lors du traitement du client : {e}")
                index = self.clients.index(client)
                self.clients.remove(client)
                client.close()
                pseudo = self.pseudos[index]
                self.diffusion(f'{pseudo} a quitté la discussion'.encode('utf-8'))
                self.pseudos.remove(pseudo)
                break


def recevoir():
    while True:
        client, adresse = server_socket.accept()
        print(f"connecté avec {str(adresse)}")
        client.send('pseudo'.encode('utf-8'))
        pseudo = client.recv(1024).decode('utf-8')
        pseudos.append(pseudo)
        clients.append(client)
        print(f"Le pseudo du client est {pseudo}")
        diffusion(f'{pseudo} a rejoint le chat'.encode('utf-8'))
        thread = threading.Thread(target=gerer, args=(client,))
        thread.start()


print("serveur en écoute")
recevoir()
