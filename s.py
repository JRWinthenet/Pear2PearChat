import socket
def externo():
    ipex = input("Insira O Ip Externo:")
    return ipex
opiniao = input("Colocar O Ip Externo? 's' ou 'n': ")
HOST = socket.gethostbyname(socket.gethostname())              
if opiniao == 's':
    ipext = externo()
    HOST = ipext
PORT = 5000            
print(f"Host: {HOST} Porta: {PORT}")
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

con, cliente = tcp.accept()
print(f'Concetado por {cliente}')
while True:
    msg = con.recv(1024)
    msgd = msg.decode()
    if not msg: break
    print(f"{cliente}  : {msgd} ")
print(f'Finalizando conexao do cliente {cliente}')
con.close()