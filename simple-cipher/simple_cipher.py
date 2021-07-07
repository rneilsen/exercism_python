from secrets import randbelow
from itertools import cycle
from string import ascii_lowercase

DEFAULT_KEY_LENGTH = 100

class Cipher:
    def __init__(self, key=None):
        if key is not None:
            self.key = key.lower()
        else:
            self.key = ''
            for n in range(DEFAULT_KEY_LENGTH):
                self.key += ascii_lowercase[randbelow(26)]
      
        self.cycler = cycle([ord(c) - ord('a') for c in self.key])

    def encode(self, text):
        ciphertext = ''
        for c in text:
            mod = (ord(c) - ord('a') + next(self.cycler)) % 26
            ciphertext += chr(ord('a') + mod)
        return ciphertext

    def decode(self, text):
        plaintext = ''
        for c in text:
            mod = (ord(c) - ord('a') - next(self.cycler)) % 26
            plaintext += chr(ord('a') + mod)
        return plaintext
