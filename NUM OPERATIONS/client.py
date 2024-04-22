import socket

server_ip = '127.0.0.1'
server_port = 8002

s = socket.socket()  # Create client-side socket
s.connect((server_ip, server_port))

def get_input():
    return input('Enter operation number1 number2 (e.g., addition 5 3): ')

while True:
    data_to_server = get_input()  # Get client's message to server

    if data_to_server.lower() == 'exit':
        break

    s.send(data_to_server.encode())  # Send byte data to server

    data_from_server = s.recv(1024).decode()  # Receive data from server
    print(f'Result: {data_from_server}')  # Display server's message

s.close()  # Close connection
