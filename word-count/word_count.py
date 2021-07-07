from collections import Counter
import re

def count_words(sentence):
    # note: regex needs the contraction pattern [a-z]+\'[a-z]+ before the
    # simple word pattern [a-z]+ to ensure it finds contractions correctly
    word_list = re.findall('[0-9a-z]+(?:\'[a-z]+)?', sentence.strip().lower())
    word_counts = Counter(word_list)
    return word_counts