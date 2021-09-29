import struct
from io import BytesIO


def pack_varint(number, max_bits=32):
    """
    Packs a varint.
    """

    number_min = -1 << (max_bits - 1)
    number_max = +1 << (max_bits - 1)
    if not (number_min <= number < number_max):
        raise ValueError("varint does not fit in range: %d <= %d < %d"
                         % (number_min, number, number_max))

    if number < 0:
        number += 1 << 32

    out = b""
    for i in range(10):
        b = number & 0x7F
        number >>= 7
        out += struct.pack("B", b | (0x80 if number > 0 else 0))
        if number == 0:
            break
    return out


def unpack_varint(data):
    """Read a varint from `stream`"""
    data = BytesIO(data)
    shift = 0
    result = 0
    while True:
        i = _read_one(data)
        result |= (i & 0x7f) << shift
        shift += 7
        if not (i & 0x80):
            break

    return result


def _read_one(data):
    """Read a byte from the file (as an integer)
    raises EOFError if the stream ends while reading bytes.
    """
    c = data.read(1)
    if c == b'':
        raise EOFError("Unexpected EOF while reading bytes")
    return ord(c)
