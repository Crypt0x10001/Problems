import os 
import random 
import string 
import hashlib 

flag = os.environ.get("FLAG", b"SYC{Al3XEI_FAKE_FLAG}")
DEBUG = False
banner = '|'*70
if DEBUG:
    print("==DEBUG MODE==") 

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

try:
    if not proof_of_work():
        exit() 
    print(banner) 
    parms = [random.getrandbits(32) for _ in range(128)] 
    res = res = int(input('Give me x calculating f(x) :\n> '))  
    if res >= 2**32:
        print("Give me something smaller.\n")  
        print(banner+'\n') 
        exit() 

    cnt = 0  
    for _ in range(128): 
        cnt += pow(res,_)*parms[_]  
    print(cnt) 
    ans = input('Give me Coefficients :\n> ') 
    ans = [int(_) for _ in ans.split(",")] 
    
    if ans == parms:
        print('Congrats! Your flag is:',flag)  
    else:
        exit()

except Exception:
    print("Something goes wrong...\n") 
    print(banner+'\n') 
    exit() 