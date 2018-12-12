import ElGamal
import RSA
import BlumBlumShub

#!/usr/bin/env python

if __name__ == '__main__':

    # Set our game ending flag to False
    running = True
    while running:
        in_algorithm = True

        print("\nEncrypter/ Decrypter")
        print("================================================")

        print("1. RSA Encryption\n2. El-Gamal Encryption\n3. Exit ")

        # Pick a number for encryption algorithm
        type_encryption = input("\nPlease Enter a number to choose encryption algorithm: ")

        if type_encryption == "1" or type_encryption == "2":
            # Loop until the user exit from algorithm
            while in_algorithm:
                print("\n------------------------------------------------------")
                print("\n1 - Generate Key Pair\n2 - Encrypt a message\n3 - Decryption a cipher text\n4 - Eavesdrop and decrypt the message\n5 - Choose other encryption algorithm ")

                # Get a number for user-requested function from user
                function = input("\nPlease enter a number: ")

                # Choose function 1 - Generate Key Pair
                if function == "1":

                    # Get the number of bit from user
                    num_bit = input("Please enter the number of bit for generating keys: ")

                    print("\n------------------------------------------------------")

                    # If encryption algorithm is RSA
                    if type_encryption == "1" :

                        # Use Blum Blum Shub algorithm to generate random prime numbers
                        p = BlumBlumShub.generate_prime(num_bit)
                        q = BlumBlumShub.generate_prime(num_bit)

                        RSA.generate_keypair(p,q)

                    # If encryption algorithm is El-Gamal
                    elif type_encryption == "2" :

                        # Use Blum Blum Shub algorithm to generate random prime number
                        p = BlumBlumShub.generate_prime(num_bit)  # 127 #999416681 #2860486313 #127

                        public, private = ElGamal.generate_keypair(p)

                # Otherwise, function 2 - Encrypt a message
                elif function == "2":

                    # Get the message from user
                    message = input("Please enter your message : ")

                    # Get the public key from user
                    public = input("Please enter the public key ( (g, p, h) for El-Gamal /(e,n) for RSA ): ")

                    print("\n------------------------------------------------------")

                    # If encryption algorithm is RSA
                    if type_encryption == "1":
                        print(" public :",public)
                        result = [int(x.strip()) for x in public.split(',')]
                        print(" result :", result)
                        public_key =(result[0]),(result[1])

                        # Encrypt with RSA Algorithm
                        RSA.encrypt(public_key, message)

                    # If encryption algorithm is El-Gamal
                    elif type_encryption == "2":

                        result = [int(x.strip()) for x in public.split(',')]

                        # Encrypt with El-Gamal Algorithm
                        ElGamal.encrypt((result[0],result[1],result[2]), message)

                # Otherwise, function 3 - Decrypt a message
                elif function == "3":

                    # Get the encrypted message from user
                    encrypted_msg = input("Please enter encrypted message : ")

                    # Get the private key from user
                    private = input("Please enter the private key ((g, p, x) for El-Gamal / (d,n) for RSA ): ")

                    print("\n------------------------------------------------------")

                    # If encryption algorithm is RSA
                    if type_encryption == "1":

                        result = [int(x.strip()) for x in private.split(',')]
                        private_key = (result[0],result[1])
                        # Decrypt with RSA Algorithm
                        RSA.decrypt(private_key, encrypted_msg)

                    # If encryption algorithm is El-Gamal
                    elif type_encryption == "2":

                        result = [int(x.strip()) for x in private.split(',')]

                        # Decrypt with El-Gamal Algorithm
                        ElGamal.decrypt((result[0],result[1],result[2]), encrypted_msg)

                # Otherwise, function 4 - Eavesdrop and decrypt the message
                elif function == "4":

                    # Get the encrypted message from user
                    encrypted_msg = input("Please enter encrypted message : ")

                    # Get the public key from user
                    public = input("Please enter the public key ((g, p, h) for El-Gamal / (e,n) for RSA ): ")

                    print("\n------------------------------------------------------")

                    # If encryption algorithm is RSA
                    if type_encryption == "1":

                        result = [int(x.strip()) for x in public.split(',')]
                        public_key = (result[0],result[1])
                        # Eavesdrop with factorization and decrypt the message with RSA Algorithm
                        RSA.factorization(public_key, encrypted_msg)

                    # If encryption algorithm is El-Gamal
                    elif type_encryption == "2":

                        result = [int(x.strip()) for x in public.split(',')]

                        # Eavesdrop with baby-step giant-step and decrypt the message with El-Gamal Algorithm
                        ElGamal.eve((result[0],result[1],result[2]), encrypted_msg)

                # Otherwise, function 5 - Choose other encryption algorithm
                elif function == "5":
                    break

                # Otherwise,  nope
                else:
                    print()
                    print("Oh, that's not proper choose...")
        elif type_encryption == "3":
            running = False
        # Otherwise,  nope
        else:
            print()
            print("Oh, that's not proper choose...")




