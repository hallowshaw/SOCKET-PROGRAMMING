import socket

def is_prime(n):
    if n <= 1:
        return f"{n} is not a prime number"
    if n <= 3:
        return f"{n} is a prime number"
    if n % 2 == 0 or n % 3 == 0:
        return f"{n} is not a prime number"
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return f"{n} is not a prime number"
        i += 6
    return f"{n} is a prime number"

host = '127.0.0.1'
port = 8002

s = socket.socket()  # Create server-side socket
s.bind((host, port))  # Bind the socket to host and port
s.listen(1)  # Max number of connections allowed

print('Server is running...')

c, addr = s.accept()  # Wait till a client connects
print(f'A client connected from {addr}')

while True:
    data_received = c.recv(1024)  # Receive byte data from client

    if not data_received or data_received.lower() == b'exit':
        break

    try:
        n = int(data_received.decode())
        result = is_prime(n)
    except ValueError:
        result = "Error: Invalid input"

    c.send(result.encode())  # Send the result to client in byte format

c.close()  # Close client connection
s.close()  # Close server socket
print('Server has shut down.')
