import socket

def crc_calc(data: bytes, poly = 0x1021, i_crc = 0xFFFF):
    crc = i_crc

    for byte in data:
        crc ^= (byte<<8)
        for _ in range(8):
            crc = (crc << 1) ^ poly if crc&0x8000 else (crc<<1)
            crc &= 0xFFFF
    return crc

# def calc(data: bytes, poly = 0x1021, i_crc = 0xFFFF):
#     crc = i_crc
#     for byte in data:
#         crc ^= (byte << 8)
#         for _ in range(8):
#             crc = (crc << 1) ^ poly if crc & 0x8000 else crc<<1
#             crc &= 0xFFFF
#     return crc

def server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 5000))
    server.listen(1)
    print("Server listening at 5000")

    con, adr = server.accept()
    print(f"Client connected with {adr}")

    msg = input("Enter the message: ")
    e_msg = msg.encode()

    crc = crc_calc(e_msg)
    con.send(e_msg + crc.to_bytes(2, "big"))
    binary = bin(crc)
    print(f"Send {msg} with crc: {binary}")

    con.close()
    server.close()

if __name__ == "__main__":
    server()