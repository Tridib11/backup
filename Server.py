import socket

s = socket.socket()  ##by default it will be TCP and ipv4
print("Socket Created")
s.bind(('localhost', 9999))
s.listen(3)
print("Waiting for connections")
while True:
    c,addr=s.accept()
    name = c.recv(1024).decode()
    print("Client connected with ",addr,name)

    c.send(bytes("Welcome to tridib",'utf-8'))
    c.close()
