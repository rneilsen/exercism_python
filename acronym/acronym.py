import re

def abbreviate(words):
    word_list = re.findall("[A-Z']+", words.strip().upper())
    return ''.join([w[0] for w in word_list])
