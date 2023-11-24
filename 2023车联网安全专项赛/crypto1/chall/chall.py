from Crypto.Util.number import *
from Crypto.Random import *
from math import gcd
from flag import flag

gift = bytes_to_long(get_random_bytes(128))

e = 7
p = getStrongPrime(1024)
q = getStrongPrime(1024)

tmp = 0
while gcd(e, (p-1)*(q-1)) != 1:
    p = getStrongPrime(1024)
    q = getStrongPrime(1024)

N = p * q

print("N = "+str(N))
print("e = "+str(e))

ciphertext = []
ciphertext.append(pow(gift << 48, e, N))

for i in flag:
    ciphertext.append(pow(pow(i, e, N)+2023*(gift << 48), e, N))

print("ciphertext = "+ str(ciphertext))