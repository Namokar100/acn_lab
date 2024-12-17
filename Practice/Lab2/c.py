import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client.connect(("127.0.0.1", 5000))

msg = input("Enter the message: ")
client.sendto(msg.encode(), ("127.0.0.1", 5000))

data, _ = client.recvfrom(1024)

print("Received data ", data.decode())