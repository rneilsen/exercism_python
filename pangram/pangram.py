import string

def is_pangram(sentence):
    used_chars = set(sentence.lower())
    
    for c in string.ascii_lowercase:
        if c not in used_chars:
            return False
    
    return True
