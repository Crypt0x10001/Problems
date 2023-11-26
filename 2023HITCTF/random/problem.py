import random

with open('output.bin', 'wb') as f:
    f.write(random.randbytes(2500))

print('HITCTF2023{%s}' % random.randbytes(16).hex())