from Crypto.Util.number import *
import random
from secret import flag

def convert(m):
    m = m ^ m >> 13
    m = m ^ m << 9 & 2029229568
    m = m ^ m << 17 & 2245263360
    m = m ^ m >> 19
    return m


def circular_shift_left(int_value, k, bit=32):
    bin_value = bin(int_value)[2:].zfill(32)
    bin_value = bin_value[k:] + bin_value[:k]
    int_value = int(bin_value, 2)
    return int_value


def enc_block(block):
    block ^= a
    block = circular_shift_left(block, 11)
    block ^= b
    return block


def my_encblock(message):
    assert len(message) % 4 == 0
    new_message = b''
    IV = bytes_to_long(b'retu')
    for i in range(len(message) // 4):
        block = message[i * 4: i * 4 + 4]
        block = bytes_to_long(block)
        block = convert(block)
        block = enc_block(block) ^ IV
        IV = block
        block = long_to_bytes(block, 4)
        new_message += block
    return new_message


a = random.getrandbits(32)
b = random.getrandbits(32)
m = my_encblock(flag)
print('a =', a)
print('b =', b)
print('m =', m)
'''
a = 1909693462
b = 3279553481
m = b'\xa1\x14\xa66\x9c\x88\xe3\xeco?\xe2\x95\xbd\xcd\x1a2)i\xf5_)\x15H\xf2y\xec\x8d\xfc*KU\xefv\xdd\xd0X'
'''