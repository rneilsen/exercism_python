import string

def is_pangram(sentence):
    used_chars = set(sentence.lower())
    return set(string.ascii_lowercase).issubset(used_chars)
