from collections import defaultdict

''' Find greatest common divisor(gcd) of x and y '''
def gcd(x, y):

    while (y):
        x, y = y, x % y

    return x


''' Implementation of The Fast Exponentiation Algorithm  (x ^ e) % Y mod n '''
def fast_exp(x, e, n):

   y = 1
   while e != 0:  # iterate until e is not 0
       if not e % 2 == 0:  # If e is odd
           e = (e - 1)
           y = (y * x) % n
       else : # If e is  even
           x = (x * x) % n
           e = e // 2

   return y


''' Find the modular inverse with Extended Euclidian Algorithm'''
def get_inverse_with_euclidean(a, b):

    gcd, x, y = extended_euclidean(a,b)
    if x<0:
        return b+x
    else :
        return x


''' The equation for ax+by=gcd(a,b) has been returned where x and y are solved. '''
def extended_euclidean(a, b):

    if a != 0:
        gcd, x, y = extended_euclidean(b % a, a)
        return (gcd, y - (b // a) * x, x)

    return (b, 0, 1)


''' Find the factors of a number  '''
def factor(num):

    factors = defaultdict(lambda: 0)
    n = 2
    while num != 1:
        while num % n == 0:
            factors[n] += 1
            num /= n
        n += 1

    return dict(factors)


""" 
print ("gcd: ", gcd(614, 513))

#  (x ^ e) % Y mod n
print ("fast exp: ",fast_exp(2, 1000, 11))

print ("get_inverse_with_euclidean: ",get_inverse_with_euclidean(5, 7))

# ax+by=gcd(a,b)
print ("extended_euclidean: ", extended_euclidean(513, 614))

print ("factor: ", factor(2057))


"""