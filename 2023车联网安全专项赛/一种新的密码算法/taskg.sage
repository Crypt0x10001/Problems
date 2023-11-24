import flag
pk_mt = matrix(ZZ, 6, 6)

pk_mt[0] = [24, -246, 6, 2, -188, -7]
pk_mt[1] = [-28, -243, 6, -1, 2, -9]
pk_mt[2] = [-29, 251, -6, 0, -206, 14]
pk_mt[3] = [-101, 246, -6, -16, 575, 5]
pk_mt[4] = [2, 230, -7, -37, 206, 19]
pk_mt[5] = [425, -734, 30, 52, -3089, -8]

assert hadamard_ratio(pk_mt) < 0.1

plain = []
for i in flag:
    plain.append(ord(i))
    
def encrypt(m, pk):
    r = vector(ZZ, [-1, -0, 1, -1, 2, 3])
    return m * pk + r

def hadamard_ratio(mt):
    d = abs(mt.determinant())
    # print("d", d)
    if mt.rank() != mt.nrows():
        return 0
    dim = mt.rank()
    a = 1
    for i in mt:
        a *= i.norm()
    a = float(a)
    return (d/a)^(1/mt.rank())

i = 0
cipher = []

while i < len(plain):
    cipher.extend(encrypt(vector(ZZ, plain[i:i+6]), pk_mt))
    i += 6

print("cipher ",cipher)