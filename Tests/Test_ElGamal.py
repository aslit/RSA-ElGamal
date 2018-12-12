import unittest
import ElGamal
import BlumBlumShub
import sys

def test_ElGamal(num_bit, message):
    print("\n------------------------------------------------------")
    # Generate random prime numbers
    p = BlumBlumShub.generate_prime(num_bit)

    # Test generate_keypair which returns public key ( g, p, h) and the private key (g, p, x)
    public, private = ElGamal.generate_keypair(p)

    print("\n------------------------------------------------------")
    encrypted_msg = ElGamal.encrypt(public, message)

    print("\n------------------------------------------------------")
    decrypted_msg = ElGamal.decrypt(private, encrypted_msg)

    print("\n------------------------------------------------------")
    eve_decrypted_msg = ElGamal.eve(public, encrypted_msg)

    return decrypted_msg, eve_decrypted_msg

class TestElGamal(unittest.TestCase):

    def test_decyption_ElGamal(self):
        # Test whether decrypted_msg and eve_decrypted_msg are matched with orginal message
        self.assertEqual((328492349280182901, 328492349280182901), test_ElGamal(26, "328492349280182901"))
        #self.assertEqual((3182049, 3182049), test_ElGamal(16, "3182049"))


if __name__ == '__main__':

    unittest.main()
