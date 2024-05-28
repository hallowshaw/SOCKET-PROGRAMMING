import socket

server_name = 'localhost'
server_port = 8000

s = socket.socket() #create TCP socket

s.connect((server_name,server_port)) #connect to server

filename = input('Enter filename: ') #provide the filename

#filename = 'test_md.txt'

s.send(filename.encode()) #send the filename to the server

content = s.recv(1024) #receive file content from server

print(content.decode()) #print the content in string format

s.close() #close the connection
