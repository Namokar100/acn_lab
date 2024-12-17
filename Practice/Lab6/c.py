import socket
import struct

def calc(data: bytes):
    cs = 0
    for i in range(0, len(data), 2):
        word = (data[i]<<8) + (data[i+1] if i+1 < len(data) else 0)
        cs += word
        cs = (cs & 0xFFFF) + (cs >> 16)
    return ~cs&0xFFFF

def client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip = input("Enter the msg: ")
    msg = ip.encode()

    crc = calc(msg)

    print("Message: ", ip)
    print("CS: ", hex(crc))

    client.sendto(msg, ("127.0.0.1", 5000))

    client.settimeout(5)

    try:
        data, msg = client.recvfrom(1024)

        msg, rcs = data.rsplit(b'|', 1)
        rcs = struct.unpack("!H", rcs)[0]

        print("Received msg: ", msg)
        print("Received CS: ", hex(rcs))

        if crc == rcs:
            print("Success")
        else:
            print("Failure")

    finally:
        client.close()

if __name__ == "__main__":
    client()