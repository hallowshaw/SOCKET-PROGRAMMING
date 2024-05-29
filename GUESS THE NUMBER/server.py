import socket
import random

def start_game():
    number_to_guess = random.randint(1, 100)
    return number_to_guess

host = '127.0.0.1'
port = 8002

s = socket.socket()  # Create server-side socket
s.bind((host, port))  # Bind the socket to host and port
s.listen(1)  # Max number of connections allowed

print('Server is running...')

c, addr = s.accept()  # Wait till a client connects
print(f'A client connected from {addr}')

number_to_guess = start_game()
print(f"The number to guess is: {number_to_guess}")  # For debugging purposes

while True:
    data_received = c.recv(1024)  # Receive byte data from client

    if not data_received or data_received.lower() == b'exit':
        break

    try:
        guess = int(data_received.decode())
        if guess < number_to_guess:
            result = "Too low!"
        elif guess > number_to_guess:
            result = "Too high!"
        else:
            result = "Correct! You've guessed the number!"
            c.send(result.encode())
            number_to_guess = start_game()  # Restart game with a new number
            continue
    except ValueError:
        result = "Error: Invalid input"

    c.send(result.encode())  # Send the result to client in byte format

c.close()  # Close client connection
s.close()  # Close server socket
print('Server has shut down.')
