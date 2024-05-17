import socket
import threading


# Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8080))
server.listen(5)

def server_inst():
   while True:
       client, address = server.accept()
       threading.Thread(target=response_manager,args=(client,)).start()

def response_manager(client):
   while True:
       message = client.recv(1024)
       print('message: ', message.decode())
       message = input('=> ')
       client.send(message.encode())
server_inst()
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