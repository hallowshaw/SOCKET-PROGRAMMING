import socket

server_name = 'localhost'
server_port = 6889

# Create and bind the UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((server_name, server_port))

# Loop to receive and print messages
while True:
    msg, addr = s.recvfrom(1024)
    if not msg:
        break
    print("Received:", msg.decode())

# Close the socket
s.close()
