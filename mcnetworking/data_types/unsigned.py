import struct


def int_to_unsigned(integer: int) -> bytes:
    return struct.pack(">H", integer)


def unsigned_to_int(byte_data: bytes) -> int:
    return struct.unpack(">H", byte_data)[0]
