import socket
server = socket.socket() 
server.bind(("", 5000))
server.listen(4) 
client_socket, client_address = server.accept()
print(client_address, "has connected")
while True:
    recvieved_data = client_socket.recv(1024)
    print(recvieved_data)
    dataenv = input("msg:")
    client_socket.send(dataenv)

