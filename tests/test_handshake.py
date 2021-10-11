import unittest
from mcnetworking.packets.clientbound.Handshake import Handshake


class TestHandshake(unittest.TestCase):
    def test_handshake(self):
        packet = Handshake()
        packet.write_packet(47, "127.0.0.1", 25565, 1)
        raw = packet.get_raw_bytes()
        packet.read_handshake(raw)
        self.assertEqual("127.0.0.1", packet.server_address)
        self.assertEqual(47, packet.protocol_version)
        self.assertEqual(25565, packet.server_port)
        self.assertEqual(1, packet.next_state)


if __name__ == '__main__':
    unittest.main()
