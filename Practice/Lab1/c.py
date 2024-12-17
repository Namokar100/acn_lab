import socket

client = socket.socket()
client.connect(("127.0.0.1", 5000))
print("Connected to server")

fname = input("Enter the filename: ")
client.send(fname.encode())

filedata = client.recv(1024).decode()

print(filedata)