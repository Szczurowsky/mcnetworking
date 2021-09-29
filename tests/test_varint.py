import unittest
from mcnetworking.data_types.varint import pack_varint, unpack_varint


class TestVarInt(unittest.TestCase):
    def test_varint(self):
        number = 2147483647
        varint = pack_varint(number)
        self.assertEqual(unpack_varint(varint), number)


if __name__ == '__main__':
    unittest.main()
