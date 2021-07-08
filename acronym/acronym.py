import re

def abbreviate(words):
    word_list = re.findall("[0-9a-z]+(?:'[a-z]+)?", words.strip().lower())
    return ''.join([w[0] for w in word_list]).upper()
