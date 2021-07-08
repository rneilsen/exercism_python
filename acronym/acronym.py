import re

def abbreviate(words):
    word_list = re.findall("[0-9A-Z]+(?:'[A-Z]+)?", words.strip().upper())
    return ''.join([w[0] for w in word_list])
