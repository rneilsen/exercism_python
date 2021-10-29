from string import ascii_lowercase as alphabet

GROUP_SIZE = 5

def encode(plain_text):
    cipher = {pt: ct for (pt, ct) in zip(alphabet, reversed(alphabet))}
    cipher.update({ str(n): str(n) for n in range(10) })

    cipher_text = ''
    cipher_text += ''.join([cipher[ch] for ch in plain_text.lower()
            if ch.isalnum()])

    return ' '.join([cipher_text[i:i+GROUP_SIZE] 
            for i in range(0, len(cipher_text), GROUP_SIZE)])


def decode(ciphered_text):
    return encode(ciphered_text).replace(' ', '')
