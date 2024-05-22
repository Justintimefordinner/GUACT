import socket
import threading
from GUAC import GUAC
import queue
from time import sleep

# socket instance
socket_instance = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_instance.bind(('localhost', 8080))
socket_instance.listen(5)

game = GUAC()

# Dictionary to store the queues for each player
player_queues = {}

def game_lobby():
    while True:
        socket_connection, address = socket_instance.accept()
        uname = socket_connection.recv(1024).decode()
        print(f'{uname} connected')
        game.add_player(uname, address)
        
        # Create a new queue for the player
        player_queues[game.getID(uname)] = queue.Queue()
        
        threading.Thread(target=handle_user_connection, args=[socket_connection, address, game.getID(uname)]).start()
        
        # Display the current players in the lobby
        print('Current players in the lobby:')
        for player in game.players:
            print(player)
        
        # Send a start signal to all connected players
        for player_queue in player_queues.values():
            player_queue.put('start')

def server():
    # Start the game lobby in a separate thread
    threading.Thread(target=game_lobby).start()

    while True:
        sleep(1)  # Sleep to reduce CPU usage


def handle_user_connection(client: socket.socket, address: str, id: int) -> None:
    """
    Function to handle the server-side interaction.

    Parameters:
    connection (socket.socket): The connection object.
    address (str): The address of the client.

    Returns:
    None
    """
    while True:
        try:
            message = client.recv(1024).decode()
        except Exception:
            print(f'Player {id} disconnected')
            game.remove_player(id)
            del player_queues[id]
            break

        player_id, letter, timestamp = message.split(',')
        
        # Put the message in the player's queue
        player_queues[player_id].put((letter, timestamp))
        
        # Get the next message from the player's queue
        next_letter, next_timestamp = player_queues[player_id].get()
        
        game.checker(player_id, next_letter, next_timestamp)
        client.send(game.nextbase(player_id).encode())

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