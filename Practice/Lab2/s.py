import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1", 5000))
# server.listen(1)
print("Server listening at 5000")

while True:
    data, add = server.recvfrom(1024)

    if data:
        print(data)
        server.sendto(data.decode().upper().encode(), add)
