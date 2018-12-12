import sys
import math
from BlumBlumShub import *
from CommonFunctions import *
from MillerRabin import *

# !/usr/bin/env python


""" Generate public and private key for RSA"""
def generate_keypair(p, q):

    print("\nGenerating your public/private keypairs now for RSA Algorithm . . .")

    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')

    n = p * q

    # Compute phi is φ(n). p and q are prime, so φ(n)  of n is (p - 1) * (q - 1)
    phi = (p - 1) * (q - 1)

    # Choose an random integer e
    e = generate_random_number( start = 1, stop = phi)

    # Use Euclid's Algorithm to verify that e and φ(n) are relatively prime
    g = gcd(e, phi)
    while g != 1:
        e = generate_random_number( start = 1, stop = phi) #random.randrange(1, phi)  # If e and φ(n) are not relatively prime, choose another e
        g = gcd(e, phi)  # Use Euclid's Algorithm to verify that e and φ(n) are relatively prime again

    # Use Extended Euclid's Algorithm to generate the private key
    d = get_inverse_with_euclidean(e, phi)

    print("\nModulus of the group :", n, " Prime numbers :", p, ",", q)
    print("\nYour public key (e, n) is ", (e, n), " and your private key is (d, n) ", (d, n))

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


""" Encrypt a given plaintext message with public key """
def encrypt(public_key, message):

    print("\nEncrypting message with public key (e,n) ", public_key)

    # Unpack the key
    key, n = public_key

    # Create a bytearray from a string with utf-16 encoding.
    encoded_text = int(message).to_bytes((int(message).bit_length() + 7) // 8, byteorder=sys.byteorder)

    # List of cipher of the encryption of each integer in the encoded text.
    cipher_array = []

    # Encrypt until end of the encoded_text
    for i in encoded_text:
        # Compute i^key mod n with fast expo. algorithm
        cipher = fast_exp(i, key, n)
        # Add each cipher to cipher_array
        cipher_array.append(cipher)

    encrypted_text = ""
    for pair in cipher_array:
        encrypted_text += str(pair) + ' '

    print("\nThe encrypted message is: ", encrypted_text)

    # Return the cipher
    return encrypted_text


""" Decrypt a ciphertext message with public key """
def decrypt(private_key, ciphertext):

    print("\nDecrypting message with private key (d,n) ", private_key, " . . .")

    # Unpack the key into its components
    key, n = private_key

    # Decrpyts each pair and adds the decrypted integer to list of plaintext integers
    plain_array = []

    # Break cipher_text down into smaller chunks
    cipherArray = ciphertext.split()

    for i in range(0, len(cipherArray)):
        cipher = int(cipherArray[i])

        # Decrypted each message chunk and add it into plain_array
        message = fast_exp(cipher, key, n)
        plain_array.append((message))

    # Decodes integers to the original message bytes
    decrypted_text = int.from_bytes(plain_array, byteorder=sys.byteorder)

    # hex_str = ''.join(str(e) for e in plain_array)
    # decrypted_text = int.from_bytes(bytes.fromhex(hex_str), byteorder=sys.byteorder)

    print("\nThe message is:", decrypted_text)

    return decrypted_text


""" Factor using Pollard's p-1 method """
def pollard_method(n):

    # Choose a random b, which 1 < b < n-1
    b = generate_random_number( start = 1, stop = (n-1)) #random.randint(1, n - 1)

    # Calculate gcd(b,n)
    g = gcd(b, n)

    if g == n:              # If g = n, choose another b
        pollard_method(n)
    elif g in range(2, n):  # Else if 1 < g < n, a factor of n is found
        return g
    else:                   # Else g = 1
        p = 2
        while p <= b:

            # Compute log base p of n
            l = math.floor(math.log(n, p))
            b = fast_exp(b, fast_exp(p, l, n), n)
            g = gcd(b - 1, n)

            if g == n:                  # If g = n, choose another b
                pollard_method(n)
            elif g in range(2, n - 1):  # Else if 1 < g < n, a factor of n is found
                return g
            p = p + 1                   # Else if g = 1, repeat same steps with different p

        return None


'''Use pollard n-1 factorization algorithm to decrypt the message '''
def factorization(public_key, ciphertext):

    print("\nEve decrypt the message with factorization  . . .")

    # Unpack the key
    e, n = public_key

    # Use pollard_method() for finding factor of n
    first_factor = pollard_method(n)
    second_factor = (n // pollard_method(n))

    # Find phi with factors
    phi = (first_factor - 1) * (second_factor - 1)

    # Calculate d with extended euclid algorithm, it is the inverse of e
    d = get_inverse_with_euclidean(e, phi)

    # Decrypt with private key
    return decrypt((int(d), n), ciphertext)


if __name__ == '__main__':

    # Use Blum Blum Shub algorithm to generate random prime number
    p = generate_prime(32)
    q = generate_prime(32)

    print("\n------------------------------------------------------")
    public, private = generate_keypair(p, q)

    #public, private =(155163283893911887, 321537506783761603), (20821325952358623, 321537506783761603)
    #public = (1691893746218639,7241764034427121)
    #encrypted_msg =  ""

    message = "11122018111223212983920183018"
    print("\n------------------------------------------------------")
    encrypted_msg = encrypt(public, message)
    print("\n------------------------------------------------------")
    decrypt(private, encrypted_msg)
    print("\n------------------------------------------------------")
    factorization(public, encrypted_msg)

    """
    
    
       # Public key is (e, n) and private key is (d, n)
    
    """