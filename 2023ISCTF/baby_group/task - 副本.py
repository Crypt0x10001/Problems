from Per import P,Block
from secret import flag
import hashlib
from libnum import s2n

mask = P(256)

print(mask**2)
mask_hash = hashlib.sha512(str(mask).encode()).hexdigest()
print("the mask hash is:" + mask_hash)

mul = P(256)
print(f"{mul=}")
temp = hashlib.sha512(str(mask * mul).encode()).hexdigest()

msg = s2n(flag) ^ int(temp,16)

worker = Block()
print(f"pubkey(q,h):{worker.getPublicKey()}")
c = worker.enc(msg)
print(f"{c=}")
dec = worker.dec(c)

