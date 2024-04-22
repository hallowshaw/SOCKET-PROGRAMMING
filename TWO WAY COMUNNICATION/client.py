import socket

server_name = 'localhost'
server_port = 9000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_ip = socket.gethostbyname(server_name)
s.connect((server_ip, server_port))

while True:
    # Sending message to server
    msg = input("Enter your message: ")
    s.send(msg.encode())

    # Receiving message from server
    received_msg = s.recv(1024).decode()
    print('Received:', received_msg)

    if received_msg.lower() == 'bye':
        break

s.close()
