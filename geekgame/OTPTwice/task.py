from pwn import xor 
from os import urandom 
flag = b"SYC{Al3XEI_FAKE_FLAG}" 

# step0: key generation & distribution
def s0(msg): 
    k1,k2 = [urandom(len(msg)) for _ in "__"] 
    return k1,k2 

#  

# step1: Alice encrypt M, and send it to Bob
def s1(msg,k1):
    c1 = xor(msg,k1)
    return c1 

# step2: Bob encrypt c1, and send it to Alice 
def s2(msg,k2):
    c2 = xor(msg,k2) 
    return c2 

# step3: Alice decrypt c2, and send it to Bob.
def s3(msg,k1):
    c3 = xor(msg,k1)
    return c3 

# step4: Bob decrypt c3, get M.
def s4(msg,k2):
    m_ = xor(msg,k2) 
    return m_ 


def encrypt(msg,k1,k2): 
    c1 = s1(msg,k1) 
    c2 = s2(c1,k2) 
    c3 = s3(c2,k1)
    m_ = s4(c3,k2) 
    assert msg == m_

# Here's what hacker Eve got:
def encrypt_(msg,k1,k2):
    c1 = s1(msg,k1) 
    c2 = s2(c1,k2) 
    c3 = s3(c2,k1)
    m_ = s4(c3,k2) 
    if HACK == True:
        print(c1) 
        print(c2) 
        print(c3) 


k1,k2 = s0(flag) 
encrypt_(flag,k1,k2) 

'''
b'\xdbi\xab\x8d\xfb0\xd3\xfe!\xf8Xpy\x80w\x8c\x87\xb9'
b'o\xb0%\xfb\xdb\x0e\r\x04\xde\xd1\x9a\x08w\xda4\x0f\x0cR'
b'\xe7\x80\xcd\ria\xb2\xca\x89\x1a\x9d;|#3\xf7\xbb\x96'
'''