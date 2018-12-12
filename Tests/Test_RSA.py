import unittest
import RSA
import BlumBlumShub

def test_RSA(num_bit, message):
    print("\n------------------------------------------------------")
    # Generate random prime numbers
    p = BlumBlumShub.generate_prime(num_bit)  # 107 #999319777 #1500450271 #107
    q = BlumBlumShub.generate_prime(num_bit)  # 127 #999416681  #2860486313 #127

    # Test generate_keypair which returns public key is (e, n) and private key is (d, n)
    public, private = RSA.generate_keypair(p,q)

    print("\n------------------------------------------------------")
    encrypted_msg = RSA.encrypt(public, message)

    print("\n------------------------------------------------------")
    decrypted_message = RSA.decrypt(private, encrypted_msg)

    print("\n------------------------------------------------------")
    eve_decrypted_msg = RSA.factorization(public, encrypted_msg)

    return decrypted_message, eve_decrypted_msg

class TestRSA(unittest.TestCase):

    def test_decyption_RSA(self):
        # Test whether decrypted_msg and eve_decrypted_msg are matched with orginal message
        self.assertEqual((328492349280182901, 328492349280182901), test_RSA(16, "328492349280182901"))
        #self.assertEqual((3182049, 3182049), test_RSA(26, "3182049"))



if __name__ == '__main__':

    unittest.main()
