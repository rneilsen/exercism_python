from string import ascii_lowercase as ALPHABET
from math import gcd

GROUP_SIZE = 5

M = len(ALPHABET)
NUMALPH = {n: ALPHABET[n] for n in range(M)}
ALPHNUM = {ALPHABET[n]: n for n in range(M)}

def encode(plain_text, a, b):
    if gcd(a, M) != 1:
        raise ValueError("a and m must be coprime.")
    
    cipher_text = transcode(plain_text, a, b, lambda n, a, b: a * n + b)

    return ' '.join(cipher_text[i:i+GROUP_SIZE] 
            for i in range(0, len(cipher_text), GROUP_SIZE))


def decode(ciphered_text, a, b):
    if gcd(a, M) != 1:
        raise ValueError("a and m must be coprime.")
    
    a_inv = pow(a, -1, M)

    return transcode(ciphered_text, a_inv, b, lambda n, a, b: a * (n - b))


def transcode(text, a, b, lookup_func):
    trans_text = ""
    for ch in text.lower():
        if ch in ALPHABET:
            trans_text += NUMALPH[lookup_func(ALPHNUM[ch], a, b) % M]
        elif ch.isnumeric():
            trans_text += ch
    return trans_text