from collections import Counter
import re

def count_words(sentence):
    # note: regex needs the contraction pattern [a-z]+\'[a-z]+ before the
    # simple word pattern [a-z]+ to ensure it finds contractions correctly
    wordlist = re.findall('([0-9]+|[a-z]+\'[a-z]+|[a-z]+)', sentence.strip().lower())
    word_counts = Counter()
    for w in wordlist:
        word_counts[w] += 1
    return word_counts