import socket
import time

server_name = 'localhost'
server_port = 6889

# Create the UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Optional wait time to ensure the server is ready
time.sleep(5)

# Send messages to the server
s.sendto(b"Hello class!! Welcome to your lab class", (server_name, server_port))
s.sendto(b"Goodbye!!", (server_name, server_port))

# Close the socket
s.close()
