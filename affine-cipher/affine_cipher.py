from string import ascii_lowercase as ALPHABET
from math import gcd

GROUP_SIZE = 5

M = len(ALPHABET)
NUMALPH = {n: ALPHABET[n] for n in range(M)}
ALPHNUM = {ALPHABET[n]: n for n in range(M)}

def encode(plain_text, a, b):
    if gcd(a, M) != 1:
        raise ValueError("a must be coprime to m")
    
    cipher_text = ""
    for ch in plain_text.lower():
        if ch in ALPHABET:
            cipher_text += NUMALPH[(a * ALPHNUM[ch] + b) % M]
        elif ch in '0123456789':
            cipher_text += ch
        
    return ' '.join(cipher_text[i:i+GROUP_SIZE] 
            for i in range(0, len(cipher_text), GROUP_SIZE))


def decode(ciphered_text, a, b):
    if gcd(a, M) != 1:
        raise ValueError("a must be coprime to m")
    
    a_inv = pow(a, -1, M)

    plain_text = ""
    for ch in ciphered_text.lower().replace(' ', ''):
        if ch in ALPHABET:
            plain_text += NUMALPH[(a_inv * (ALPHNUM[ch] - b)) % M]
        elif ch in '0123456789':
            plain_text += ch
    
    return plain_text
