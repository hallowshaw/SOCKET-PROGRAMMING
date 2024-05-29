import socket

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return f"{year} is a leap year"
    else:
        return f"{year} is not a leap year"

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
        year = int(data_received.decode())
        result = is_leap_year(year)
    except ValueError:
        result = "Error: Invalid input"

    c.send(result.encode())  # Send the result to client in byte format

c.close()  # Close client connection
s.close()  # Close server socket
print('Server has shut down.')
