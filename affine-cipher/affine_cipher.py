from string import ascii_lowercase as ALPHABET
from math import gcd

M = len(ALPHABET)
NUMALPH = {n: ALPHABET[n] for n in range(M)}
ALPHNUM = {ALPHABET[n]: n for n in range(M)}

def encode(plain_text, a, b):
    if gcd(a, M) != 1:
        raise ValueError("a must be coprime to m")
    
    cipher_text = ""
    for ch in plain_text.lower():
        if ch not in ALPHABET:
            continue
        cipher_text += NUMALPH[(a * ALPHNUM[ch] + b) % M]

    return cipher_text


def decode(ciphered_text, a, b):
    if gcd(a, M) != 1:
        raise ValueError("a must be coprime to m")
