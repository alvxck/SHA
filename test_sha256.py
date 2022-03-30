import unittest
from sha256 import SHA256

class TestSHA256(unittest.TestCase):
    def test_hash(self):
        test = SHA256('hello world')
        self.assertEqual(test.hash(), [['01101000011001010110110001101100', '01101111001000000111011101101111', '01110010011011000110010010000000', '00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000000000000', '00000000000000000000000001011000', '00110111010001110000001000110111', '10000110110100001100000000110001', '11010011101111010001000100001011', '01111000001111110100011110000010', '00101010100100000111110011101101', '01001011001011110111110011001001', '00110001111000011001010001011101', '10001001001101100100100101100100', '01111111011110100000011011011010', '11000001011110011010100100111010', '10111011111010001111011001010101', '00001100000110101110001111100110', '10110000111111100000110101111101', '01011111011011100101010110010011', '00000000100010011001101101010010', '00000111111100011100101010010100', '00111011010111111110010111010110', '01101000011001010110001011100110', '11001000010011100000101010011110', '00000110101011111001101100100101', '10010010111011110110010011010111', '01100011111110010101111001011010', '11100011000101100110011111010111', '10000100001110111101111000010110', '11101110111011001010100001011011', '10100000010011111111001000100001', '11111001000110001010110110111000', '00010100101010001001001000011001', '00010000100001000101001100011101', '01100000100100111110000011001101', '10000011000000110101111111101001', '11010101101011100111100100111000', '00111001001111110000010110101101', '11111011010010110001101111101111', '11101011011101011111111100101001', '01101010001101101001010100110100', '00100010111111001001110011011000', '10101001011101000000110100101011', '01100000110011110011100010000101', '11000100101011001001100000111010', '00010001010000101111110110101101', '10110000101100000001110111011001', '10011000111100001100001101101111', '01110010000101111011100000011110', '10100010110101000110011110011010', '00000001000011111001100101111011', '11111100000101110100111100001010', '11000010110000101110101100010110']])

if __name__ == '__main__':
    unittest.main()