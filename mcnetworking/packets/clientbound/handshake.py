import struct
from data_types.varint import pack_varint
from data_types.string import pack_string


class Handshake:

    def __init__(self, protocol, address, port, next_state):
        self.id = b'\x00'
        self.protocol = protocol
        self.address = address
        self.port = port
        self.next_state = next_state

    def get_raw(self):
        packet = self.id + pack_varint(self.protocol) + pack_string(self.address) + struct.pack(">H", self.port) + \
                 pack_varint(self.next_state)
        return pack_varint(len(packet)) + packet
