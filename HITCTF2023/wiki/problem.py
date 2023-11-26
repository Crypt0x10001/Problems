import requests as rq
from bs4 import BeautifulSoup
from Crypto.Cipher import AES
from secret import key, nonce, flag

def encrypt(m):
    return AES.new(key, mode=AES.MODE_CTR, nonce=nonce).encrypt(m.encode())

def get_wiki():
    r = rq.get('https://en.wikipedia.org/wiki/Special:Random')
    soup = BeautifulSoup(r.text, 'html.parser')
    text = ''.join(x.getText() for x in soup.select('#mw-content-text p'))
    return text

for x in range(100):
    with open(f'wiki/{x}.bin', 'wb') as f:
        f.write(encrypt(get_wiki()))

print(encrypt(flag))
# b'\x92\xc2\xbe\xf0ia\xb8\xe6$\xf3\x85\x9e\xc9\x1bq\xfe\xdc\xc0\xfb@AB/\x15\xee\x15\xf5\x0b\t\xf3_\x8b\xe5Vi\n\xad'
