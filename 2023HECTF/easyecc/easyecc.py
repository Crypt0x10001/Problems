from Crypto.Util.number import *
from Crypto.PublicKey import ECC
from fastecdsa import curve
from sympy import *
me = bytes_to_long(flag)

key = ECC.generate(curve='NIST P-256')
f = open('pem.txt', 'w').write(key.export_key(format='PEM'))
G = key.public_key()
k = key.d
n = G.order()
p = curve.P256.p
r = randprime(1, n-1)

M = E.random_point()
# M = (mx, my)
e = nextprime(my-mx)
N = n * p
c = pow(me, e, int(N))
print('c =', c)

K = k*G
c1 = M+r*K
c2 = r*G
print(c1)
print(c2)

# c = 340411986008332622492252515156919590702658555525072399052451683041772652474839788525448087771416400264570261404595656046016551644464496921197111421138765
# c1 = (71430232672331113271988412132459391678542075997754159037222774180961171917977 : 62238630405406252154015032808640586594811636815028129383858020738965206372881 : 1)
# c2 = (25742109236464952840117078659367834030129507446418393682693133323915430074859 : 65657711071079869088595294059522027768683424454908946840021611773238453793364 : 1)
