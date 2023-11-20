# from sage.all import *
import os 
import random 
import string 
import hashlib 
from Crypto.Util.number import * 

DEBUG = True

banner = '|'*70 
flag = os.environ.get("FLAG", b"SYC{Al3XEI_FAKE_FLAG}").encode()
pbits = 120
abp = "abp" 


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

def check(a,b,p,turn,ans):
    if DEBUG:
        return True 
    try:
        if turn == "a":
            return int(a) == ans 
        if turn == "b":
            return int(b) == ans
        if turn == "p":
            return int(p) == ans  
    except Exception:
        exit()


try: 
    if not proof_of_work():
        exit() 
    print(banner) 
    print('\nHi Crypto-ers! AL3XEI here. I know you are excellent at math, so I prepared a game for u.') 
    print('In the equation y^2 = x^3+ a*x + b (mod p), 4 points are given. Plz give me the right a, b or p to contine the game.') 
    print('Good Luck!\n') 
    print(banner+'\n') 

    for i in range(10):
        turn = random.choice(abp) 
        p = getPrime(pbits) 
        a,b = [next_prime(random.randint(2,p)) for _ in "ab"] 
        curve = EllipticCurve(GF(p),[a,b]) 
        pts = [curve.random_point() for _ in range(4)]
        pts = [(_[0], _[1]) for _ in pts] 
        for _ in pts:
            print(_,end=" ") 
        print('\nGive me '+turn+" :") 
        ans = int(input('> ')) 
        if check(a,b,p,turn,ans):
            print("Good! Next challenge->\n") 
            print(banner+'\n')
            pbits+=5  
            continue 
        else:
            print("Something goes wrong...\n") 
            print(banner+'\n') 
            exit() 

    print('Congrats! Your flag is:',flag)

except Exception:
    print("Something goes wrong...\n") 
    print(banner+'\n') 
    exit() 