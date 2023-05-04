# RSA Algorithm Implementation

import random
import sympy

small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                31, 37, 41, 43, 47, 53, 59, 61, 67,
                71, 73, 79, 83, 89, 97, 101, 103,
                107, 109, 113, 127, 131, 137, 139,
                149, 151, 157, 163, 167, 173, 179,
                181, 191, 193, 197, 199, 211, 223,
                227, 229, 233, 239, 241, 251, 257,
                263, 269, 271, 277, 281, 283, 293,
                307, 311, 313, 317, 331, 337, 347, 349]

def gcd(x,y):
    if (y==0):
        return x
    else:
        return gcd(y,x%y)

def inverse(num,mod):
    m = mod
    y = 0
    x = 1

    while (num>1):
        q = num//mod
        t = mod
        mod  = num%mod
        num = t
        t = y

        y = x - q * y
        x = t
    if (x<0):
        x += m

    return x

def generate(n):
    while True:
        pn = random.randrange(2**(n-1), (2**n) -1)
        for i in small_primes:
            if (pn % i == 0):
                break
        else:
            return pn

def trialComposite(round_tester, ec, mrc, maxDivisionsByTwo):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                return False
        return True

def isMillerRabinPassed(mrc):
    maxDivisionsByTwo = 0
    ec = mrc-1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * ec == mrc-1)
    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, mrc)
        if trialComposite(round_tester,ec,mrc,maxDivisionsByTwo):
            return False
    return True

def primeGen(n):
    if (n<=16):
        ls = list(sympy.primerange(2**(n-1),2**n))
        rd = random.randint(0,len(ls)-1)
        return ls[rd]
    else:
        while True:
            pbl = generate(n)
            if isMillerRabinPassed(pbl):
                return pbl

def power(x, y, p):
    res = 1 
    x = x % p
 
    while (y > 0):
        
        if (y & 1):
            res = (res * x) % p

        y = y >> 1
        x = (x * x) % p
         
    return res
