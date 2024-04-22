import socket

def addition(a, b):
    return str(a + b)

def subtraction(a, b):
    return str(a - b)

def multiplication(a, b):
    return str(a * b)

def division(a, b):
    if b == 0:
        return "Error: Division by zero"
    return str(a / b)

host = '127.0.0.1'
port = 8002

s = socket.socket()  # Create server-side socket
s.bind((host, port))  # Bind the socket to host and port
s.listen(1)  # Max number of connections allowed

print('Server is running...')

while True:
    c, addr = s.accept()  # Wait till a client connects
    print(f'A client connected from {addr}')

    while True:
        data_received = c.recv(1024)  # Receive byte data from client

        if not data_received or data_received.lower() == b'exit':
            break

        data = data_received.decode().split()
        if len(data) < 3:
            c.send("Error: Invalid input format".encode())
            continue

        operation, n1, n2 = data[0], int(data[1]), int(data[2])

        if operation == 'addition':
            result = addition(n1, n2)
        elif operation == 'subtraction':
            result = subtraction(n1, n2)
        elif operation == 'multiplication':
            result = multiplication(n1, n2)
        elif operation == 'division':
            result = division(n1, n2)
        else:
            result = "Error: Invalid operation"

        c.send(result.encode())  # Send the result to client in byte format

    c.close()  # Close client connection

s.close()  # Close server socket
