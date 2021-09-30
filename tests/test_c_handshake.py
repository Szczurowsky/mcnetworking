import unittest
from mcnetworking.packets.clientbound.handshake import Handshake


class TestClientHandshake(unittest.TestCase):
    def test_client_handshake(self):
        self.assertEqual(b'\x0f\x00/\tlocalhostc\xdd\x01', Handshake(47, "localhost", 25565, 1).get_raw())


if __name__ == '__main__':
    unittest.main()
