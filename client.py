import socket
import datetime

# Client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8080))
gamestart = False

def client_init():
    """
    Function to handle the client-side interaction.

    This function prompts the user to enter their username, sends it to the server,
    and waits for the game to start. Once the game starts, it prints a message and exits the loop.

    Parameters:
    None

    Returns:
    None
    """
    uname = input('Enter your username: ')
    client.send(uname.encode())
    while gamestart == False:
        message = client.recv(1024).decode()
        print(f'message: {message}')
        if message == 'Game starting':
            gamestart = True
            print('Game starting')
            break
        
def conn()

 
while True:
    print(client.recv(1024))
    client.send(input('=> ').encode())
    message = client.recv(1024).decode()
    print(f'message: {message}')
# client sends connection request/ready to play
