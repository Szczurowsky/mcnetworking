def delete_from_buff(raw_bytes, length) -> bytearray:
    i = 0
    while i != length:
        del raw_bytes[0]
        i += 1
    return raw_bytes