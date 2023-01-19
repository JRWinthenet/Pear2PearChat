import socket
server = socket.socket() 
ip = input("Insert ip here: ")
server.bind((ip, 10020)) 
server.listen(4) 
client_socket, client_address = server.accept()
print(client_address, "has connected")
while True:
    recvieved_data = client_socket.recv(1024)
    print(recvieved_data)
