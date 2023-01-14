import socket
hos = input("Digite o ip ou host do servidor: ")

HOST = hos     
PORT = 5000            
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print('Para sair use CTRL+X\n')
msg = "t"
while msg != '\x18':
    msg = input()
    msgb = msg.encode()
    tcp.send(msgb)
tcp.close()