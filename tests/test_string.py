import unittest
from mcnetworking.data_types.string import unpack_string, pack_string


class TestString(unittest.TestCase):
    def test_string(self):
        string = "TeSt StRiNg3#"
        encoded_sting = pack_string(string)
        self.assertEqual(unpack_string(encoded_sting), string)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
