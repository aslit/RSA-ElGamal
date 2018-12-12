import random
from CommonFunctions import *

''' Miller-Rabin test to determine possible primality '''
def miller_rabin(n):

    # Pick a random b in 1 < b < n - 1
    b = random.randint(1, n - 1)

    # Find m which when n-1 = 2^r * m where m is odd
    m = n - 1
    r = 0
    while m % 2 == 0:
        m = m / 2
        r = r + 1
    # Compute x = b ^ m mod n
    x = fast_exp(b, m, n)

    if  x == 1 or  x == n - 1:                      # If x = 1 or  x = -1 then n is a Miller Rabin pseudoprime
        return True
    elif x != n - 1 :                               # Else x != -1
        if fast_exp(fast_exp(b, m, n),2, n) == n-1:                             # If (b^m)^2 = -1 mod n then n is a Miller Rabin pseudoprime
            return True
        elif fast_exp (fast_exp (fast_exp(b, m, n), 2, n), (r-1), n ) == n-1:    # If ((b^m)^2)^(r-1) = -1 mod n then n is a Miller Rabin pseudoprime
            return True
    # Otherwise, n is composite number
    return False


''' Check whether is a number is prime '''
def is_prime(num):

    # Check the number is not smaller than 2, it is not prime
    if (num < 2):
        return False
    # If number is even, it is not prime
    elif (num % 2 == 0) :
        return False

    return miller_rabin(num)



#("is_prime:",is_prime(4093082899))

