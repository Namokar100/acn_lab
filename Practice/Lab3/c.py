import socket

def calc_crc(data: bytes, poly = 0x1021, i_crc = 0xFFFF):
    crc = i_crc

    for byte in data:
        crc ^= (byte<<8)
        
        for _ in range(8):
            crc = (crc<<1) ^ poly if crc&0x8000 else (crc<<1)
            crc &= 0xFFFF
    return crc

def client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 5000))
    print("Client connected")

    data = client.recv(1024)

    msg, r_crc = data[:-2], int.from_bytes(data[-2:], "big")
    print(f"Received msg: {msg.decode()}")
    binary = bin(r_crc)
    print(f"Received crc: {binary}")
    crc = calc_crc(msg)
    print(f"Calculated crc: {bin(crc)}")

    if crc == r_crc:
        print("Success")
    else:
        print("Failure")
    
    client.close()

if __name__ == "__main__":
    client()