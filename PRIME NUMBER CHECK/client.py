import socket

server_ip = '127.0.0.1'
server_port = 8002

s = socket.socket()  # Create client-side socket
s.connect((server_ip, server_port))

def get_input():
    return input('Enter a number to check if it is prime (or type exit to quit): ')

while True:
    data_to_server = get_input()  # Get client's message to server

    if data_to_server.lower() == 'exit':
        s.send(data_to_server.encode())
        break

    s.send(data_to_server.encode())  # Send byte data to server

    data_from_server = s.recv(1024).decode()  # Receive data from server
    print(data_from_server)  # Display server's message

s.close()  # Close connection
