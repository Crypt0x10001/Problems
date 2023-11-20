from Crypto.Cipher import DES3
from Crypto.Util.number import *
import os
import random
import string
import hashlib

xor = lambda a,b: bytes([a[i % len(a)] ^ b[i % len(b)] for i in range(max(len(a), len(b)))])
pad = lambda msg,padlen: msg+chr((padlen-(len(msg)%padlen))).encode()*(padlen-(len(msg)%padlen))

flag = os.environ.get("FLAG", "SYC{Al3XEI_FAKE_FLAG}").encode()
sec = os.urandom(8)

banner = '|'*70

DEBUG = False 
def proof_of_work():
    if DEBUG:
        return True
    proof = ''.join([random.choice(string.ascii_letters+string.digits) for _ in range(20)])
    digest = hashlib.sha256(proof.encode()).hexdigest()
    print("sha256(XXXX+%s) == %s" % (proof[4:], digest))
    x = input("Give me XXXX: ")
    if len(x)!=4 or hashlib.sha256((x+proof[4:]).encode()).hexdigest() != digest:
        return False
    print("Right!")
    return True



def enc(msg,key):
    try:
        key = long_to_bytes(key)
        msg = xor(long_to_bytes(msg),sec)
        des = DES3.new(key,DES3.MODE_ECB)
        ct = xor(des.encrypt(pad(msg,8)),sec)
        return bytes_to_long(ct)
    except Exception as e:
        print(e)
        return Exception

def service():
    cnt = 0
    if not proof_of_work():
        exit()
    print(banner)
    print('Simple DES Encryption Service')
    print(banner)
    while cnt<2:
        print('1. Encrypt\n2. Get encrypted flag.')
        choice = int(input('> '))
        if choice == 1:
            print('Input msg:')
            msg = int(input('> ').strip())
            print('Input key:')
            key = int(input('> ').strip())
            print(enc(msg,key))
        elif choice == 2:
            print('Input key:')
            key = int(input('> ').strip())
            print(enc(bytes_to_long(flag),key))
        else:
            exit()
        cnt+=1
    print(banner)
    print('Bye!')
    exit()

try:
    service()
except Exception:
    print("Something goes wrong...\n")
    print(banner+'\n')
    exit()
