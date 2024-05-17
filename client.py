import socket


# Client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8080))
gamestart = False

def client_inst():
    uname = input('Enter your username: ')
    client.send(uname.encode())
    while gamestart == False:
        message = client.recv(1024).decode()
        print(f'message: {message}')
        if message == 'Game starting':
            gamestart = True
            print('Game starting')
            break
    
while True:
   client.send(input('=> ').encode())
   message = client.recv(1024).decode()
   print(f'message: {message}')
# client sends connection request/ready to play
