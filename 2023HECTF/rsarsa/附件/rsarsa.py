from functools import reduce
from Crypto.Util.number import *
import random
from secret import flag,hint

def generate_PQ(bits):
    x = getPrime(bits) >> bits//2 << bits//2
    while True:
        p = x + random.getrandbits(bits//2)
        if isPrime(p):
            break
    while True:
        q = x + random.getrandbits(bits//2)
        if isPrime(q):
            break
    return p,q

m = bytes_to_long(flag)
hint = bytes_to_long(hint)
e = 65537
p,q = generate_PQ(1024)
n = p*q
random.seed(seed)
x = [random.randint(1,seed) for _ in range(2)]
y = [random.randint(1,seed) for _ in range(2)]

print("c =",pow(hint,e,n))
print("n =",n)
print("c1 =",pow(reduce(lambda x, y: x * m + y, x), 17, n))
print("c2 =",pow(reduce(lambda x, y: x * m + y, y), 17, n))