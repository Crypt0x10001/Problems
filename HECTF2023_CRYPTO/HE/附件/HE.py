from Crypto.Util.number import *
from random import randrange


def bin_expansion(c, p):
    row = c.nrows()
    col = c.ncols()
    log_p = row // col
    Ec = Matrix(ZZ, row, row)
    for i in range(row):
        for j in range(col):
            bits = bin(c[i, j] % p)[2:].rjust(log_p, '0')[::-1]
            for index in range(log_p):
                Ec[i, j * log_p + index] = int(bits[index])
    return Ec


def encryp(A,e,s,G,message,p):
    message = bin(message)[2:]
    Cipher = []
    for i in message:
        ci = block_matrix([A, A*s+e],ncols=2,subdivide=False)+ int(i) * G
        ci = bin_expansion(ci, p)
        Cipher.append(ci)
    return ' '.join([str(i.list()) for i in Cipher])


column = 7
prime = 4097
t = round(log(prime, 2))
m = t*column
G = Matrix(ZZ, t*column, column)
for i in range(t):
    for j in range(column):
        G[j*t+i, j] = 2 ** i
A = random_matrix(ZZ, m, column-1, x=0, y=prime)
e = random_matrix(ZZ, m, 1, x=0, y=prime//64)
s = random_matrix(ZZ, column-1, 1, x=prime//4, y=4*prime//3)
decrypt_key = Matrix(s.list() + [-1]).transpose()
encrypt_key = s

message = bytes_to_long(flag)
cipher = encryp(A,e,s,G,message,prime)
with open('cipher.txt', 'w') as f:
    f.write(cipher)
