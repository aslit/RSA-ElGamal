Final Project, MET CS 789 - Asli Terzioglu

RSA-ElGamal
================

RSA encryption is a python module use to

    a. Encrypt and send a message (Alice)
    b. Receive and encrypt a message (Bob)
    c. Eavesdrop and decrypt the message (Eve)

El Gamal encryption is a python module use to

    a. Encrypt and send a message (Alice)
    b. Receive and encrypt a message (Bob)
    c. Eavesdrop and decrypt the message (Eve)


Features
----------------

RSA.py

    RSA.pollard_method(n)                           # Factorization using pollard's p-1 method
    RSA.generate_keypair(p, q)                      # Generate public (e, n) and private key (d, n)
    RSA.encrypt(public_key, plaintext)              # Encrypt a given plaintext message with public key
    RSA.decrypt(private_key, ciphertext)            # Decrypt a ciphertext message with public key
    RSA.factorization(public_key, ciphertext)       # Use pollard n-1 function to decrypt the message

ElGamal.py

    ElGamal.generate_keypair(p)                     # Generate key pair and returns the public key ( g, p, h) and the private key (g, p, x)
    ElGamal.encrypt(public_key, plain_text)         # Encrypt a given plaintext message with public key
    ElGamal.decrypt(private_key, cipher_text)       # Decrypt the cipher message with private key
    ElGamal.finding_primitive_root(p)               # Find the one of the primitive root of p randomly
    ElGamal.bsgs(g, h, p)                           # Baby-step Giant-step Algorithm to compute Discrete Logs - Solve for x in h = g^x mod p given a prime p

MillerRabin.py

    MillerRabin.miller_rabin(n)                     # Miller-Rabin test to determine possible primality
    MillerRabin.is_prime(num)                       # Check whether is a number is prime with using miller_rabin() function

CommonFunctions.py
    
    CommonFunctions.factor(num)                     # Find the factors of a number
    CommonFunctions.gcd(x, y)                       # Find greatest common divisor(gcd) of x and y
    CommonFunctions.fast_exp(x, e, n)                # Implementation of The Fast Exponentiation Algorithm  (x ^ e) % Y mod n
    CommonFunctions.extended_euclidian(a, b)        # The equation for ax+by=gcd(a,b) has been returned where x and y are solved.
    CommonFunctions.get_inverse_with_euclidean(a,b) #Find the modular inverse with Extended Euclidian Algorithm'''

BlumBlumShub.py
    
    BlumBlumShub.generate_prime(num_bit)                                        # Generate random prime number
    BlumBlumShub.generate_random_number(num_bit= None, start=1, stop=None)      # Generate random number in range or according to bit number


How to run
--------------------

To run the algorithms :

    python RSA-ElGamal/main.py


Whenever you run the main, you can select which following algorithm to work with
    1 - RSA 
    2 - El Gamal

And then, you can select the following options 
    1 - Generate Key Pair
    2 - Encrypt a message
    3 - Decryption a cipher text
    4 - Eavesdrop and decrypt the message
    5 - Choose other encryption algorithm 

Note: Keys must be typed without brackets as input:
    Please enter the public key ( (g, p, h) for El-Gamal /(e,n) for RSA ): 20821325952358623, 321537506783761603


Unit Tests
----------------

To run the RSA tests:          
            
    python -m Tests.Test_RSA -v

To run the El Gamal  tests:                 

    python -m Tests.Test_ElGamal -v

To run all of other the unit tests:     

    python -m Tests.unit_tests -v


The '... ok' indicate a test that has passed. 

    test_extended_euclidian (__main__.TestCommonFunctions) ... ok
    test_factor (__main__.TestCommonFunctions) ... ok

If a test has failed, you should see output that looks similiar to:

    ERROR: test_decyption_ElGamal (__main__.TestElGamal)
    
    Traceback (most recent call last):
      File "/Users/asli/PycharmProjects/RSA-ElGamal/Tests/Test_ElGamal.py", line 28, in test_decyption_ElGamal
        self.assertEqual((328492349280182901, 328492349280182901), test_ElGamal(26, "328492349280182901"))
      File "/Users/asli/PycharmProjects/RSA-ElGamal/Tests/Test_ElGamal.py", line 11, in test_ElGamal
        public, private = ElGamal.generate_keypair(p)
    AttributeError: module 'ElGamal' has no attribute 'generate_keypair'

    ----------------------------------------------------------------------
    Ran 1 test in 0.006s
    
    FAILED (errors=1)

The output shows how it failed.

Contribute
------------------

- Source Code:https://github.com/aslit/RSA-ElGamal

Compatibility
------------------
Python 3.4.

