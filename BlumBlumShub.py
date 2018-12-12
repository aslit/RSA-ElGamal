import MillerRabin
import random
from CommonFunctions import *

""" Generate random  number """
def generate_bbs(num_bit):

    bbs = BlumBlumShub(num_bit);
    list_sequence = bbs.generate_sequence()
    x = int("".join(map(str, list_sequence)), 2)

    return x

""" Generate random prime number """
def generate_prime(num_bit):

    x = generate_bbs(num_bit)
    while not MillerRabin.is_prime(x):
        x = generate_bbs(num_bit)
    return x

""" Generate random  number """
def generate_random_number(num_bit= None, start=1, stop=None):

    if num_bit == None:
        num_bit = random.randrange(start.bit_length()+1, stop.bit_length())

    x = generate_bbs(num_bit)
    while not x >= start and x <= stop:
        x = generate_bbs(num_bit)

    return x


class BlumBlumShub(object):

    """ Constructor """
    def __init__(self, numBits):
        self.numBits = int(numBits) # bits - Number of bits for number
        self.n = self.compute_n(int(numBits))
        self.seed = self.set_seed()

    """ Compute n = q * p"""
    def compute_n(self, numBits):
        return self.get_random_prime(numBits) * self.get_random_prime(numBits)

    """ Check to generates the appropriate primes (p = 3 mod 4) """
    def is_good_prime(self, p):
        return p % 4 == 3 and MillerRabin.is_prime(p)

    """ Choose randomly prime """
    def get_random_prime(self, numBits=32):
        prime = 1
        while not self.is_good_prime(prime):
            prime = random.getrandbits(int(numBits))
        return prime

    """ Sets the seed value. s0 , s1, s2 ...are integers from the range of 1 to n-1 relatively prime to n . """
    def set_seed(self):

        seed = 0
        while not gcd(seed, self.n) == 1 :
            # Choose s ∈ [1, n − 1], the random seed
            seed = random.randint(2, self.n - 1)

        list_seeds = range(self.n)
        # Compute s1 = s0^2 %n,  s2 = s1^2 %n,  ....
        for i in range(self.numBits):
            seed = fast_exp(seed, 2, self.n)
            yield seed

    """ Generate sequence of pseudo-random bits where  b0 = s0%2, b1 = s1%2, ...."""
    def generate_sequence(self):

        list_seeds = self.seed

        for s in list_seeds:
            yield s % 2

    def get_sequence(self):

        list_sequence = self.generate_sequence()
        for x in list_sequence:
            print("list_sequence:", x)


if __name__ == "__main__":

    prime_number = generate_prime(32)
    print("\n", prime_number.bit_length() , "bits prime number is generated : ",prime_number)


    number = generate_random_number( start = 1, stop = 24)
    print( "\n random number : ", number)

    number2 = generate_random_number(num_bit = 32)
    print("\n", prime_number.bit_length(), "bits number is generated : ", prime_number)

