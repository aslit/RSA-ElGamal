import sys
from math import ceil, sqrt
from BlumBlumShub import *
from CommonFunctions import *
from MillerRabin import *

""" Baby-step Giant-step Algorithm to compute Discrete Logs - Solve for x in h = g^x mod p given a prime p."""
def bsgs(g, h, p):

   if not (is_prime(p)):
       raise ValueError('Number must be prime.')

   m = ceil(sqrt(p - 1)) # phi(p) is p-1 if p is prime

   # Baby step - Compute hashmap which store g^{1...m} (mod p).
   pairs = {}
   for i in range(m):
       pairs[ fast_exp(g, i, p) ] = i

   # Compute inverse of m
   inverse_m = get_inverse_with_euclidean(g,p)

   c = fast_exp(inverse_m, m , p)

   # Giant step - Search for an equivalence in the table.
   for j in range(m-1):
       y = (h * fast_exp(c, j,p)) % p
       if y in sorted(pairs):
           return j * m + pairs[y]

   # Solution not found
   return None


"""  Find primitive roots """
def finding_primitive_root (p):

   if not (is_prime(p)):
       raise ValueError('Number must be prime.')

   random_number = generate_random_number( start = 2, stop = (p-1))

   # Find factors of φ(n) = p-1
   factors = factor(p - 1)

    # Test the powers instead of testing all of them)
   for x, y in factors.items():

       # Compute random_number ^ ((p - 1) / x) % p
       result = fast_exp(random_number, ((p - 1) / x), p)

       # If it equals 1, reject and select another random number
       if result == 1:
           return finding_primitive_root(p)

   return random_number


""" Generate public and private key """
def generate_keypair(p):

    print("\nGenerating your public/private keypairs  . . .")

    if not (is_prime(p)):
       raise ValueError('Number must be prime.')

    # Choose an generator as g
    g = finding_primitive_root(p)

    # Choose random secret x in the group p
    x = generate_random_number( start = 1, stop = (p-1))

    # Computes h = g^x (mod p)
    h = fast_exp(g, x, p)

    print("\nModulus of the group :", p, "   Prime number :", p, "   Primitive root :", g)

    print("\nYour public key is (g, p, h) : ", (g, p, h), "and your private key is (g, p, x) : ", (g, p, x))

    # Returns the public key ( g, p, h) and the private key (g, p, x).
    return (( g, p, h), (g, p, x))


""" Encrypt a given plaintext message with public key """
def encrypt(public_key, message):

    print("\nEncrypting message with public key  (g, p, h) ",public_key)

    # Unpack the public key
    g, p, h = public_key

    # Encode the message
    encoded_text = int(message).to_bytes((int(message).bit_length() + 7) // 8, byteorder=sys.byteorder)

    # List of pairs (c1, c2) maintains the encryption of each integer in the encoded text.
    cipher_pair = []

    # Encrypt until end of the encoded_text
    for i in encoded_text:
       # Choose random secret y in the group
       y = generate_random_number( start = 1, stop = (p-1))

       # Compute (c1, c2) = (g^y(mod p), m*h^y(mod p)).
       c1 = fast_exp(g, y, p)
       c2 = (i * fast_exp(h, y, p)) % p

       # Add the pair to the cipher pairs list
       cipher_pair.append([c1, c2])

    encrypted_str = ""
    for pair in cipher_pair:
       encrypted_str += str(pair[0]) + ' ' + str(pair[1]) + ' '

    print("\nThe encrypted message is: ", encrypted_str)

    # Return the cipher pairs list (c1, c2)
    return encrypted_str

""" Decrypt the cipher message with private key """
def decrypt(private_key, cipher_text):

   print("\nDecrypting message with private key  (g, p, x) ", private_key)

   # Unpack the private key
   g, p, x = private_key

   # List of plaintext integers for adding decrypted each pair
   plain_array = []

   # Break cipher_text down into smaller chunks
   cipher_array = cipher_text.split()

   # If length of cipher_array is not even, it means cipher test is altered, because ciphertext has formed in pairs[c1, c2]
   if (not len(cipher_array) % 2 == 0):
      return "Improper Cipher Text"

   for i in range(0, len(cipher_array), 2):

       # Unpack the pair
       c1 = int(cipher_array[i])
       c2 = int(cipher_array[i + 1])

       # Compute s1 with fast exponentiation algorithm (c1 ^ x) % p. s1 is the secret which share with both side but no one else knows.
       s1 = fast_exp(c1, x, p)

       if gcd(s1, p)== 1:
           # Compute s2 which is the inverse of s1.
           # s2 = g^(-xy)(mod p)
           # p is a prime, so phi(p) is (p-1).
           s2 = fast_exp(s1, (p-1)-1 , p)

           # Decrypted each message chunk and add it into plain_array
           plain_text = (c2 * s2) % p
           plain_array.append(plain_text)

   # Convert bytearray back into a string.
   decrypted_text = int.from_bytes(plain_array, byteorder=sys.byteorder)

   print("\nThe message is:", decrypted_text)

   return decrypted_text

""" Eve make search for the discrete log and decrypt the message with baby-step giant-step algorithm """
def eve(public_key, encrypted_msg):

    print("\nEve decrypt the message with baby-step giant-step algorithm   . . .")

    # Unpack the key
    g, p, h = public_key

    # Apply Baby step Giant step Algorithm to break the El Gamal cipher
    x = bsgs(g, h, p)

    decrypted_msg = decrypt((g, p, x), encrypted_msg )

    return decrypted_msg


if __name__ == '__main__':

   print ("El Gamal Encrypter/ Decrypter")

   # Use Blum Blum Shub algorithm to generate random number
   p = generate_prime(30)

   print("\n------------------------------------------------------")
   public, private = generate_keypair(p)

   # public, private =( , , ), ( , , )
   # public = ( , , )
   # encrypted_msg =

   message = "2323914489138290840923"
   print("\n------------------------------------------------------")
   encrypted_msg = encrypt(public, message)

   print("\n------------------------------------------------------")
   decrypted_msg = decrypt(private, encrypted_msg )

   print("\n------------------------------------------------------")
   eve_decrypted_msg = eve(public, encrypted_msg)

   """
   
   
   Returns the public key ( g, p, h) and the private key (g, p, x).
   
   """

