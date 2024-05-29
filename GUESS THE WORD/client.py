import socket

server_ip = '127.0.0.1'
server_port = 8002

s = socket.socket()
s.connect((server_ip, server_port))

print(s.recv(1024).decode())  # Welcome message
name = input("Enter your name: ").strip()
s.send(name.encode())

while True:
    current_state = s.recv(1024).decode()
    if "Congratulations!" in current_state or "Game over!" in current_state:
        print(current_state)
        break

    print(current_state)
    guess = input('Enter your guess (or type exit to quit): ')
    
    if guess.lower() == 'exit':
        s.send(guess.encode())
        break

    s.send(guess.encode())
    response = s.recv(1024).decode()
    print(response)

s.close()
