import socket
import struct

def calc(data: bytes):
    cs = 0
    for i in range(0, len(data), 2):
        word = (data[i]<<8) + (data[i+1] if i+1 < len(data) else 0)
        cs += word
        cs = (cs & 0xFFFF) + (cs >> 16)
    return ~cs&0xFFFF

def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(("127.0.0.1", 5000))
    print("Listening at 5000")

    msg, add = server.recvfrom(1024)
    print("received msg: ", msg.decode())
    crc = calc(msg)
    print("Checksum: ", hex(crc))

    data = (msg + b'|' + struct.pack("!H", crc))

    server.sendto(data, add)
    print("Data sent back")


if __name__ == "__main__":
    server()