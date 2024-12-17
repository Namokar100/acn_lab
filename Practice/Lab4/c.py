import socket

def calc(data: bytes):
    cs = 0
    for i in range(0, len(data), 2):
        word = (data[i] << 8) + (data[i+1] if i+1 < len(data) else 0)
        cs += word
        cs = (cs & 0xFFFF) + (cs >> 16)
    return ~cs & 0xFFFF

# Create a socket and connect to the server
client = socket.socket()
client.connect(("127.0.0.1", 5000))
print("Connected to server")

# Take input from the user for the message
user_input = input("Enter the message to send: ")
msg = user_input.encode()  # Convert to bytes

# Calculate the checksum
cs = hex(calc(msg))

# Send the message and checksum to the server
client.send(msg + b'|' + cs.encode())
print("Message sent: ", msg)
print("Checksum: ", cs)

# Close the client connection
client.close()
