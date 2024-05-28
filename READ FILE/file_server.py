import socket

host = 'localhost'
port = 8000

s = socket.socket() #create a TCP socket

s.bind((host,port)) #bind socket to host and port num

s.listen(1) #max 1 connection will be accepted

c, addr = s.accept() #wait till client connects
print('A client requested a connection')

fname = c.recv(1024) #accept file name from client

fname = str(fname.decode()) #decode filename to string format

print('Filename received from client: '+fname) 

try:
    f = open(fname, 'rb') #open the file at server side
    content = f.read() #read content of the file
    c.send(content) #send the content of the file, no need to use encode() as by default the content is read as byte
    f.close() #close the file
except FileNotFoundError:
    c.send(b'File does not exist')

c.close() #disconnect the server
