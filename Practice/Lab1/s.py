import socket

server = socket.socket()
server.bind(("127.0.0.1", 5000))
server.listen(1)
print("Listening at port 5000")

while True:
    con, adr = server.accept()
    print(f"Client connected with address {adr}")
    
    fname = con.recv(1024).decode()

    try:
        with open(fname, 'r') as file:
            con.send(file.read().encode())
    except FileNotFoundError:
        con.send("File not found")
    con.close()