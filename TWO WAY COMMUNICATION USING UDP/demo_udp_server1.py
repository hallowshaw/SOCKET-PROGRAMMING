import socket

client_name = 'localhost'
client_port = 8001

# Create a UDP socket at server side 
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((client_name, client_port))

print("Server is up and running...")

while True:
    message, client_address = s.recvfrom(1024)
    print(f'Message from client: {message.decode()}')
    response = input("Message to client: ")
    s.sendto(response.encode(), client_address)

s.close() # This line will never be reached due to the infinite loop
