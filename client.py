# import socket
# client=socket.socket()
# client.connect(('localhost',9999))
# name=input("Enter your name")
# client.send(bytes(name,'utf-8'))
# thiername=client.recv(1024).decode()
# print("Connected to ",thiername)
# while True:
#     recdata=client.recv(1024).decode()
#     print(thiername," : ",recdata)
#     data=input("You : ")
#     client.send(bytes(data,'utf-8'))
#     client.close()

import socket

client = socket.socket()
client.connect(('172.20.10.5', 9999))

name = input("Enter your name: ")
client.send(bytes(name, 'utf-8'))

their_name = client.recv(1024).decode()
print("Connected to:", their_name)

while True:
    rec_data = client.recv(1024).decode()
    print(their_name, ":", rec_data)

    data = input("You: ")
    client.send(bytes(data, 'utf-8'))

    if data == "bye":
        break

client.close()
print("Connection closed.")

