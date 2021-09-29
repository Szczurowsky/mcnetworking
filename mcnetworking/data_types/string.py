from .varint import pack_varint, unpack_varint


def pack_string(text):
    """
    Pack a varint-prefixed utf8 string.
    """

    text = text.encode("utf-8")
    return pack_varint(len(text)) + text


def unpack_string(data):
    """
    Unpack a varint-prefixed utf8 string.
    """

    length = unpack_varint(data)
    text = read_string(data, length)
    return text


def read_string(buffer, length):
    position = 1
    final = bytearray()
    i = 0
    while i < length:
        final.append(buffer[position + i])
        i += 1
    return final.decode("utf-8")
