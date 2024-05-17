import socket
import threading
import GUAC

# socket instance
socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_instance.bind(('localhost', 8080))
socket_instance.listen(5)

def server():
   while True:
       socket_connection, address = socket_instance.accept()
       threading.Thread(target=handle_user_connection, args=[socket_connection, address]).start()

def response_manager(client):
   while True:
       message = client.recv(1024)
       print('message: ', message.decode())
       message = input('=> ')
       client.send(message.encode())

def handle_user_connection(connection: socket.socket, address: str) -> None:
    pass

server()
# serverside - loads dna strand
# client sends connection request/ready to play
# game starts
# server sends 1 nucleotide to client at a time
# players send string of playerID, complement nucleotide, and a timestamp
# server checks if the string is valid
# server scores the string
# server sends updated scoreboards to all players
# game ends when all nucleotides are sent
# server sends game over message to all players
# server sends final scoreboards to all players