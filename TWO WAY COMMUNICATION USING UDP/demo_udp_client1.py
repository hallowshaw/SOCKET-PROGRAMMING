import socket

server_name = 'localhost'
server_port = 8001

# Create a client side UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address_port = (server_name, server_port)

print("Client is up and running...")

data_to_send = input("Data to server: ")
while data_to_send.lower() != 'exit':
    s.sendto(data_to_send.encode(), server_address_port)
    response, _ = s.recvfrom(1024)
    print(f'Message from server: {response.decode()}')
    data_to_send = input("Data to server: ")

s.close()
