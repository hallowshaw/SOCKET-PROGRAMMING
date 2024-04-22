import socket

own_name = 'localhost'
own_port = 9000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((own_name, own_port))
s.listen(1)

c, addr = s.accept()
print('Connection from:', str(addr))

while True:
    # Receiving message from client
    received_msg = c.recv(1024).decode()
    if not received_msg:
        break
    print('Received:', received_msg)

    # Sending messages to client
    msg = input("Enter your message: ")
    c.send(msg.encode())

c.close()
s.close()
