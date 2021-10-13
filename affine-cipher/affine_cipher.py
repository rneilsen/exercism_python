from string import ascii_lowercase as ALPHABET
from math import gcd

M = len(ALPHABET)
NUMALPH = {n: ALPHABET[n] for n in range(M)}
ALPHNUM = {ALPHABET[n]: n for n in range(M)}

def encode(plain_text, a, b):
    if gcd(a, M) != 1:
        raise ValueError("a must be coprime to m")


def decode(ciphered_text, a, b):
    if gcd(a, M) != 1:
        raise ValueError("a must be coprime to m")
