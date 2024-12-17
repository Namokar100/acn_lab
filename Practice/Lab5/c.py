import socket
import pickle

class IPPacket:
    def __init__(self, id, offset, more_fragments, data):
        self.id, self.offset, self.more_fragments, self.data = id, offset, more_fragments, data

def fragment_and_send(packet, mtu, server_address):
    data_size = mtu - 20  # Header size is 20 bytes
    num_fragments = (len(packet) + data_size - 1) // data_size
    print(f"MTU: {mtu}\nNumber of fragments: {num_fragments}")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for i in range(num_fragments):
        fragment = IPPacket(1, i * data_size, i < num_fragments - 1, packet[i * data_size:(i + 1) * data_size])
        print(f"ID: {i}, Size: {len(fragment.data)}, Offset: {fragment.offset}, Flag (MF): {fragment.more_fragments}")
        try:
            client_socket.sendto(pickle.dumps(fragment), server_address)
        except Exception as e:
            print(f"Error: {e}")
    client_socket.close()

packet = b'A' * int(input("Enter the size of the data (in bytes): "))
print(packet)
mtu = int(input("Enter the MTU value: "))
fragment_and_send(packet, mtu, ('127.0.0.1', 8080))  # Directly call the function
