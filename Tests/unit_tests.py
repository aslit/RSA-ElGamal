import unittest
import CommonFunctions
import BlumBlumShub
from MillerRabin import is_prime

class TestCommonFunctions(unittest.TestCase):

    def test_gcd(self):
        self.assertEqual(CommonFunctions.gcd(0, 0), 0)
        self.assertEqual(CommonFunctions.gcd(343, 1), 1)
        self.assertEqual(CommonFunctions.gcd(48, 54), 6)

        # Test two large primes
        self.assertEqual(CommonFunctions.gcd(999416681, 999319777), 1)

        # Test two integers m and n are relatively prime if and only if gcd(m,n) =1
        self.assertEqual(CommonFunctions.gcd(9, 8), 1)
        self.assertEqual(CommonFunctions.gcd(102313, 103927), 1)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # Test the Fast Exponentiation Algorithm  (x ^ e) % Y.
    def test_fast_exp(self):
        self.assertEqual(CommonFunctions.fast_exp(2, 100, 71), 20)
        self.assertEqual(CommonFunctions.fast_exp(54321, 3, 210757), 208718)
        self.assertEqual(CommonFunctions.fast_exp(2, 56, 1001), 438)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # Test the modular inverse with Extended Euclidian Algorithm
    def test_extended_euclidian(self):
        self.assertEqual(CommonFunctions.get_inverse_with_euclidean(513, 614), 231)
        self.assertEqual(CommonFunctions.get_inverse_with_euclidean(9, 11), 5)

    """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""
    # Test the factors of a number
    def test_factor(self):
        self.assertEqual(CommonFunctions.factor(35),  {5: 1, 7: 1})
        self.assertEqual(CommonFunctions.factor(736482378392),{73: 1, 2: 3, 523: 1, 659: 1, 3659: 1})

class TestMillerRabin(unittest.TestCase):

    # Test whether is a number is prime with Miller Rabin Test
    def test_miller_rabin(self):
        self.assertTrue(is_prime(BlumBlumShub.generate_prime(16)))
        self.assertTrue(is_prime(BlumBlumShub.generate_prime(32)))
        self.assertTrue(is_prime(4093082899))


if __name__ == '__main__':

    unittest.main()
