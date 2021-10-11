from mcnetworking.data_types.varint import pack_varint, unpack_varint
from mcnetworking.data_types.string import pack_string, unpack_string
from mcnetworking.data_types.unsigned import int_to_unsigned, unsigned_to_int
from mcnetworking.packets.utility import delete_from_buff


class Handshake:
    def __init__(self):
        self.packet_ID = b'\x00'
        self.protocol_version = None
        self.server_address = None
        self.server_port = None
        self.next_state = None
        self.raw_packet = None
        self.length = None

    def get_raw_bytes(self) -> bytes:
        if self.raw_packet is not None:
            return self.length + self.raw_packet
        raise Exception("Cannot get bytes from empty handshake")

    def write_packet(self, protocol_version, server_address, server_port, next_state):
        self.protocol_version = protocol_version
        self.server_address = server_address
        self.server_port = server_port
        self.next_state = next_state
        self.raw_packet = self.packet_ID + pack_varint(protocol_version) + pack_string(
            server_address) + int_to_unsigned(self.server_port) + pack_varint(self.next_state)
        self.length = pack_varint(len(self.raw_packet))

    def read_handshake(self, raw_bytes):
        if raw_bytes[1] != 0x00:
            raise Exception("Received bytes are not valid handshake packet")
        raw_bytes = bytearray(raw_bytes)

        # Length
        raw_bytes = delete_from_buff(raw_bytes, len(pack_varint(unpack_varint(raw_bytes))))

        # Packet ID
        raw_bytes = delete_from_buff(raw_bytes, len(pack_varint(unpack_varint(raw_bytes))))

        # Protocol version
        self.protocol_version = unpack_varint(raw_bytes)
        raw_bytes = delete_from_buff(raw_bytes, len(pack_varint(self.protocol_version)))

        # Server address
        self.server_address = unpack_string(raw_bytes)
        raw_bytes = delete_from_buff(raw_bytes, len(pack_string(self.server_address)))

        # Port
        self.server_port = unsigned_to_int(raw_bytes[0:2])
        raw_bytes = delete_from_buff(raw_bytes, 2)

        # Next state
        self.next_state = unpack_varint(raw_bytes)
