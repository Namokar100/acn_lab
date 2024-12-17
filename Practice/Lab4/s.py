import socket

def calc(data: bytes):
    cs = 0
    for i in range(0, len(data), 2):
        word = (data[i] << 8) + (data[i+1] if i+1 < len(data) else 0)
        cs += word
        cs = (cs & 0xFFFF) + (cs >> 16)
    return ~cs & 0xFFFF

# def calc(data: bytes):
#     cs = 0
#     for i in range(0, len(data), 2):
#         word = (data[i]<<8) + (data[i+1] if i+1 < len(data) else 0)
#         cs += word
#         cs = (cs&0xFFFF) + (cs >> 16)
#     return ~cs&0xFFFF

server = socket.socket()
server.bind(("127.0.0.1", 5000))
server.listen(1)
print("Listening at 5000")

con, _ = server.accept()
print("Client connected")

m = con.recv(1024)
msg, cs = m.rsplit(b'|', 1)

print("Received msg", msg.decode())
print("Received cs", cs.decode())

calc_cs = hex(calc(msg))

if calc_cs == cs.decode():
    print("Success")
else:
    print("Failure")

con.close()
server.close()

